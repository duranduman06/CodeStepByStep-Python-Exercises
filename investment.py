"""
Write a console program that calculates money earned by two investors. Use the following compound interest formula:

PV * (1 + r)n = FV
Also report the overall "quality" of the investment as from the table below:

Profit	 Category
0 - 10%	  weak
10 - 50%	medium
over 50%	strong
Match the following example output log (with user input shown like this):

Investor 1
Initial amount? 100.00
Interest rate%? .03
Num. of months? 5
Amount: $ 115.93
Profit: $ 15.93 = 16 %
Medium

Investor 2
Initial amount? 5.25
Interest rate? .08
Num. of months? 24
Amount: $ 33.29
Profit: $ 28.04 = 534 %
Strong

Have a nice day!
"""
import math
def g():
    print("Investor 1")
    
def investment():
    g()
    myFunc()
    print("")
    print("Investor 2")
    myFunc()
    print("")
    print("Have a nice day!")
def myFunc():
    pv= float(input("Initial amount? "))
    r=float(input("Interest rate%? "))
    n=float(input("Num. of months? "))
    r=1+r
    a=math.pow(r,n)
    fv=pv*a
    b=round(fv,2)
    c=abs(pv-b)
    prsntg=100 * c / pv
    print("Amount: $",b)
    print("Profit: $",round(c,2),"=",round(prsntg),"%")
    if (prsntg<10):
            print("Weak")
    elif(10<prsntg<50):
            print("Medium")
    else:
            print("Strong")
investment()
