"""
Write a function named even_sum that prompts the user for many integers and print the total even sum and maximum of the even numbers.
You may assume that the user types at least one non-negative even integer.

how many integers? 4
next integer? 2
next integer? 9
next integer? 18
next integer? 4
even sum = 24
even max = 18

"""
def even_sum():
    numberOfNum=int(input("how many integers? "))
    num=[0]*numberOfNum
    evensum=0
    evenmax=0
    for i in range(0,numberOfNum):
        inputNum=int(input("next integer? "))
        if(inputNum%2==0):
            evensum+=inputNum
            num[i]=inputNum
    evenmax=max(num)
    return print("even sum =",evensum,"\n"+"even max =",evenmax )
