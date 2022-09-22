"""
Write a function min_to_front that takes a list of integers as a parameter and that moves the minimum value in the list to the front, 
otherwise preserving the order of the elements.
For example, if a variable called list stores the following values: [3, 8, 92, 4, 2, 17, 9] and you make the call of min_to_front(list)
it should store the following values after the call: [2, 3, 8, 92, 4, 17, 9] You may assume that the list stores at least one value.
"""

def min_to_front(list):
    minnum=min(list)
    list.remove(minnum)
    emptylist=[]
    emptylist.append(minnum)
    for i in range(0,len(list)):
        emptylist.append(list[i])
    list.clear()
    for i in range(0,len(emptylist)):
        list.append(emptylist[i])
