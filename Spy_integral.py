                                                    # SPY CHAT APP

from Spy_Details import spy, Spy, chatMessage, friends, dic_special_words
from steganography.steganography import Steganography
from datetime import datetime
from colorama import init
from colorama import Fore

init()    # init() used to initialize colorama


# List of Status messages(msg) the spy had
msgs_of_status = ['Hello spies,available now', 'Working on secret mission', 'Live the life to the fullest', 'Important messages only', 'Having fun with friends']


def status_upd():   # Function to update the status

    updated__msg = None
    if spy.current_status_msg != None:      # checking if the spy has anu current status msg or not
        print 'Your current status message is:' + ' ' + spy.current_status_msg
    else:
        print 'There is no status message at present..'

    stat_choice = raw_input('Do you want to select status message from old status updates?(y/n)')
    if stat_choice == 'Y' or stat_choice == 'y':
        pos = 1
        for msg in msgs_of_status:      # listing the old status msg
            print str(pos) + '.' + ' ' + msg
            pos = pos+1

        select = int(raw_input('Which status message do you want to select?(Select the position number of the message.)'))
        if select <= len(msgs_of_status):    # checking if selected msg lies in the status msg list or not
            updated_msg = msgs_of_status[select-1]
            print 'Your updated status message is:' + ' ' + updated_msg
        else:
            print 'You have selected wrong choice.press either y or n... '

    elif stat_choice == 'N' or stat_choice == 'n':      # if the spy wants to add a new status msg
        new_msg = raw_input('Enter you new status message:\n')
        if len(new_msg) > 0:
            updated_msg = new_msg
            msgs_of_status.append(updated_msg)
            print 'Your updated status message is' + ' ' + updated_msg
        else:
            print'You have not entered anything.Please try again.Press y or n...'
    else:
        print'Chosen wrong option!! You have not updated your status message!!!'

    return updated_msg


def add_friend():   # add a new friend to friend list
    new_friend = Spy('', '', 0, 0.0)

    print'You decided to add a spy friend...'

    new_friend.spy_name = raw_input("what is your friend's name?")
    new_friend.spy_salutation = raw_input('What should we call them, Mr. or Ms.? ')
    new_friend.spy_age = int(raw_input("what is your friend's age?"))
    new_friend.spy_rating = float(raw_input("what is your friend's rating"))

    # checking the credentials if the new friend can be added or not
    if len(new_friend.spy_name) > 0 and new_friend.spy_age > 12 and new_friend.spy_rating > spy.spy_rating:
        friends.append(new_friend)
        print 'Congrats.. ' + new_friend.spy_salutation + ' ' + new_friend.spy_name + ' ' + 'age:' + str(new_friend.spy_age) + ' ' + 'rating:' + str(new_friend.spy_rating) + ' ' + 'is added to the spy community.'
    else:
        print "Sorry.Didn't fulfill the required conditions.\n Thus not added to spy community."

    return len(friends)


def select_a_friend():    # selecting a friend to chat with
    f_pos = 0
    for friend in friends:      # displaying the friends list
        print str(f_pos+1)+'. ' + friends[f_pos].spy_name
        f_pos = f_pos+1

    f_choice = raw_input('With which friend you want to chat with (Select the position of the friend)?')
    f_choice_ind = int(f_choice)-1  # calculate the index of the friend selected
    return f_choice_ind


def send_msg():     # send the msg to selected friend using Steganography
    fri_choice = select_a_friend()

    input_img = raw_input('What is the name of the image?')     # name of the file in which encoding of secret msg is done
    output_path = 'output.jpg'      # name of the file generated after encoding the secret msg in it
    mesg = raw_input('Write the message you want to hide in the image..')    # writing msg to hide in image
    Steganography.encode(input_img, output_path, mesg)      # using Steganography hiding msg in image


    new_mesg = chatMessage(mesg, True)

    friends[fri_choice].chats.append(new_mesg)      # appending msg in chats list

    print 'your message is encoded in the image.'
    print 'Now you can send it to your spy friend..'


