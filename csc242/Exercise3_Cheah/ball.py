'''
Ricky Cheah
Mar 6, 2020

The Ball Class.
'''

class Ball(object):
    '''
    A Ball Class.
    Created by taking in two arguments, a color and a shape.
    '''
    def __init__(self, color, shape):
        '''
        Initializes the ball object with passed in color and shape arguments. 
        '''
        self.color = color
        self.shape = shape
    
    def __str__(self):
        '''
        returns a string representation of the ball object with color and shape.
        '''
        return str((self.color, self.shape)) #in the form of a tuple
        
if __name__ == '__main__':
    ball1 = Ball("Red", "Square")
    print(ball1)