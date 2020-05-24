import collections

d1 = collections.OrderedDict()

d1['A'] = 1
d1['B'] = "Hola"
d1['C'] = 2.3
d1['D'] = True

for k,v in d1.items():
    print(k,v)
