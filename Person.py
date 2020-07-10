from datetime import datetime
class Person:
    def __init__(self,name,birthday,height):
        self.name = name
        self.birthday = birthday
        self.height = height
    def __repr__(self):
        return self.name
list = [Person("John Cena","21/4/2013",134),Person("minh Anh","12/4/2013",114)]
list.sort(key = lambda item: item.height)
print(list)
print("jell")