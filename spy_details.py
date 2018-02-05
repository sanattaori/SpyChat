from datetime import datetime


# Spy details class
class Spy:
    # Constructor
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


# Chat Message for sending and receiving record
class ChatMessage:
    # Constructor
    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


# spy object with default bond spy
spy = Spy('Bond', 'Mr.', 24, 8)

# spy default friends
friend_one = Spy('Ravi', 'Mr.', 19, 6)
friend_two = Spy('Rohit', 'Mr.', 20, 5.39)
friend_three = Spy('Rani', 'Mr.', 21, 5.95)

friends = [friend_one, friend_two, friend_three]
