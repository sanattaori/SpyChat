from spy_details import spy, Spy, friends, ChatMessage
from stegano import lsb
from datetime import datetime
import csv
STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
current_status_message = ""

new_friend = Spy(" ", " ", 0, 0.0)


def get_name():
    """ Get Spy Name """
    global spy_name, sy_nm_len, spy_salutation, sy_sa_len, spy_full_name
    spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
    sy_nm_len = len(spy_name)
    """ Get Spy Name Length """
    spy_salutation = input("Should I call you Mister or Miss?: ")
    sy_sa_len = len(spy_salutation)

    spy_full_name = spy_salutation + " " + spy_name.capitalize() + " "

    # Repeat until user enter valid name
    while sy_nm_len == 0 and sy_sa_len == 0:
        print("Incorrect Values enter name and salutation again", end='\n')
        get_name()
    else:
        print("Alright " + spy_full_name.capitalize() + " I'd like to know a little bit more about...", end='\n')


def get_age():
    """ Get Spy Age  """
    global spy_age
    try:
        spy_age = int(input("Enter your age: "))
    except Exception:
        print("Error age not valid", end='\nEnter Age Again\n')
        get_age()
    check_age()


def get_rating():
    """ Get Spy Rating  """
    global spy_rating
    try:
        spy_rating = float(input("Please enter your spy rating between 0 to 5 : "))
    except Exception:
        print("Rating not valid", end='\nPlease try Again\n')
        get_rating()


def show_error():
    global error
    error = True
    print("Sorry You are not of the proper age to enter the spy community!")


def check_age():
    # Check Spy Age
    global spy_is_online
    spy_is_online = False

    if 12 < spy_age < 50:
        print("Valid Spy, Welcome!")
        get_rating()

        if spy_rating > 4.5:
            print('Great ace!')
        # Chained Comparison
        elif 3.5 < spy_rating <= 4.5:
            print('You are one of the good ones.')
        elif 2.5 <= spy_rating <= 3.5:
            print('You can always do better')
        else:
            print('We can always use somebody to help in the office.')

        spy_is_online = True
    else:
        print("Sorry You are not of the proper age to enter the spy community!\n Enter age bw 12 to 50")
        get_age()


def add_status():
    spy.current_status_message = input("Enter status: ")
    print("status updated")
    start_chat(spy_name, spy_age, spy_rating)


def view_status():
    print("Your status is " + str(spy.current_status_message))
    start_chat(spy_name, spy_age, spy_rating)


def add_friend():

    new_friend.name = input("Please add your friend's name: ")
    new_friend.salutation = input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = input("Age?")

    new_friend.rating = input("Spy rating?")

    friends.append(new_friend)
    print('Friend Added!')

    print('You have %d friends' % len(friends))

    start_chat(spy_name, spy_age, spy_rating)


def append_to_friend(secret_text, sender):
    new_chat = {
        "message": secret_text,
        "time": datetime.now(),
        "sent_by_me": False
    }

    friends[sender]['chats'].append(new_chat)


def read_message():

    output_path = input("What is the name of the file? \n (Press enter to read default secret file)")
    # sender = select_a_friend()

    if len(output_path) == 0:
        secrettext = lsb.reveal("./secret.png")
        # new_chat = ChatMessage(secrettext, False)
        # friends[sender].chats.append(new_chat)
    else:
        try:
            secrettext = lsb.reveal(output_path)
            # new_chat = ChatMessage(secrettext, False)
            # friends[sender].chats.append(new_chat)
        except Exception:
            print('error exiting your entered output path invalid')
            exit()
    print("Your secret message is " + str(secrettext))

    start_chat(spy_name, spy_age, spy_rating)


def select_a_friend():
    item_number = 0
    for friend in friends:
        print("%d. %s" % (item_number + 1, friend.name))
        item_number = item_number + 1

    ch = input("select friend index")

    friend_choice_position = int(ch) - 1

    return friend_choice_position


def send_msg():
    ch = select_a_friend()
    text = input("What do you want to say? ")

    secret = lsb.hide("./input.png", text)
    output = input('Name of output file: \n (Press enter for default name)')
    if len(output) == 0:
        secret.save("./secret.png")
        print("Your secret message image is ready! with file name 'secret.png' ")
    else:
        try:
            secret.save(output)
            print("Your secret message image is ready! with file name " + output)
        except Exception:
            print('enter valid extension')

    # Append chat to friend
    new_chat = ChatMessage(text, True)
    friends[ch].chats.append(new_chat)

    start_chat(spy_name, spy_age, spy_rating)


def exits():
    print('Exiting, Hey don\'t forget to clear your secret image file and data')
    exit(1)


def store_friends_data():
    # Saving Friends data
    try:
        with open('data.csv', 'wb') as csv_file:
            writer = csv.writer(csv_file)
            for key, value in friends.items():
                writer.writerow([key, value])
    except Exception:
        print('error no chat data found \nYou need to chat send message first')

    start_chat(spy_name, spy_age, spy_rating)


def view_friends_data():
    # Reading Friends Data from csv
    try:
        with open('data.csv', 'rb') as csv_file:
            reader = csv.reader(csv_file)
            friends_data = dict(reader)
            print('Friends data ' + str(friends_data))
    except Exception:
        print('Error no data in csv found')

    start_chat(spy_name, spy_age, spy_rating)


def start_chat(name, age, rating):

    # Authentication Complete
    # print("Authentication Complete. Welcome %s, age: %d, rating : %.2f." % (name, age, rating))

    # Show Menu
    menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message " \
                   "\n 4. Read a secret message \n 5. View Status \n 6. Store Friends_Data \n 7. View Friends Data \n "\
                   "8. Exit \n"

    ch = input(menu_choices)

    options = {
               1: add_status,
               2: add_friend,
               3: send_msg,
               4: read_message,
               5: view_status,
               6: store_friends_data,
               7: view_friends_data,
               8: exits
              }
    options[int(ch)]()


spy_name = spy.name
spy_salutation = spy.salutation
spy_age = spy.age
spy_rating = spy.rating
spy_is_online = spy.is_online

question = "Do you want to continue as " + spy_salutation + " " + spy_name + " (Y/N)? "
existing = input(question)
print(existing)
if existing == "Y" or existing == "y":
    start_chat(spy_name, spy_age, spy_rating)
else:
    spy_name = ''
    spy_salutation = ''
    spy_age = 0
    spy_rating = 0.0
    spy_is_online = False

    get_name()

    get_age()

    # check_age()

    start_chat(spy_name, spy_age, spy_rating)
