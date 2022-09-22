"""
Write a function named class_presidents that tallies votes for presidents of two school classes.
Somehow the vote tallies for sophomore and junior class presidents got mixed up! Your function should accept as its parameter a string representing a filename of vote results.
It should output the next sophomore and junior class presidents.
The file format looks like the following:

Jared s 25 Sophie j 12 Tom j 44 Isaac s 30 Emily s 60 Russ s 23 Madison j 20
The file repeats the pattern name year votes. The year is either "s" for sophomore or "j" for junior. Your program should output the candidate in each presidential race with the most votes, and how many votes they got. 
Specifically, if this file were named candidates.txt, your function should produce the following output:

Sophomore Class President: Emily (60 votes)
Junior Class President: Tom (44 votes)
You may assume that there are no ties and that each class has one single person who received the most votes.
"""
def class_presidents(x):
        file=open(x)
        content = file.read().split()
        seniorVotes = []
        juniorVotes = []
        seniorNames = []
        juniorNames = []
        for i in range(0, len(content) , 3):
            if content[i+1] == "s" :
                seniorVotes.append(content[i+2])
                seniorNames.append(content[i])
            elif content[i+1] == "j" :
                juniorVotes.append(content[i+2])
                juniorNames.append(content[i])
        m = seniorVotes.index(max(seniorVotes))
        k = juniorVotes.index(max(juniorVotes))
        print(f"Sophomore Class President: {seniorNames[m]} ({max(seniorVotes)} votes)")
        print(f"Junior Class President: {juniorNames[k]} ({max(juniorVotes)} votes)")
