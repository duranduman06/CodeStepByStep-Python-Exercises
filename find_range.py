"""
Write a function named find_range that accepts a list of integers as a parameter and returns the range of values contained in the list, 
which is equal to one more than the difference between its largest and smallest element. For example, if the largest element is 17 and the smallest is 6, the range is 12. If the largest and smallest values are the same, the range is 1.

Constraints: You may assume that the list contains at least one element (that its length is at least 1). You should not modify the contents of the list.
"""
def find_range(a):
    b=min(a)
    c=max(a)
    return c-b+1
