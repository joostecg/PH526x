#Shallow copy refers back to original objects

x = [1,[2]]
y = copy(x)
z = deepcopy(x)
y is z