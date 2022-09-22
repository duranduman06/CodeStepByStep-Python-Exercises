"""
Write a Python program that prompts the user for nonzero integers, and then prints the average of all even numbers typed. 
(When the user types 0, stop asking for input.) You may assume that the user types at least one even integer.
The following is an example output from one run of your code:

Integer? 1
Integer? 3
Integer? 2
Integer? 6
Integer? 4
Integer? 10
Integer? 9
Integer? 0
Average: 5.5

"""

def even_average():
    num=int(input("Integer? "))
    sum=0
    count=0
    average=0
    
    while num!=0:
        if num%2==0:
            sum+=num
            count+=1
            if(count!=0):
                average=float(sum/count)
        num=int(input("Integer? "))
    return print("Average: "+str(average))
