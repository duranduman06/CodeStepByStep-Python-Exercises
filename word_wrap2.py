"""
Modify the previous problem's word_wrap function into a new function word_wrap2 that 
accepts two parameters representing an input file and an output file name, and outputs the newly wrapped text from the input file to the given output file.
Also, modify it to use a constant for the maximum line length rather than hard-coding 60.
"""
def word_wrap2(a,a1):
    with open(a) as f:
        with open(a1,"w")as out:
            lines=f.readlines()
            lines=[k.replace('\n','') for k in lines]
            count=0
            for i in range(0,len(lines)):
                if len(lines[i])>59:
                    for j in range(0,len(lines[i])):
                        out.write(lines[i][j])
                        count+=1
                        if count==60:
                            out.write("\n")
                            count=0
                    out.write("\n")
                    count=0
                else:
                    for k in lines[i]:
                        out.write(k)
                    out.write("\n")
