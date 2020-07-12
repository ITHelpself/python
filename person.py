from operator import itemgetter,attrgetter
class Person:
    """a simple class"""
    def __init__(self,name):
        self.name = name
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
    def from_full_name(self,name):
        pass #TODO: from full file
class SpecialPerson(Person):
    def __init__(self, name, rewardMark):
        super(SpecialPerson, self).__init__(name)
        self.rewardMark = rewardMark
    def __str__(self):
        return str(self.name) + " " + str(self.rewardMark)
# people
people = [{'name':'chandan','age':20,'salary':2000},
{'name':'chetan','age':18,'salary':5000},
{'name':'guru','age':30,'salary':3000}]
by_age = itemgetter('age')
by_salary = itemgetter('salary')
people.sort(key=by_age) #in-place sorting by age
people.sort(key=by_salary) #in-place sorting by salary
# person
person = Person("Minh")
print(person.__str__())
Person.countPerson()
Person.countPerson()
Person.countPerson()
print(Person.getCount())
specialPerson = SpecialPerson("hoa",43)
print(specialPerson.__str__())
# thêm getName vào trong Person class
def getName(self):
    return self.name
Person.getName = getName
print(person.getName())