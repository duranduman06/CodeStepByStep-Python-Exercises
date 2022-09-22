"""
Write a function named random_walk that simulates a 1-dimensional "random walk" algorithm.
A random walk is where an integer value is repeatedly increased or decreased by 1 randomly many times until it hits some threshold.
Your function should accept the integer threshold as a parameter, then start an integer at 0 and adjust it by +1 or -1 repeatedly until its value reaches positive or negative threshold.
For example, if the call of random_walk(3) is made, your function would randomly walk until it hits 3 or -3. Each time the value is adjusted, it is printed in the format shown.
When you have reached the threshold, report the number of steps that were taken from the starting poof 0, as well as the maximum position that was reached during the walk. 
(If the walk ever reaches positive threshold, that is the maximum position.)

The log below shows the output from an example call of random_walk(3) . You should match the output format below exactly, though the numbers are randomly generated. 
Use random or randint to give an equal chance of moving by +1 and -1 on each step. If the threshold parameter passed to your function is not greater than 0, your function should produce no output.

Position = 0
Position = 1
Position = 0
Position = -1
Position = -2
Position = -1
Position = -2
Position = -3
Finished after 7 step(s)
Max position = 1
(Because this problem uses random numbers, it is hard for our system to perfectly verify your code. Make sure to match our output format exactly.)
"""

import random
def random_walk(self):
    x=0
    t=0
    list=[]
    while -3<=x<=3 :
        k = random.randint(0,1)
        if (k == 1):
            print("Position =" , x)
            list.append(x)
            x=x+1
            t=t+1

        if (k == 0):
            print("Position =" , x)
            list.append(x)
            x=x-1
            t = t + 1
    print("Finished after", t ,"step(s)")
    print("Max position =",max(list))
