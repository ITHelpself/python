from array import *
def appendNumber(number, numbers):
    numbers.append(number)
def printNumber(numbers):
    for number in numbers:
        print(number)
a = [1,2,4,5] + [3,4,5,6]
print(a)
list = ["one","two","three"]
for index, item in enumerate(list):
    print(index,"::",item)
x = map(lambda x: x.upper(),list)
for index, item in enumerate(x):
    print(index,"::",item)
y = [(1,2,3),(1,4,5),(3,5,6)]
my_array = array('i',[1,2,3,4,5])
print(my_array[1])
# insert
my_array.insert(4,23)
print(my_array)
# info buffer
y = my_array.buffer_info()
print(y)
# count of number
y = my_array.count(3)
print(y)
# to string
y = my_array.tostring()
print(y)