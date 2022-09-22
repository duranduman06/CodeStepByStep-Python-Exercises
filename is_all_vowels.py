"""
Write a function named is_all_vowels that returns whether a string consists entirely of vowels (a, e, i, o, or u, case-insensitively). 
For example, is_all_vowels("ei_e_io") should return True while is_all_vowels("banana") should return False.
For this problem, you may assume that a working solution already exists to the previous problem, is_vowel, and you may call it in your solution.
"""

def is_all_vowels(text):
    true=0
    if(text==""):
        return True
    for i in range(0,len(text)):
        if(text[i]=="a" or text[i]=="e" or text[i]=="i" or text[i]=="o" or text[i]=="u" or text[i]=="A" or text[i]=="E" or text[i]=="I" or text[i]=="O" or text[i]=="U"):
            true+=1
        else:
            return False
    return True
