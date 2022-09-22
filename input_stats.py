"""
Write a function named input_stats that accepts a string parameter representing a file name, then opens/reads that file's contents and prints information to the console about the file's lines. Report the length of each line, the number of lines in the file, the length of the longest line, and the average characters per line, in exactly the format shown below. You may assume that the input file contains at least one line of input. For example, if the input file carroll.txt contains the following data:

Beware the Jabberwock, my son,
the jaws that bite, the claws that catch,

Beware the JubJub bird and shun
the frumious bandersnatch.
Then the call of input_stats("carroll.txt") should produce the following console output:

Line 1 has 30 chars
Line 2 has 41 chars
Line 3 has 0 chars
Line 4 has 31 chars
Line 5 has 26 chars
5 lines longest = 41, average = 25.6
If the input file does not exist or is not readable, your function should prno output. If the file does exist, you may assume that the file contains at least 1 line of input.

Constraints: Your solution should read the file only once, not make multiple passes over the file data.
"""

def input_stats(filename):
    f=open(filename)
    lines=f.readlines()
    lenparts=[]
    sum=0
    for i in range(0,len(lines)):
        res=""
        parts=lines[i]
        res+=parts
        lenparts=[len(x) for x in lines ]
        sum+=lenparts[i]
        print("Line",str(i+1),"has",str(len(res)-1),"chars")
                   
    print(str(len(lines)),"lines; longest =",str(max(lenparts)-1)+", average =",str(sum/len(lines)-1))
