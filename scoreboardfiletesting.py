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
