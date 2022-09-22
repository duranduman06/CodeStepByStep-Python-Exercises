"""
Write a function named second_half_letters that accepts a string as its parameter and returns an integer representing 
how many of letters in the string come from the second half of the alphabet (that is, have values of 'n' through 'z' inclusive). 
Compare case-insensitively, such that uppercase values of 'N' through 'Z' also count. For example, the call of second_half_letters("ruminates") 
should return 5 because the 'r', 'u', 'n', 't', and 's' come from the second half of the alphabet.
You may assume that every character in the string is a letter.
"""

def second_half_letters(word):
    alph=["n","o","p","q","r","s","t","u","v","w","x","y","z"]
    word=word.lower()
    syc=0
    shl=0
    for i in range(len(word)):
        if(word[i] not in alph):
            syc +=1
        else:
            shl +=1
    return shl
