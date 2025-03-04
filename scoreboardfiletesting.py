import random, sys

pscore = 0
bscore = 0


def crackballs():
    global pscore
    global bscore
    num = random.randint(0,10)
    if num >= 5:
        pscore += 1
        print("Player")
    else:
        bscore += 1
        print("Bot")
    scoreboardsave()
    

def scoreboardsave():
    global bscore
    global pscore
    try:
     f = open("filetest.txt", "w+")
     f.write(str(bscore) + "\n" + str(pscore))
     f.close()
     tst = open("filetest.txt", "r")
     print(tst.read())
    except:
     print("File Read Error!")
     sys.exit()

crackballs()
