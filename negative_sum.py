"""
Write a function named negative_sum that accepts a string as a parameter representing a file name, which reads input from that file containing a series of integers, and determine whether the sum starting from the first number is ever negative. The function should pra message indicating whether a negative sum is possible and should return True if a negative sum can be reached and False if not. For example, if the file contains the following text, your function will consider the sum of just one number (38), the sum of the first two numbers (38 + 4), the sum of the first three numbers (38 + 4 + 19), and so on up to the sum of all of the numbers:

38 4 19 -27 -15 -3 4 19 38
None of these sums is negative, so the function would produce the following message and return False:

no negative sum
If the file instead contains the following numbers, the function finds that a negative sum of -8 is reached after adding 6 numbers together (14 + 7 + -10 + 9 + -18 + -10):

14 7 -10 9 -18 -10 17 42 98
It should output the following and return True, indicating that a negative sum can be reached:

-8 after 6 steps
"""
def negative_sum(x):
        file=open(x)
        content= file.read().split()
        s = 0
        c = 0
        for i in range(0, len(content)):
            k = int(content[i])
            s+= k
            c+=1
            if s < 0 :
                print(f"{s} after {c} steps")
                return True
        print("no negative sum")
        return False
