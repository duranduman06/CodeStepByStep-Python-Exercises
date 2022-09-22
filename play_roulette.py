"""
Write a function named play_roulette that generates random numbers to simulate playing a simplified version of the casino game Roulette, as described below.
Roulette has a wheel laid flat with colored numbered areas numbered from 0-36. (In some versions, the wheel also has a "00", but not in this problem.) 
In each round, the wheel is spun and a ball is tossed onto it, landing on one of the numbers. 
A player bets money on groups of numbers where he/she thinks the ball will land.

For our game, the player bets that the ball will land on any even number. If the ball lands on an even number, the player wins and if the ball lands on any odd number, the player loses.
The number 0 region is special if the ball lands there, the player loses.

Your function accepts two parameters: an integer for the dollars the player starts with and another integer for the dollars the player will bet each round.
At the start, prthree headings of "bet", "spin", and "money" separated by a tab (\t). Then repeatedly use random numbers to simulate spins of the roulette wheel. 
The player bets the given amount each time, or as close to that amount as the player can afford, until their money reaches 0. If the player doesn't have enough money to bet the given amount, they bet all of their current money. 
For example, if the bet amount is $5 but the player has only $2, the player bets $2. If the player wins (ball lands on a positive even number), the player receives the amount they bet.
If the player loses (ball lands on an odd number or 0), the player loses the amount they bet. After each spin, print the bet amount, the number where the ball landed, and the player's money, separated by a tab (\t).
Keep going as long as it takes for the money to reach 0. At the end, print the maximum money the player ever had during the session.

The following log represents the console output from an example call to your function.
Because the code uses randomness, each run produces unique output, but your function should exactly match the behavior and output structure shown.

play_roulette(10, 3)
start with $ 10 and bet up to $ 3
bet     spin    money
3      11      7
3      22      10
3      5       7
3      30      10
3      24      13
3      30      16
3      32      19
3      0       16
3      9       13
3      11      10
3      1       7
3      33      4
3      12      7
3      0       4
3      19      1
1      14      2
2      34      4
3      5       1
1      31      0
max money: $ 19
Assumptions: You may assume that the parameter values passed will be reasonable that is, the starting money will be non-negative and the bet amount will be a positive integer. 
The bet amount might be greater than the starting money.

Constraints: You should not use data structures such as lists or strings to help you solve this problem. 
You may declare as many simple variables (such as ints or floats) as you like.
"""

import random
def play_roulette(money,bet_max):
    max = money
    
    print("start with $ "+str(money)+" and bet up to $ "+str(bet_max))
    print("bet\tspin\tmoney\t")
    while money != 0:
        if money >= bet_max:
            bet = bet_max
        else : 
            bet = money
        print(str(bet)+"\t",end="")
        roulette = random.randint(0,36)
        print(str(roulette)+"\t",end="")
        if roulette % 2 == 0 and roulette != 0:
            money += bet
        else:
            money -= bet
        print(str(money)+"\t",end="")
        if money > max:
            max = money
        print()
    print("max money: $ "+str(max))
