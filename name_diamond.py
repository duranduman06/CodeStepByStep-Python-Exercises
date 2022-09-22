"""
Write a function named name_diamond that accepts a string as a parameter and prints it in a "diamond" format as shown below. 
For example, the call of name_diamond("MARTY") should print:

M
MA
MAR
MART
MARTY
 ARTY
  RTY
   TY
    Y
"""

def name_diamond(str):
    for i in range (0,len(str)+1):
        print(str[0:i])
    for i in range(0,len(str)+1):
        print(" "*i,str[i+1:])
