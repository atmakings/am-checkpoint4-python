from decimal import Decimal
import math

list1 = ['item1', 'item2', 'item3']
tuple1 = ('element1', 'element2', 'element3')
float1 = 55.55
integer1 = 7
deci1 = Decimal(44.44)
dictionary1 = {'subject1': 'math', 'subject2': 'science'}
print(list1, tuple1, float1, integer1, deci1, dictionary1)

print(round(float1))

print(math.sqrt(float1))

dictionary_items = dictionary1.items()
print(list(dictionary_items)[0][1])

print(tuple1[1:2])

list1.append('item4')
print(list1)

list1[0] = 'item5'
print(list1)

list1.sort()
print(list1)

tuple1 += ('element4',)
print(tuple1)

my_list = ['mars', 'earth', 'venus', 'pluto', 'saturn']
my_list.sort(reverse=True)
print(my_list)