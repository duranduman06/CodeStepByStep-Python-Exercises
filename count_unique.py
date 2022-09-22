"""
Write a function named count_unique that takes three integers as parameters and that returns the number of unique integers among the three. 
For example, the call count_unique(18, 3, 4) should return 3 because the parameters have 3 different values. 
By contrast, the call count_unique(6, 7, 6) should return 2 because there are only 2 unique numbers among the three parameters: 6 and 7.
"""
def count_unique(x,y,z):
    count=0
    if(x==y and x==z and y==z):
        count+=1
        return count
    if(x!=y):
        count+=1
    if(x!=z):
        count+=1
    if(y!=z):
        count+=1

    return count
