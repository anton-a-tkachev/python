# Classes and Objects

import datetime

class User:
    """A class representing a person"""
    
    def __init__(self, full_name, birthday):
        self.first_name = full_name.split(' ')[0]
        self.last_name  = full_name.split(' ')[-1]
        self.birthday = datetime.datetime.strptime(birthday,"%d/%m/%Y")

    def age(self):
        return datetime.datetime.today() - self.birthday
###############################################################################

user1 = User("Anton Tkachev","28/01/1988")
print(user1.first_name, user1.last_name, user1.birthday.strftime("%d/%m/%Y"))
print(user1.age().days//365, "years old")