class Student:
    def __init__(self,name):
        self.name = name
    def __eq__(self,other):
        return self.name == other.name
student1 = Student("minh")
student2 = Student("minh")
print(student1.__eq__(student2))