def read_msg():   # reading the decoded msg using Steganography
    sender = select_a_friend()
    output_path = raw_input('What is the file name?')   # Writing the file name generated by Steganography
    secret_msg = Steganography.decode(output_path)      # Decoding the secret msg

    split_msg = secret_msg.split(" ")       # splitting the secret msg

    a = dic_special_words.keys()        # obtaining keys from the dictionary of special words

    place = 0
    for x in a:
        if x in split_msg:
            print 'Special words in msg %s: %s' %(x, dic_special_words.get(x))       # printing the special word with its value
            place = place+1
        else:
            continue

    if len(split_msg) > 100:   # removing the friend from list if they speak too much
        print '%s Has been removed from spy list !!' % (friends[sender].spy_name)
        friends.remove(friends[sender])
    if len(secret_msg) == 0:    # if image does not contain any msg
        print 'There is no message in the image ..'
    new_mesg = chatMessage(secret_msg, False)
    friends[sender].chats.append(new_mesg)      # appending msg to chats list

    print 'Your message is saved and secured.'


def read_chat_history():    # reading chat history of the selected friend

    friend_select = select_a_friend()

    for chat in friends[friend_select].chats:   # displaying the chat history of selected friend
        # using colorama to display coloured output on terminal and datetime to show time
        if chat.sent_by_me:
            print (Fore.BLUE + chat.time.strftime('[%d %B %Y, %I:%M:%S]') + ' ' + Fore.RED + 'You said:' + ' ' + Fore.BLACK + chat.msg)
        else:
            print (Fore.BLUE + chat.time.strftime('[%d %B %Y, %I:%M:%S]') + ' ' + Fore.RED + friends[friend_select].spy_name + ':' + ' ' + Fore.BLACK + chat.msg)



ask = raw_input('Do you want to continue as %s %s(Yes/No)?' %(spy.spy_salutation, spy.spy_name))    # asking user to continue as default spy or not


def start_chat(spy):    # starting spy chat app

    spy.spy_name = spy.spy_salutation + ' ' + spy.spy_name

    if spy.spy_age >=12 and spy.spy_age <=50:   # checking the requirements to be a spy
        print 'verification complete.Welcome' + ' ' + spy.spy_name + ' ' + 'with an age of' + ' ' + str(spy.spy_age) + ' ' + 'and rating of' + ' ' + str(spy.spy_rating)

        if spy.spy_rating>4.0:      # displaying msg based on spy rating
            print 'You are awesome'
        elif spy.spy_rating>=2.5 and spy.spy_rating<=4.0:
            print 'You are good.'
        else:
            print 'You can do much better.'


        display_menu = True

        while display_menu:     # displaying the list of options in spy chat app
            question = 'Which option do you want to select?\n 1.Add a status update\n 2.Add a friend\n 3.send a secret message \n 4.Read a secret message\n 5.Read chats from the user\n 6.close application'
            choice = raw_input(question)


            if len(choice)>0:
                 choice = int(choice)
                 if choice == 1:
                     spy.current_status_msg = status_upd()
                 elif choice == 2:
                     num_of_spyfriend = add_friend()
                     print 'The number of spy friends you have is ' + str(num_of_spyfriend)
                 elif choice == 3:
                     send_msg()
                 elif choice == 4:
                     read_msg()
                 elif choice == 5:
                     read_chat_history()
                 elif choice == 6:
                     print 'You choose to close application.'
                     exit()     # exiting the spy chat app

                 else:
                     display_menu = False
                     print 'You have entered wrong choice.'

    else:
        print 'Sorry.You are not eligible to be a Spy!!!'

if ask == 'Yes':    # starting chat as default spy
    start_chat(spy)
else:               # starting chat as new spy
    spy = Spy('', '', 0, 0.0)


    spy.spy_name = raw_input('Enter your name:')
    if len(spy.spy_name)>0:
        spy.spy_salutation = raw_input('What should i call you (Mr. or Ms.)?')
        spy.spy_age = raw_input("what's your age?")
        spy.spy_age = int(spy.spy_age)
        spy.spy_rating = raw_input("What's your rating?")
        spy.spy_rating = float(spy.spy_rating)
        spy.spy_online_status = True
        start_chat(spy)
    else:
        print 'You have not entered a valid name.'
        print 'Please enter a valid one'



