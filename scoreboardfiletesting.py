def scoreboard():
    try:
     f = open("filetest.txt", "w")
     f.write("PEBKAC \n")
     f.close()
     tst = open("filetest.txt", "r")
     print(tst.read())
    except:
     print("shit.")
     sys.exit()

scoreboard()