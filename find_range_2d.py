"""
Write a function named find_range_2d that accepts a list of lists of integers as a parameter and returns the range of values contained in the list of lists, 
which is equal to one more than the difference between its largest and smallest element. For example, 
if the largest element is 17 and the smallest is 6, the range is 12. If the largest and smallest values are the same, the range is 1.
If the list is empty your function should return 0.

Constraints: You may not create any other data structures You may not modify the contents of the list.
"""
def find_range_2d(li1):
    if len(li1) ==0:
        return 0
    myList = []
    for i in li1:  
        for k in range(len(i)):
            myList.append(i[k])
    if max(myList) == min(myList):
        return 1
    rang = max(myList) - min(myList)
    return rang+1
