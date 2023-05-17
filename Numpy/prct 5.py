import numpy as np

# a = np.array([2, 3, 4, 5])
# b = np.array([8, 5, 4])
# c = np.array([5, 4, 6, 8, 3])
# ax, bx, cx = np.ix_(a, b, c)
# print(ax)

a = np.arange(100)
b = a.reshape((5,-1,4))
#print(b.shape)

print(b)