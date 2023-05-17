from functools import reduce

print( reduce(lambda x,y: x+y, [], 0) )
print( reduce(lambda x,y: x+y, [1, 2], 0) )

print( reduce(lambda x,y: x*y, [1, 2], 0) )
print( reduce(lambda x,y: x*y, [2, 3], 1) )
print( reduce(lambda x,y: x*y, [], 0) ) 