# Tuple and set datatype
a = (1,2,3,4,5,6)
print(a)
print(type(a))

# set
b = {1,2,3}
print(b)
print(type(b))

c = {1,2,3,3}
print(c)

d = {1,2,3,4}
d.add(8)
print(d)

d = {1,2,3,4}
d.remove(3)
print(d)

e = {1,2,3}
f = {4,5,6}
g = e.union(f)
print(g)

h = {1,2,3}
i = {4,2,6}
j = h.intersection(i)
print(j)