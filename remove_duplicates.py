"""
Write a function named remove_duplicates that accepts a string parameter and returns a new string with all consecutive
occurrences of the same character in the string replaced by a single occurrence of that character.
For example, the call of remove_duplicates("bookkeeeeeper") should return "bokeper" .
"""

def remove_duplicates(text):
    text_list = list(text)
    i = 0
    while i < len(text_list)-1:
        if text_list[i] == text_list[i+1]:
            text_list.pop(i)
        else : 
            i += 1
        
    a = ""
    for i in range(len(text_list)):
        a += text_list[i]

    return a
