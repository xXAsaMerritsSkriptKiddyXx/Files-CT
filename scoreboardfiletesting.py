import random

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
    

def scoreboard():
    try:
     f = open("filetest.txt", "w")
     f.write("PEBKAC")
     f.close()
     tst = open("filetest.txt", "r")
     print(tst.read())
    except:
     print("AUUUUUUUUUUUUGHHHHHHHHHHHHHHHHH.")
     sys.exit()

scoreboard()


crackballs()
