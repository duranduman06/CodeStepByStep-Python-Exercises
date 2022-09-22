"""
Write a function named first_digit that returns the first digit of an integer. For example, first_digit(3572) should return 3.
It should work for negative numbers as well. For example, first_digit(-947) should return 9.
"""
def first_digit(num):
        if(num<0):
            num=abs(num)
        numlen=len(str(num))
        for i in range(0,numlen):
            digit=num % 10
            num=num//10
        return digit
