active = True

while active:
    msg_4 = input("You are running the program. Press 'Y' to continue or 'Q' to quit: ")
    if msg_4 == "Q" or msg_4 == "Y":
        if msg_4 == "Y":
            active = True
            msg = input('Enter your first name :- ')
            msg_1 = input('Enter your last name  :- ')
            print(f'welcome!! for {msg + " " + msg_1} !'
                  f' my name is robot')
            msg_3 = input('How can i help you !! please Enter your Problem :- ')
            print('sorry not find solution')
        elif msg_4 == "Q":
            active = False
    else:
        print("Invalid input. Please enter 'Y' or 'Q'.")