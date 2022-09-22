"""
Consider the flawed function print_letters that follows, which accepts a string as its parameter and attempts to print the letters of the string,
separated by dashes. For example, the call of print_letters("Rabbit") should print R-a-b-b-i-t.
The initial code shown is incorrect. Correct it to produce the desired behavior. (Your function should print nothing if the empty string ("") is passed.)
"""
def print_letters(text):
    if(text==""):
         print()
    else:
        for i in range(0, len(text)-1):
            print(text[i] + "-", end="")
        print(text[len(text)-1])
        print() 
