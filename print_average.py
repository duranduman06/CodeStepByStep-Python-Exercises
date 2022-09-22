"""
Write a function named print_average that repeatedly prompts the user for numbers. Once any number less than zero is typed, the average of all non-negative numbers typed is displayed. Display the average as a real number, and do not round it. The following is one example log of execution for your function:

Type a number: 7
Type a number: 4
Type a number: 16
Type a number: -4
Average was 9.0
If the first number typed is negative, do not print an average. For example:

Type a number: -2
"""
def print_average():
    sum = 0
    count = 0
    ave = -1
    number = 0
    while True :
        number = int(input("Type a number: "))
        if number < 0:
            break
        sum += number
        count += 1
    if count != 0 :
        ave = sum / count
    if ave != -1:
        
        print("Average was",ave)
