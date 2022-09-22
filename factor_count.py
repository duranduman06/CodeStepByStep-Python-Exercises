"""
Write a function named factor_count that accepts an integer (assumed to be positive) as its parameter and returns a count of its positive factors. 
For example, the eight factors of 24 are 1, 2, 3, 4, 6, 8, 12, and 24, so the call of factor_count(24) should return 8.
"""

def factor_count(number):
    count=0
    if(number>0):
        for i in range(1, number+1):
            if(number%i==0):
                count+=1
        return count
    return -1
