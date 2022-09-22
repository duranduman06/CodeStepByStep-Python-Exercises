"""
Write a function named print_palindrome that prompts the user to enter one or more words and prints whether the entered string is a palindrome 
(i.e., reads the same forwards as it does backwards, like "abba" or "racecar"). For an added challenge, 
make the code case-insensitive, so that words like "Abba" and "Madam" will be considered palindromes. Here is the resulting output for two calls:

Type one or more words: racecar
racecar is a palindrome!
Type one or more words: hello
hello is not a palindrome.
"""

def print_palindrome():
    word=str(input("Type one or more words: "))
    
    for i in range(0,len(word)//2):
        lowerWord=word.lower()
        if(lowerWord[i]!=lowerWord[len(word)-1-i]):
            return print(word,"is not a palindrome.")
    
    return print(word,"is a palindrome!")
