from operator import itemgetter, attrgetter
animals = [{'name':'cat', 'weight':34},{'name':'dog', 'weight':44},{'name':'chicken', 'weight':13},{'name':'chip', 'weight':4}]
animals.sort(key = lambda item:item['weight'])
print(animals)