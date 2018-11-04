#Kaivalya Vohra 2018
#import libraries
from ast import literal_eval
from collections import OrderedDict
from time import sleep

#open highscore textfile
textfile = open("highscores.txt", "r")
scores = sorted(literal_eval(textfile.read()).items(),
                key=lambda t: t[1], reverse=True)

#print table of highscores
def printscores(scoredict):
    print("High Scores\nNo     Name        Score")
    for i in scoredict:
        sleep(0.3)
        print(scoredict.index(i) + 1, "    ", i[0], "         ", i[1])

#add new score if it is within top 5
def addscore(name, score, scores):
    x = -1

    for i in range(0, 5):

        if score > scores[i][1]:
        	x = i
        	break
    if x > -1:
        scores.insert(x, (name, score))
    if len(scores) == 6:
        del(scores[-1])

    arr = {}
    for i in scores:
        arr[i[0]] = i[1]

    textfile = open("highscores.txt", "w")

    textfile.write(str(arr))

