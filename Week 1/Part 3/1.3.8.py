def intersect(s1, s2):
    res = []
    for x in s1:
        if x in s2:
            res.append(x)
    return res

intersect([1,2,3,4,5],[3,4,5,6,7])


import random
random.choice([1,2,3,4])
random.choice("abcdef")

def password(length):
    pw = str()
    characters = "abcdefghijklmnopqrstuvwxyz" + "0123456789"
    for i in range(length):
        pw = pw + random.choice(characters)
    return pw

password(10)

def is_vowel(letter):
   if letter in "aeiouy":
     return(True)
   else:
     return(False)

is_vowel("a")


def factorial(n):
   if n == 0:
     return 1
   else:
     N = 1
     for i in range(1, n+1):
       N = N * i
     return(N)

factorial(3)