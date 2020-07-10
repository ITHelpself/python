from collections import Counter
first_list = [1,6,8,4,5,5]
second_list = [6,7,9]
a = set(first_list)
b = set(second_list)
print("a = ", a)
print("b = ", b)
# inter section
c = a.intersection(b)
print("intersection = ", c)
# union
c = a.union(b)
print("union = ",c)
# difference
c = a.difference(b)
print("difference = ",c)
# super set check
c = a.issuperset(b)
print("a is superset of b: ", c)
# disjoin check
c = a.isdisjoint(b)
print("a is disjoint of b: ",c)
# symmetric difference
c = a.symmetric_difference(b)
print("symmetric difference of a,b:",c) 
# subset
c = a.issubset(b)
print("a is subset of b:",c)
# checking a is exist element = 2
c = 2 in a
print("2 in a: ",c)
# checking a is don't exist element = 2
c = 2 not in a
print("2 not in a: ", c)
# add element to set
a.add(3)
print("after add 3 to a: ", a)
# remove element = 3 from set
a.remove(3)
print("after remove 3 from a:", a)
# update
a.update(b)
print("after update a by b: ",a)
# convert set to list
list = list(a)
print("convert a to list:",list)
# set of sets
c = {frozenset({1,2}),frozenset({2,3})}
print("fronzen list: ",c)
# length
print("length of a:",len(a))
# counter element in list
counter = Counter(['a','b','a','c'])
print("counter: ", counter)
print("count of 'a':",counter['a'])