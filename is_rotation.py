"""
Write a function named is_rotation that accepts two strings as parameters and returns true if they are rotations of each other.
Two strings are considered rotations if they contain the same characters in the same relative order when wrapped around. 
For example, the call of is_rotation("abcde", "deabc") should return True. The call of is_rotation("abcde", "edcba") 
should return False because the characters are not in the same order.
A string is also considered to be its own rotation.
"""

def is_rotation(str1,str2):
    size1=len(str1)
    size2=len(str2)
    if size1!=size2:
        return False
    text=str1+str1
    if (text.count(str2)> 0):
        return True
    else:
        return False

