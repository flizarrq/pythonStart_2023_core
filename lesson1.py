'''
qwe
qwe
qwe
'''

"""
qwe
qwe
qwe
"""

print('hello world!')

print(1, 2, 3, sep='-', end=' finish\n')

i = 3
f = 3.1
b = True
s = 'Text'
n = None

print(type(n))

int()
str()
float()
bool()

print(i is n)
print(i is not n)

print(isinstance('str', str))  # проверяет тип данный -> bool

print((n in [1, 2, 3, 4]))  # проверяет есть ли обьект в массиве -> bool\

res = 'yes' if f == 3.1 else 'no'
print(res)

l = [1, 2, 3, 4, 5]

print(len(l))  # length

l.append(6)  # add to list

del l[-1]  # delete

l2 = l
l3 = l.copy()

l.insert(2, 77)  # 1 в какой индекс, 2 что вставать

l.remove(77)  # какой елемент удалить

pop = l.pop(0)  # удалить по индексу

l.index(5, 0, 10)  # find index

l.reverse()  # reverse

l.sort(reverse=True)  # sort

l.count(2)  # count

l.clear()  # clear

print(l[::2])  # срезы

s = 'read'

print(list(s))  # make a list

tuple1 = (1, 2, 3, 4)

tuple1.count(1)
tuple1.index(1)

user = {
    'name': 'bob',
    'robert': 12
}

# print(d['name'])
# print(d.get('name1', False))
#
# del d['name']
# d.clear()
#
# print(d.items())
#
# d.keys()
# d.values()
#
# d.pop('name', None)

user.setdefault('bomber', 24)

user.update({'street': 'bomber'})
user |= {'user': 14}

user = dict(name='max', age=18)

print(user)

# SET
s = [1, 2, 3, 4, 5, 5, 5, 5, 12, 1, 2, 1, 12, 3]

s = set(s)

s = {1, 2, 3, 3, 3, 2, 2, 2, 1}

s.add(22)

name = 'kirill'
weight = 50

string = 'my name is {name} and my weight is {weight}'.format(name=name, weight=weight)
print(string)

string.find('name')

print(['   astral '.strip()])
print(['   astral  sf sfs dfs '.split()])

print(['   astral  sf sfs dfs '.partition('sf')])

