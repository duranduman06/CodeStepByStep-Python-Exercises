"""
Write a function named get_days_in_month that accepts an integer parameter representing a month (between 1 and 12) and returns the number of days in that month in a non-leap year. 
For example, the call get_days_in_month(9) would return 30 because September has 30 days.
"""
def get_days_in_month(month):
    monthlist=[0]*13
    monthlist[1]=31
    monthlist[2]=28
    monthlist[3]=31
    monthlist[4]=30
    monthlist[5]=31
    monthlist[6]=30
    monthlist[7]=31
    monthlist[8]=31
    monthlist[9]=30
    monthlist[10]=31
    monthlist[11]=30
    monthlist[12]=31
    
    return monthlist[month]
