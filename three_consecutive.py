"""
Write a function named three_consecutive that accepts three integers as parameters and returns True if they are three consecutive numbers that is,
if the numbers can be arranged into an order such that their values differ by exactly 1. 
For example, the call of three_consecutive(3, 2, 4) would return True.
"""
def three_consecutive(a,b,c):
    if(a==b-1 and b==c-1): 
        return True
    elif(c==b-1 and b==a-1): 
        return True
    elif(c==a-1 and b==c-1): 
        return True
    elif(a==c-1 and c==b-1): 
        return True
    elif(a==b-1 and c==a-1): 
        return True
    elif(b==a-1 and b==a-1):
        return True
    else:
        return False
