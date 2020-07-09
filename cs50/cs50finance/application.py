import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# for showing money in a proper format
@app.template_filter()
def moneyFormat(value):
    return '${0:,.2f}'.format(value)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    userid=session["user_id"]

    cash = db.execute("SELECT * FROM users WHERE id = :userid", userid=userid)[0]["cash"]
    rows = db.execute("SELECT * FROM usershares where userID = :userid" , userid=userid)
    totaluserworth = cash # keep track of total user worth (stocks + cash)
    for row in rows:
        stock = row['stock'] # stock symbol
        shares = row['shares'] # number of shares
        worth = lookup(stock)['price'] # current price of a single share
        row['worth'] = worth # price of SINGLE share
        totalworth = worth*shares
        row['totalworth'] = totalworth # update total worth of all the shares of that symbol
        totaluserworth += totalworth # user's total asset
        db.execute("UPDATE usershares SET worth=:worth, totalworth=:totalworth WHERE userid = :userid AND stock=:stock",worth=worth, userid=userid, stock=stock, totalworth=totalworth) # This might not be necessary

    # this second rows is so we could order based on DESC
    # if we don't do this, the redirect after we buy won't show the stocks in descending order
    # because the newly bought will just be added to the last row.
    rows = db.execute("SELECT * FROM usershares where userID = :userid ORDER BY totalworth DESC" , userid=userid)
    return render_template("index.html", rows=rows, cash=cash, totaluserworth = totaluserworth)

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    userid=session["user_id"]
    rows = db.execute("SELECT * FROM userhistory where userID = :userid", userid=userid)
    for row in rows:
        print(row)
    return render_template("history.html", rows = rows)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    if request.method == "GET":
        try:
            # Forget any user_id
            # try/except is to make wrong username/password flash work. If no user is logged in, won't session.clear() so flash is kept.
            if session["user_id"]:
                session.clear()
                flash("Logged Out!", "alert-warning") # a user manually typed in /login at URL, because no LOGIN button to push once logged in. So we log them out.
                return render_template("login.html")

        # a user genuinely wants to login, through LOGIN button or redirected from "/"
        except:
            return render_template("login.html")

    # User reached here via POST (as by submitting the form in login.html)
    else:
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Must provide username!", "alert-danger")
            return redirect("/login")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Must provide password!", "alert-danger")
            return redirect("/login")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("Invalid username and/or password!", "alert-danger")
            return redirect("/login")

        # Once verified, remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Welcome Back!", "alert-success")
        return redirect("/")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    flash("Logged Out!", "alert-danger")
    return redirect("/")

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html", mode = 'requestquote') # mode to decide which html "mode" to display

    else: # user has submitted a stock name
        stockname = request.form.get("stockname")
        response = lookup(stockname)
        if response:
            return render_template("quote.html", mode = 'displayquote', response = response)
        else:
            flash("No such stock!", "alert-danger")
            return redirect("/quote")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "GET":
        return render_template("register.html")
    else:
        username = request.form.get("username")
        if not username:
            return apology("must provide username", 403)
        password = request.form.get("password1")
        passwordconfirm = request.form.get("password2")
        if not password or not passwordconfirm or password != passwordconfirm:
            return apology("must provide matching passwords", 403)

        # check if username is available
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=username)
        # print(rows)
        if len(rows) != 0: # username taken
            return apology("username taken", 409) # 409 is conflict


        hashedpassword = generate_password_hash(password)
        db.execute("INSERT INTO users (username, hash) VALUES (:username, :hashedpassword)",
                    username = username, hashedpassword = hashedpassword)

        rows = db.execute("SELECT * FROM users WHERE username = :username",
                            username=request.form.get("username"))
        session["user_id"] = rows[0]["id"] #this logs user in after registration
        flash("Registered and logged in!", "alert-success")
        return redirect("/")

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "GET": # getting to the buy page
        return render_template("buy.html")
    else: # submitting final buy request
        stockname = request.form.get("stockname").upper() # .upper() for consistency
        response = lookup(stockname) # dict returned
        if response:
            shares = int(request.form.get("stockamount")) # number of shares to buy *need to convert str to int!
            price = response["price"] # price of each share
            userid = session["user_id"] # minimize repeats
            fullname = response["name"] # complete name of stock
            # print(type(shares), type(price)) # int and float
            totalCost = round(shares*price,2)
            datetime = db.execute("SELECT datetime('now')")[0]["datetime('now')"] # dict is the format returned, this is how to access it
            # print(price, datetime)
            # print(session["user_id"])
            cash = db.execute("SELECT cash FROM users WHERE id = :userid",userid=userid)[0]['cash']
            # print(cash, price)
            if cash > totalCost:
                cash -= totalCost
                db.execute("UPDATE users SET cash = :cash WHERE id = :userid",cash = cash, userid=userid)
                db.execute("INSERT INTO userhistory (userID, stock, useraction, price, transacted) VALUES (:userid, :stock, :useraction, :price, :datetime)",
                            userid=userid, stock=stockname, useraction=shares, price=price, datetime=datetime)

                currentShares = db.execute("SELECT * FROM usershares WHERE userID = :userid AND stock=:stock", userid=userid, stock=stockname)

                if currentShares:
                    updatedShares = currentShares[0]['shares'] + shares
                    worth = currentShares[0]['worth'] + totalCost
                    db.execute("UPDATE usershares SET shares=:updatedShares, worth=:worth WHERE userID = :userid AND stock=:stock",
                                updatedShares=updatedShares, worth=worth, userid=userid, stock=stockname)
                else:
                    # print(totalCost)
                    db.execute("INSERT INTO usershares (userID, stock, fullname, shares, worth) VALUES (:userid, :stock, :fullname, :shares, :worth)",
                    userid=userid, stock=stockname, fullname=fullname, shares=shares, worth=totalCost) # worth is totalCost b/c never had this stock.
                flash ("Bought!", "alert-primary")
                return redirect("/")
            else:
                flash("You can't afford it!", "alert-danger")
                return redirect("/buy")
        else:
            flash("Please enter a valid stock name!", "alert-danger")
            return redirect("/buy")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    # NEED THIS TO CASCADE DELETE! PRAGMA foreign_keys = ON;
    """Sell shares of stock"""
    userid = session["user_id"] # both get and post methods use this

    if request.method == "GET":
        rows = db.execute("SELECT stock FROM usershares WHERE userID = :userid", userid = userid)
        if rows:
            return render_template("sell.html", rows = rows)
        else:
            flash("You don't have any stocks!", "alert-danger")
            return redirect("/")

    else:
        if request.form.get("stockname"): # user has indeed selected a stock
            stock = request.form.get("stockname").upper()
            response = lookup(stock)
        else:
            flash("You did not select a stock to sell!", "alert-danger")
            return redirect("/sell")

        if response:
            # Thisif portion is now redundant because of the <option> tag in sell.html, since user can't
            # input a stock they don't own.
            rows = db.execute("SELECT * FROM usershares WHERE userID = :userid AND stock = :stock", userid=userid, stock=stock)
            if len(rows) != 1:
                flash("You don't own any shares of that stock!", "alert-danger")
                return redirect("/sell")
            else:
                ownedshares = rows[0]['shares']
                sellingshares = int(request.form.get("stockamount")) # remember to convert to int
                # print(sellingshares, ownedshares)

                if sellingshares > ownedshares: # trying to sell more than you own
                    flash(f"You only own {ownedshares} shares of {stock}!", "alert-danger")
                    return redirect("/sell")
                else:
                    currentworth = rows[0]['totalworth']
                    price = response["price"]

                    updatedworth = currentworth - sellingshares*price
                    updatedshares = ownedshares - sellingshares

                    cash = db.execute("SELECT cash FROM users WHERE id = :userid",userid=userid)[0]['cash']
                    updatedcash = cash + sellingshares*price
                    db.execute("UPDATE users SET cash = :updatedcash WHERE id =:userid", updatedcash=updatedcash, userid=userid)
                    print(currentworth, price, updatedworth)

                    datetime = db.execute("SELECT datetime('now')")[0]["datetime('now')"]

                    db.execute("INSERT INTO userhistory (userID, stock, useraction, price, transacted) VALUES (:userid, :stock, :useraction, :price, :datetime)",
                                userid=userid, stock=stock, useraction=-sellingshares, price=price, datetime=datetime)


                    if updatedshares: #does not == 0, user still has shares
                        db.execute("UPDATE usershares SET shares = :updatedshares, totalworth=:updatedworth WHERE userID = :userid AND stock=:stock",
                                    updatedshares=updatedshares, updatedworth=updatedworth,userid=userid, stock=stock)
                    else: # user has no more shares
                        db.execute("DELETE FROM usershares WHERE userID = :userid AND stock=:stock",
                                    userid=userid, stock=stock)

                    flash("Sold!", "alert-info")
                    return redirect("/")

        # don't need this anymore because we have <option> instead of <input>, all options are taken from database so they must be correct
        # else:
        #     return apology("INVALID STOCK NAME")

def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__ == "__main__":
    db = SQL("sqlite:///finance.db")
    rows = db.execute("SELECT * FROM users")
    print(rows)
