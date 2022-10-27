#Author: Michael Lagardera
#GitHub username: scott5Tots
#Date: 10/26/2022
#Description: program takes two positive integers and "multiplies" them by adding.

def mult(mul1, mul2):
    '''function takes two integers and multiplies them.'''
    if(mul1 == 0):
        #stops sequence once num1 reaches 0
        return 0
    else:
        #adds mul2 to decresing integers of mul1
        return mul2+mult(mul1-1, mul2)
