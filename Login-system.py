from time import sleep
import os

os.chdir(r'C:\Users\User\Documents\Pgit\Login-system')

info = open('information.txt', 'r')

Login = True
while Login:
    print ("Username:\n")
    Username = input()
    if Username.lower() in info.read():
        print ("You are on the list!")
        info.close()
    elif Username.lower() not in info.read():
        print ("You are not registered right now!")
        info.close()
        quit()

info.close()