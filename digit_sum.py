"""
Write a function named digit_sum that accepts an integer as a parameter and returns the sum of the digits of that number. 
For example, the call of digit_sum(29107) returns 2+9+1+0+7 or 19. For negative numbers, return the same value that would result if the number were positive.
For example, digit_sum(-456) returns 4+5+6 or 15.
"""

def digit_sum(num):
    if(num<0):
        num=(-1) * num
        
    num=str(num)
    sum=0
    
    for i in range(0,len(num)):
        sum+=int(num[i])
    return sum
