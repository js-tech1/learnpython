from collections import OrderedDict

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d)  #prints as it is

planned_order = ('b', 'c', 'd', 'a')
e = OrderedDict(sorted(d.items(), key=lambda x: planned_order.index(x[0])))
 #prints as planned but saperates the keys from values
print(e)


print('-----')
# Create index to value mapping dictionary from a list of values
planned_order = ('b', 'c', 'd', 'a')
plan = dict(zip(planned_order, range(len(planned_order))))
#prints as planned and zips the values and returns index values
print(plan) 

f = OrderedDict(sorted(d.items(), key=lambda x: plan[x[0]]))
print(f)