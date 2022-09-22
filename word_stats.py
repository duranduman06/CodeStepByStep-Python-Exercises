"""
Write a function named word_stats that accepts as its parameter a string holding a file name, opens that file and reads its contents as a sequence of words, and produces a particular group of statistics about the input. You should report the total number of words (as an integer), the average word length (as an un-rounded number), and the number of unique letters used from A-Z, case-insensitively. For example, suppose the file tobe.txt contains the following text:

To be  or not  TO BE,    THAT IS   the question.
For the purposes of this problem, we will use whitespace to separate words. That means that some words include punctuation, as in "be,". For the input above, your function should produce exactly the following output. The number of "unique letters" is 12 because the file contains 12 distinct letters of the alphabet from A-Z: a, b, e, h, i, n, o, q, r, s, t, and u. So the call of word_stats("tobe.txt") would produce the following console output:

Total words    = 10
Average length = 3.2
Unique letters = 12
Assumptions: You may assume that the input file exists and is readable.

Constraints: Your solution should read the file only once, not make multiple passes over the file data.
"""
def word_stats(filename):
        file=open(filename)
        content= file.read().split()
        ul =["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
             "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
             ".", ",", "!", "?", "/"]
        
        s=0
        c=0
        for i in range(0,len(content)):
            x= content[i].lower()
            s+= len(content[i])
            for k in range(0,len(ul)):
                if ul[k] in content[i]:
                    c+=1
                    ul[k]= "9"
                    
        print("Total words    =",len(content))
        print("Average length =",s/len(content))
        print("Unique letters =",c)
