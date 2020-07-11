from operator import itemgetter,attrgetter
class Person:
    """a simple class"""
    def __init__(self):
        self.name = "default"
    def __str__(self):
        return self.name
    def rename(self,name):
        self.name = name
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
