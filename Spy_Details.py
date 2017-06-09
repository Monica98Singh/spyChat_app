'''spy={
'spy_name':'George Smiley',
'spy_salutation':'Mr.',
'spy_age':25,
'spy_rating':3.6,
'spy_online_status':True
}'''
from datetime import datetime

class Spy:
    def __init__(self, spy_name, spy_salutation, spy_age, spy_rating):
        self.spy_name = spy_name
        self.spy_salutation = spy_salutation
        self.spy_age = spy_age
        self.spy_rating = spy_rating
        self.spy_online_status = True
        self.chats = []
        self.current_status_msg = None


class chatMessage:
    def __init__(self, msg, sent_by_me ):
        self.msg = msg
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('George Smiley', 'Mr.', 25, 3.6)


fri_one = Spy('James bond', 'Mr.', 30, 4.15)
fri_two = Spy('Justine', 'Ms.', 22, 4.8)
fri_three = Spy('Agatha', 'Ms.', 35, 3.5)
fri_four = Spy('Felix', 'Mr.', 50, 2.5)


friends = [fri_one, fri_two, fri_three, fri_four]


dic_special_words = {
    'SOS': 'Save our Soul',
    'D.U.C.K': 'Department of unknown and covert knowledge',
    'N.P': 'Nothing in particular',
    'DWSP': 'Dealing with secret project',
    'WWAA': 'Working with American Agents'
    }








