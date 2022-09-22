"""
Write a function named is_palindrome that accepts a string parameter and returns True if that string is a palindrome, or False if it is not a palindrome.
For this problem, a palindrome is defined as a string that contains exactly the same sequence of characters forwards as backwards, case-insensitively. 
For example, "madam" or "racecar" are palindromes, so the call of is_palindrome("racecar") would return True.
Spaces, punctuation, and anyother characters should be treated the same 
as letters so a multi-word string such as "dog god" could be a palindrome, as could a gibberish string such as "123 $$ 321".
The empty string and all one-character strings are palindromes by our definition.
Your code should ignore case, so a string like "Madam" or "RACEcar" would also count as palindromes.
"""

def is_palindrome(word):
  
    for i in range(0,len(word)//2):
        lowerWord=word.lower()
        if(lowerWord[i]!=lowerWord[len(word)-1-i]):
            return False
    
    return True
