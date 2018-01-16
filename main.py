def get_name():
    global spy_name, sy_nm_len, spy_salutation, sy_sa_len
    spy_name = input("Welcome to spy chat, you must tell me your spy name first: ")
    sy_nm_len = len(spy_name)

    spy_salutation = input("Should I call you Mister or Miss?: ")
    sy_sa_len = len(spy_salutation)


get_name()


spy_name = spy_salutation + " " + spy_name + " "
print(sy_nm_len + sy_sa_len)
while sy_nm_len == 0 and sy_sa_len == 0:
    print("Incorrect Values enter name and salutation again", end='\n')
    get_name()
else:
    print("Alright " + spy_name.capitalize() + " I'd like to know a little bit more about...")



