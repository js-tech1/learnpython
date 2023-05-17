import numpy as np
# a = np.arange(10)**3
# print(a[2:5])

# a[:6:2] = 1000

# print(a)

def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4), dtype = int)
print(b)