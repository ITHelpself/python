from operator import itemgetter,attrgetter
class Person:
    """a simple class"""
    @classmethod
    def __init__(self):
        self.name = "default"
        Person.count = 0
    def __str__(self):
        return self.name
    def rename(self,name):
        self.name = name
    @staticmethod
    def countPerson():
        Person.count+=1
    @staticmethod
    def getCount():
        return Person.count
# people
people = [{'name':'chandan','age':20,'salary':2000},
{'name':'chetan','age':18,'salary':5000},
{'name':'guru','age':30,'salary':3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')
people.sort(key=by_age) #in-place sorting by age
people.sort(key=by_salary) #in-place sorting by salary
# person
person = Person()
print(person.__str__())
Person.countPerson()
Person.countPerson()
Person.countPerson()
print(Person.getCount())

