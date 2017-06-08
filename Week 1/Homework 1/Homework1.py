#1a
import string
alphabet = string.ascii_letters
alphabet

#1b
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
#write your code here!
for letter in sentence:
    if letter != " ":
        count_letters[letter] = sentence.count(letter)

count_letters

#1c
sentence = 'Jim quickly realized that the beautiful gowns are expensive'

#write your code here!

def counter(sentence_str):
    count_letters_dic = {}
    for letter in sentence_str:
        if letter != " ":
            count_letters_dic[letter] = sentence.count(letter)
    return count_letters_dic

counter(sentence)

#1d
address_count = counter(address)
print(address_count)

#1e
max(count_letters.values())

list = {'george':16,'amber':19}
#search_age = raw_input("Provide age")
search_age = 16
for age in list.values():
    if age == search_age:
        name = list[age]
        name

#final answer
maxvalue = 0
for letter, value in address_count.items():
    if value > maxvalue:
        maxvalue = value
        most_frequent_letter = letter

print(most_frequent_letter)

#2a
# write your code here!
import math
print(math.pi/4)

#2b
import random

random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.

def rand():
   # define `rand` here!
    randvalue = random.uniform(-1,1)
    return randvalue

rand()

#2c
import math


def distance(x, y):

# define your function here!
    z = math.sqrt((y[0]-x[0])**2 + (y[1]-x[1])**2)
    return z

x = (0,0)
y = (1,1)

print(distance(x,y))

#2d
import random, math

random.seed(1)


def in_circle(x, origin=[0] * 2):

# Define your function here!
    x_distance = distance(x,origin)
    if x_distance < 1:
        in_circle_bool = True
    else:
        in_circle_bool = False

    return in_circle_bool

print(in_circle((1,1)))


#2e
R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    # Enter your code here! #
    check = in_circle(point)
    inside.append(check)

# Enter your code here! #
true_count = inside.count(True)
proportion = true_count / R
print(proportion)

#2f
# write your code here!


proportion = inside.count(True) / R

difference = math.pi/4 - proportion
print(difference)


#3a

import random

random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    mean_list = []
    print(x)
    for i in range(n):
        endrange = i+width
        print(str(i)+ ":" + str(endrange))
        print(sum(x[i:endrange]))
        print(width)
        mean = sum(x[i:endrange])/width
        print(mean)
        mean_list.append(mean)
    return mean_list

x=[0,10,5,3,1,5]
print(moving_window_average(x, 1))


#submitted code:
import random

random.seed(1)

def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    mean_list = []
    for i in range(n):
        endrange = i+width
        mean = sum(x[i:endrange])/width
        mean_list.append(mean)
    return mean_list

x=[0,10,5,3,1,5]
#print(moving_window_average(x, 1))


#3b
"""import random

random.seed(1)  # This line fixes the value called by your function,
# and is used for answer-checking.

# write your code here!
R = 1000
x = []
for i in range(R):
    rvalue = random.random()
    x.append(rvalue)

tempY=[]
for j in range(1,10):
    moving_average = (moving_window_average(x,j))
    tempY.append([x, moving_average])
Y = tempY

print(Y)"""

import random

random.seed(1)  # This line fixes the value called by your function,
# and is used for answer-checking.

# write your code here!
R = range(1000)
x = [random.random() for xvalue in R]
n = range(1,10)
#Y = [moving_window_average(x,n_neighbours) for n_neighbours in n]

Y = []
Y.append(x)
for n_neighbours in n:
    moving_value = moving_window_average(x, n_neighbours)
    Y.append(moving_value)
Y


#3c

print(len(Y))
length = range(len(Y))
ranges = [max(Y[i]) - min(Y[i]) for i in length]
#print(max_list)
#min_list = [min(Y[i]) for i in length]
#range = max_list - min_list
print(ranges)