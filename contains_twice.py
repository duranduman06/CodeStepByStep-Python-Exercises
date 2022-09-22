"""
Write a function named contains_twice that accepts a string and a character as parameters
and returns True if that character occurs two or more times in the string.
For example, the call of contains_twice("hello", 'l') should return True because there are two 'l' characters in that string.

"""
def contains_twice(str,chr):
    count=0
    
    for i in range(0,len(str)):
        if(str[i]==chr):
            count+=1
    if(count>=2):
          return True
    else:
          return False
