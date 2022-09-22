"""
Write a function named remove_all that accepts a string and a character as parameters, and removes all occurrences of the character.
For example, the call of remove_all("Summer is here!", 'e') should return "Summr is hr!". Do not use the string replace function in your solution.
"""

def remove_all(str,chr):
       return str.replace(chr,"")
