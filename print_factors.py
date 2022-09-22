"""
Write a function named print_factors that accepts an integer as its parameter and uses a fencepost loop to print the factors of that number, separated by the word " and ". 
For example, the number 24's factors should print as:

1 and 2 and 3 and 4 and 6 and 8 and 12 and 24
You may assume that the number parameter's value is greater than 0.
"""

def print_factors(num):
    for i in range(1,num+1):
        if(num==i):
            print(str(i))
        elif(num%i==0):
            print(str(i),"and",end=" ")
