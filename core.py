import os

ip = "192.168.0.194"
localFile = "test.txt"

os.system("scp n30b4rt@192.168.0.194:/home/n30b4rt/" + localFile + " " + localFile)