"""Write a function named stutter that accepts a list of integers as a parameter and replaces every element with two copies of itself. 
For example, if a list named nums stores [1, 2, 3], the call of stutter(nums) should change it to store [1, 1, 2, 2, 3, 3].

Constraints: Do not use any auxiliary collections as storage.
"""
def stutter(nums):
    i = 0
    while i < len(nums):
        nums.insert(i+1,nums[i])
        i+=2
    return nums
