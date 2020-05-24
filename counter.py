from collections import Counter

c = Counter()

list = [1,2,3,4,5,6,2,5,1]

print(Counter(list)[1])
print(Counter({1:5,2:3}))

list = [1,2,3,4,5,6,2,5,1]
c = Counter(list)
print(c.most_common)