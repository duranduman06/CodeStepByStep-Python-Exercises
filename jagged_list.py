"""
Write a piece of code that constructs a jagged two-dimensional list of integers named jagged with five rows and an increasing number of columns in each row, 
such that the first row has one column, the second row has two, the third has three, and so on. 
The list elements should have increasing values in top-to-bottom, left-to-right order (also called row-major order).
In other words, the list's contents should be the following:

1
2, 3
4, 5, 6
7, 8, 9, 10
11, 12, 13, 14, 15
"""
def jagged_list(): 
    jagged=[]
    new=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    t=0
    k=1
    for i in range(1,6):
        jagged.append(new[t:k])
        t += i
        k += i + 1
