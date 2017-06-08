L = [1,2,3]
M = [1,2,3]

L == M

L is M # compare the object itself

id(L)
id(M)

id(L) == id(M)

L = [1,2,3]
M = L # just a different name
M = list(L)

M is L
M == L

M = L[:]