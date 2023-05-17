#for even lists

v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8]

v3 = v1 + v2
print(v3)

sums = map(lambda x,y: x+y, v1, v2)
print(sums)
print(list(sums))

""""""""""""""""""""""""""""""""""""""""
"""""""""""""""""""""""""""""""""""""""""

#for uneven list

v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8,10,64]

v3 = v1 + v2
print(v3)

sums = map(lambda x,y: x+y, v1, v2)
print(sums)
print(list(sums))

""""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""""

#for counting empty list and replace it with none(0)

v1 = [1, 3, 5, 9]
v2 = [2, 6, 4, 8, 10]

print(map(lambda x,y: (0 if x is None else x) + (0 if y is None else y), v1, v2))

""""""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""""""

#for mixed dictionaries

v1 = ['foo', 'bar', 'baz']
v2 = 'abc'

result = map(lambda x,y: x+y, v1, v2)
print(result)
print( list(result) )
# <map object at 0x7fc5e9ff4e80>
['fooa', 'barb', 'bazc']


""""""""""""""""""""""""""""""""""""""
""""""""""""""""""""""""""""""""""""""

#to fetch specific values from dictionaries

people = [
{
'name': 'Foo',
'phone': '123',
},
{
'name': 'Bar',
'phone': '456',
},
{
'name': 'SnowWhite',
'phone': '7-dwarfs',
}
]

names = map(lambda d: d['name'], people)

print(names)
print(list(names))