"""
Write a function named word_wrap that accepts an input file name as its parameter and outputs each line of the file to the console, word-wrapping all lines that are longer than 60 characters.
For example, if a line contains 112 characters, the function should replace it with two lines: one containing the first 60 characters and another containing the final 52 characters.
A line containing 217 characters should be wrapped into four lines: three of length 60 and a final line of length 37.
"""
def word_wrap(filename):
        file=open(filename)
        content = file.read().splitlines()
        for line in content:
            myfunc(line)
def myfunc(line):
    s = len(line)
    i=0
    j=60
    while s >= 60 :
        print(line[i:j])
        s-=60
        i+=60
        j+=60
    while 0 <= s< 60 :
        print(line[i:])
        break
