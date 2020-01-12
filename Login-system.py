from time import sleep
import os

os.chdir(r'C:\Users\User\Documents\Pgit\Login-system')

info = open('information.txt', 'r+')

Password = False
Login = True
register = False

info_contents = info.read()

while Login:
    Username_input = input("Username:\n")
    Username = ("{"+str(Username_input)+"}")
    if Username in info_contents:
        sleep (1)
        Password = True
    else:
        print ("You are not regitstered")
        sleep (1)
        print ("Do you want to register?")
        register_answer = input()
        if register_answer == "yes"or"y":
            register = True

    while Password == True:
        Password_input = input("Password:\n")
        Password_in = ("("+str(Password_input)+")")
        if Password_in in info_contents:
            print ("You are now logged in")
            quit()
            info.close()
        else:
            print("wrong password")
    
    while register:
        which_Username = input("Which Username do you want to have?\n")
        new_Username = ("{"+str(which_Username)+"}")
        info.write(new_Username)
        sleep (0.5)
        which_Password = input("Which passoword do you want to have?\n")
        new_Password = ("{"+str(which_Password)+"}")
        info.write(new_Password)
        sleep (1)
        print ("Your account is now set up!")
        info.close
        quit()



info.close()
quit()