"""
Write a function named print_backward that accepts a String as its parameter and prints the characters in the opposite order.
For example, a call of print_backward("hello there!") should print the following output:

!ereht olleh
If the empty string is passed, no output should be produced.
"""

def print_backward(str):
    if(str==""):
        return print()
    a=[0]*len(str)
    emptystr=""
    for i in range (0,len(str)):
        a[i]=str[len(str)-1-i]
    for i in range(0,len(a)):
        emptystr+=a[i]
    return print(emptystr)
