"""
Write a function named contains that accepts two lists of integers a1 and a2 as parameters and that returns a value indicating whether or not a2's sequence of elements appears in a1 (True for yes, False for no). The sequence of elements in a2 may appear anywhere in a1 but must appear consecutively and in the same order. For example, if variables called a1 and a2 store the following values:

a1 = [1, 6, 2, 1, 4, 1, 2, 1, 8]
a2 = [1, 2, 1]
Then the call of contains(a1, a2) should return True because a2's sequence of values [1, 2, 1] is contained in a1 starting at index 5. If a2 had stored the values [2, 1, 2], the call of contains(a1, a2) would return False because a1 does not contain that sequence of values. Any two lists with identical elements are considered to contain each other, so a call such as contains(a1, a1) should return True.

You may assume that both lists passed to your function will have lengths of at least 1. You may not use any strings to help you solve this problem, nor functions that produce strings such as str.
"""
def contains(a1,a2):
    secondCount=0
    if(len(a1)<len(a2)):
        return False
    for i in range(0,len(a1)):
            if(a1[i]==a2[secondCount]):
                secondCount+=1
                if( secondCount==len(a2)):
                    return True
            else:
                 secondCount=0
                    
                    
    return False
