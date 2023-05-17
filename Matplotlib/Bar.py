import matplotlib.pyplot as pt
fig = pt.figure(figsize = (10, 5))
data = {'C':35,'C++':54,'Java':25,'Python':47}
keys  = list(data.keys())
values = list(data.values())
pt.bar(keys, values, color ='g',width = 0.4)
pt.show()
