from time import sleep
import os

os.chdir(r'C:\Users\User\Documents\Pgit\Login-system')

info = open('information.txt', 'r+')

Password = False                                      #the password activity is 'False' because you fist need to sign in your username
Login = True                                          
register1 = False                                      #register is off at the beginning
register2 = False                                      #register is off at the beginning
error = False

info_contents = info.read()                           

while Login:
    Username_input = input("Username:\n")             #the username gets asked
    Username = ("{"+str(Username_input)+"}")    #the username gets two curly brackets to distinguish between username and password

    if Username in info_contents:                     #if the username is in the 'information.txt'... 
        sleep (1)           
        Password = True                               #... the password sequence gets activated
    else:                                             #if the username doesn't exist...
        print ("You are not registered")             #... you get asked if you want to sign up
        sleep (1)
        print ("Do you want to sign up?")
        register_answer = input("yes/y or no/n\n")    #you can answer yes or no
        if register_answer.lower() == "yes"or"y":
            register1 = True                           #if you have answered yes, 'register1' gets activated
        else:
            info.close
            quit()

    while Password == True:
        Password_input = input("Password:\n")         #here the program asks for your password
        Password_in = (str(Username)+"("+str(Password_input)+")") #the 'Password_input' gets two brackets to distinguish between username and password
        if Password_in in info_contents:              #if the password is in the 'information.txt'...
            print ("You are now logged in")           #... you get logged in 
            quit()
            info.close()                              
        else:                                         #if the password can't get found in the 'information.txt'
            print("wrong password")                   #you have to try again
    
    while register1:                                   #while regiser is active...
        which_Username = input("Which Username do you want to have?\n") #... you choose a Username
        if which_Username.lower() in info_contents:
            print ("that name already is registered")
            press_any_key = input("press any key to move on\n")
            error = True
        elif which_Username not in info_contents:
            register2 = True
        while register2:
            new_Username = ("{"+str(which_Username)+"}")            #... the username gets written in with curly brackets
            info.write(new_Username.lower())                        #... the username gets written in the 'information.txt'
            sleep (0.5) 
            which_Password = input("Which passoword do you want to have?\n")#here you can choose your password
            new_Password = ("("+str(which_Password)+")")            #the password gets brackets
            info.write(new_Password.lower())
            info.write(".")
            sleep (1)
            if error:
                print ("sorry, we couldn't set up your account.\n please try again.")
                info.close
                quit()
            else:
                print ("Your account is now set up!")
                info.close
                quit()


info.close()
quit()