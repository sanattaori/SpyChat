from spy_details import spy_name, spy_salutation, spy_rating, spy_age, spy_is_online

STATUS_MESSAGES = ['My name is Bond, James Bond', 'Shaken, not stirred.', 'Keeping the British end up, Sir']
current_status_message = ""
friends = []
new_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0
    }


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
    global status_msg
    status_msg = input("Enter status: ")
    print("status updated")
    start_chat(spy_name, spy_age, spy_rating)


def view_status():
    if len(spy_salutation) > 0:
        print("Your status is " + status_msg)
        start_chat(spy_name, spy_age, spy_rating)
    else:
        print("No status updated please add new status")
        add_status()


def add_friend():

    new_friend['name'] = input("Please add your friend's name: ")
    new_friend['salutation'] = input("Are they Mr. or Ms.?: ")

    new_friend['name'] = new_friend['salutation'] + " " + new_friend['name']

    new_friend['age'] = input("Age?")

    new_friend['rating'] = input("Spy rating?")

    friends.append(new_friend)
    print('Friend Added!')

    print('You have %d friends' % len(friends))

    start_chat(spy_name, spy_age, spy_rating)


def send_msg():
    item_number = 0
    for friend in friends:
        print("%d %s"% (item_number + 1, friend['name']))
        item_number = item_number + 1
    print("select freind")


def start_chat(name, age, rating):

    # Authentication Complete
    # print("Authentication Complete. Welcome %s, age: %d, rating : %.2f." % (name, age, rating))

    # Show Menu
    menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message " \
                   "\n 4. Read a secret message \n 5. Read Chats from a user \n 6. View Status \n "

    ch = input(menu_choices)

    options = {1: add_status,
               2: add_friend,
               3: send_msg,
               6: view_status,

               }
    options[int(ch)]()


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
