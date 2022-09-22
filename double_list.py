"""
Write a function named double_list that takes a list of strings as a parameter and that replaces every string with two of that string. 
For example, if the list stores the values ["how", "are", "you?"] before the function is called, 
it should store the values ["how", "how", "are", "are", "you?", "you?"] after the function finishes executing.
"""
def double_list(li):
    emptylist=[]
    for i in range(0,len(li)):
        emptylist.append(li[i])
        emptylist.append(li[i])
    li.clear()
    for i in range(0,len(emptylist)):
        li.append(emptylist[i])
