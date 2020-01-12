from time import sleep
import os

os.chdir(r'C:\Users\User\Documents\Pgit\Login-system')

info = open('information.txt', 'r')

Password = False

info_contents = info.read()

Username = input("Username?\n")
if Username in info_contents:
    sleep (1)
    Password = True
else:
    print ("You are not regitstered")

while Password == True:
    Password_input = input("Password\n")
    Password_in = ("("+str(Password_input)+")")
    if Password_in in info_contents:
        print ("You are now logged in")
    else:
        print("wrong password")

info.close()
quit()