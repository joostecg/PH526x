def add(a,b):
    mysum = a + b   #names local to function
    return mysum

add(12,15)

def add_subtract(a,b):
    mysum = a + b
    mydiff = a - b
    return (mysum,mydiff)

add_subtract(20,15)

newadd = add

def modify(mylist):
    mylist[0] *= 10

L = [1,3,5,7,9]
modify(L)