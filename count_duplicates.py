"""
Write a function named count_duplicates that accepts a list of integers as a parameter and that returns the number of duplicate values in the list.
A duplicate value is a value that also occurs earlier in the list. For example, if a list named a contains [1, 4, 2, 4, 7, 1, 1, 9, 2, 3, 4, 1], 
then the call of count_duplicates(a) should return 6 because there are three duplicates of the value 1, one duplicate of the value 2, and two duplicates of the value 4.

Constraints: The list could be empty or could contain only a single element in such cases, your function should return 0. Do not modify the contents of the list.
"""
def count_duplicates(li):
    myArray = []
    dupl = 0
    for i in li:
        if i in myArray:
            dupl += 1
        else:
            myArray.append( i )
    return dupl
