"""
What is wrong with the following code, which attempts to add all numbers from 1 to a given maximum? Correct the code so that it properly implements this behavior. 
For example the call of sum_to(5) should return 1+2+3+4+5 or 15. You may assume that the value passed is at least 1.
"""
def sum_to(n):
    if(n==1):
        return 1
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum
