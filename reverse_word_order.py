"""
Write a function named reverse_word_order that accepts a string s as its parameter and returns a new string with the words from s in reverse order. 
A word is a sequence of one or more non-space characters; words are separated by single spaces.
For example, the call of reverse_word_order("Hello what is your name?") should return "name? your is what Hello".

This problem is fairly straightforward to solve if you use the string function split. For added challenge, can you solve it without using split?
"""
def reverse_word_order(str):
    list=str.split(" ")
    res=""
    for i in range(len(list)-1,0,-1):
        res+=list[i]+" "
    res+=list[0]
    return res
