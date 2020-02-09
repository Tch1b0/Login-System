from time import sleep
import os

current_path = os.path.dirname(os.path.realpath(__file__))   # Get the current path
os.chdir(current_path)                                       #the current path gets set 

info = open('information.txt', 'r+')

password = False                                      #the password activity is 'False' because you fist need to sign in your username
login = True                                          
register1 = False                                     #Register is off at the beginning
register2 = False                                     #Register is off at the beginning
error = False
Wrong_Password = 0

info_contents = info.read()                           

while login:
    username_input = input("Username:\n")             #the username gets asked
    username = ("{"+str(username_input.lower())+"}")    #the username gets two curly brackets to distinguish between username and password

    if username in info_contents:                     #if the username is in the 'information.txt'... 
        sleep (1)           
        password = True                               #... the password sequence gets activated
    else:                                             #if the username doesn't exist...
        print ("You are not registered")             #... you get asked if you want to sign up
        sleep (1)
        print ("Do you want to sign up?")
        register_answer = input("yes/y or no/n\n")    #you can answer yes or no
        if register_answer.lower() == "yes"or"y":
            register1 = True                           #if you have answered yes, 'register1' gets activated
        else:
            info.close()
            quit()

    while password == True:
        if Wrong_Password == 3:
            exit("access denied")
        password_input = input("Password:\n")         #here the program asks for your password
        password_in = (str(username)+"("+str(password_input)+")") #the 'Password_input' gets two brackets to distinguish between username and password
        if password_in in info_contents:              #if the password is in the 'information.txt'...
            print ("You are now logged in")           #... you get logged in 
            info.close()
            quit()                             
        else:                                         #if the password can't get found in the 'information.txt'
            print("wrong password")                   #you have to try again
            Wrong_Password = Wrong_Password + 1
    
    while register1:                                   #while regiser is active...
        which_username = input("Which Username do you want to have?\n") #... you choose a Username
        if which_username.lower() in info_contents:
            print ("that name already is registered")
            press_any_key = input("press any key to move on\n")
            error = True
        elif which_username not in info_contents:
            register2 = True
        while register2:
            new_username = ("{"+str(which_username)+"}")            #... the username gets written in with curly brackets
            info.write(new_username.lower())                        #... the username gets written in the 'information.txt'
            sleep (0.5) 
            which_password = input("Which passoword do you want to have?\n")#here you can choose your password.
            new_password = ("("+str(which_Password)+")")            #the password gets brackets
            info.write(new_password.lower())
            info.write(".")
            sleep (1)
            if error:
                print ("sorry, we couldn't set up your account.\n please try again.")
                info.close()
                quit()
            else:
                print ("Your account is now set up!")
                info.close()
                quit()


info.close()
quit()