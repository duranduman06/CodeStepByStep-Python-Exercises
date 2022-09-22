"""
Write a function named hours that prompts for the name of, and then reads, a file of data about the number of hours worked by several employees. Each line begins with the employee's ID number, followed by their name, then a sequence of numbers representing how many hours they worked each day. For example:

123 Amy 12.5 8.5 7.25 3.25
456 Miles 4.0 11.6 6.5 12.2 2.7
802 Jessie 1.5
647 Vilde 8.0 3.5 6.5
Your program should prompt for the file name to read, then read its data and compute the total and average hours worked by each person. Use the following format:

Input file? hours.txt 
Amy (ID#123) worked 31.5 hours (7.9/day)
Miles (ID#456) worked 37.0 hours (7.4/day)
Jessie (ID#802) worked 1.5 hours (1.5/day)
Vilde (ID#647) worked 18.0 hours (6.0/day)
You may assume that the user types the name of a file that exists and is readable, and that the data is in the valid format shown above. Use the printf function to round numbers as necessary.
"""
def hours():
    inputAl=input("Input file? ")
    file=open(inputAl)
    lines=file.readlines()
    
    for line in lines:
        parts=line.split()
        id=parts[0]
        name=parts[1]
        sum=0
        count=0
        for i in range(2,len(parts)):
            sum+=float(parts[i])
            count+=1
        average=sum/count
        print(name + " (ID#" + id + ") worked " + str(round(sum,1)) + " hours (" + str(round(average,1)) +"/day)")
