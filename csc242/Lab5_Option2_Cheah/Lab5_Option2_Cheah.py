"""
Ricky Cheah
3/15/2020

Driver program to test Chapter 7's "Postfix Expression Evaluator" after 
adding the ability to exponentiate integers.
"""
from model import PFEvaluatorModel

def main():
    model = PFEvaluatorModel()
    
    sourceStr1 = "2 4 3 * ^"
    print(f"{sourceStr1} = {model.evaluate(sourceStr1)}")
    
    sourceStr2 = "5 3 2 ^ +"
    print(f"{sourceStr2} = {model.evaluate(sourceStr2)}")
    
    sourceStr3 = "3 4 ^"
    print(f"{sourceStr3} = {model.evaluate(sourceStr3)}")

    sourceStr4 = "2 2 2 ^ ^"
    print(f"{sourceStr4} = {model.evaluate(sourceStr4)}")

if __name__ == "__main__":
    main()
    