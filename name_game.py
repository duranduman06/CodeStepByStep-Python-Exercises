"""
Write a complete console program that prints the following rhyme about the person's first and last name. 
You may assume that the user types a string with exactly one space.

What is your name? Fifty Cent
Fifty, Fifty, bo-Bifty
Banana-fana fo-Fifty
Fee-fi-mo-Mifty
FIFTY!

Cent, Cent, bo-Bent
Banana-fana fo-Fent
Fee-fi-mo-Ment
CENT! 
"""

def game(name):
    print("{0}, {0}, bo-B{1}".format(name, name[1:]))
    print("Banana-fana fo-F{}".format(name[1:]))
    print("Fee-fi-mo-M{}".format(name[1:]))
    print("{}!".format(name.upper()))
    print()
    
first, last = [word for word in input("What is your name? ").split()]
game(first)
game(last)
