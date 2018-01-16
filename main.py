spy_rating = 0.0
spy_is_online = False


def get_name():
    """ Get Spy Name """
    global spy_name, sy_nm_len, spy_salutation, sy_sa_len
    spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
    sy_nm_len = len(spy_name)
    """ Get Spy Name Length """
    spy_salutation = input("Should I call you Mister or Miss?: ")
    sy_sa_len = len(spy_salutation)


def get_age():
    """ Get Spy Age  """
    global spy_age
    spy_age = int(input("Enter your age: "))


get_name()

spy_name = spy_salutation + " " + spy_name + " "

# Repeat until user enter valid name
while sy_nm_len == 0 and sy_sa_len == 0:
    print("Incorrect Values enter name and salutation again", end='\n')
    get_name()
else:
    print("Alright " + spy_name.capitalize() + " I'd like to know a little bit more about...", end='\n')

get_age()

# Check Spy Age
if 12 < spy_age < 50:
    print("Valid Spy, Welcome!")

    spy_rating = float(input("Please enter your spy rating between 0 to 5 : "))

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

    # Authentication Complete
    print("Authentication Complete.Welcome %s,age: %d,rating : %.2f." % (spy_name, spy_age, spy_rating))

else:
    print("Sorry You are not of the proper age to enter the spy community!")
