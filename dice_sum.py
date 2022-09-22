"""
Write a function named dice_sum that prompts the user for a desired sum, then repeatedly rolls two six-sided dice until their sum is the desired sum. 
Here is the expected dialogue with the user:

Desired dice sum: 9
4 and 3 = 7
3 and 5 = 8
5 and 6 = 11
5 and 6 = 11
1 and 5 = 6
6 and 3 = 9
(Because this problem uses random numbers, our test cases check only the general format of your output. 
You must still examine the output yourself to make sure the answer is correct.)
"""
def dice_sum():
    desSum=int(input("Desired dice sum: "))
    compSum=0
    
    while(desSum!=compSum):
        a=random.randint(1,7)
        b=random.randint(1,7)
        compSum=a+b
        print(a,"and",b,"=",str(compSum))
