"""
Modify the previous problem's word_wrap function into a new function word_wrap3 that only wraps whole words, never chopping a word in half. 
Assume that a word is any whitespace-separated token and that all words are under 60 characters in length.
"""
def word_wrap3(a):
    with open(a) as f:

        lines = f.readlines()
        lines = [k.replace('\n', '') for k in lines]
        count = 0

        for i in range(0, len(lines)):
            if len(lines[i]) <= 60:
                print(lines[i], end="")

            else:
                texts = lines[i].split(" ")
                for text in texts:
                    if count+len(text)<=60:
                        print(text,end=" ")
                        count+=len(text)+1
                    else:
                        print()
                        print(text,end=" ")
                        count=len(text)+1

                count = 0
            print()
