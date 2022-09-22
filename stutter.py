"""
Write a function named stutter that accepts a string parameter returns a new string replacing each of its characters with two consecutive copies of that character. 
For example, A call of stutter("hello") would return "hheelllloo".
"""
def stutter(str):
    newArray=[0]*len(str)
    txt=""
    for i in range(0,len(str)):
        newArray[i]=str[i]*2
    for i in range(0,len(newArray)):
        txt+=newArray[i]
    return txt
