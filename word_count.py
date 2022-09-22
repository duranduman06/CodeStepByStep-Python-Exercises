"""
Write a function named word_count that accepts a String as its parameter and returns the number of words in the String.
A word is a sequence of one or more nonspace characters (any character other than ' ').
For example, the call word_count("hello") should return 1, the call word_count("how are you?") should return 3, 
the call word_count(" this   string has     wide     spaces   ") should return 5, and the call word_count(" ") should return 0.
"""

def word_count(str):
    if(str==" "):
        return 0
    myArray=str.split()
    return len(myArray)
