import collections

Student = collections.namedtuple('Student',['name','age','DOB'])

s = Student("Juan", 45, "19701010")

print(s.name)
print(s.age)
print(s.DOB)