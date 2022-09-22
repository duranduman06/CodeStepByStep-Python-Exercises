"""
Write a function named flip_lines that accepts as its parameter a string representing a file name, opens that file and reads its contents as a sequence of lines, and writes to the console the same file's contents with successive pairs of lines reversed in order, with alternating capitalization. For example, if the input file named carroll.txt contains the following text:

TWAS brillig and the Slithy Toves
did GYRE and gimble in the Wabe.
All mimsey were the Borogroves,
and the mome RATHS outgrabe.

"Beware the Jabberwock, my Son,
the JAWS that bite, the claws that Catch,
Beware the JubJub bird and SHUN
The Frumious Bandersnatch."
Then the call of flip_lines("carroll.txt") should print the first pair of lines in reverse order, then the second pair in reverse order, then the third pair in reverse order, and so on. It should produce the following console output:

DID GYRE AND GIMBLE IN THE WABE.
twas brillig and the slithy toves
AND THE MOME RATHS OUTGRABE.
all mimsey were the borogroves,
"BEWARE THE JABBERWOCK, MY SON,

BEWARE THE JUBJUB BIRD AND SHUN
the jaws that bite, the claws that catch,
THE FRUMIOUS BANDERSNATCH."
Notice the alternation between all-uppercase and all-lowercase. Also note that a line can be blank, as in the third pair. An input file can have an odd number of lines, as in the one above, in which case the last line is printed in its original position. You should not make any assumptions about how many lines are in the file.

If the input file does not exist or is not readable, your function should instead pra message in exactly the following format:

Unable to open input file "carroll.txt"!
Constraints: Your solution should read the file only once, not make multiple passes over the file data.
"""
def flip_lines(a):
    f = open(a)
    l = f.readlines()
    
    
    for i in range(0,len(l)-1,2):
        l[i],l[i+1] = l[i+1],l[i]
        
        print(l[i].upper(),end="")
        print(l[i+1].lower(),end="")

    if len(l) % 2 == 1:
        print(l[-1].upper())
