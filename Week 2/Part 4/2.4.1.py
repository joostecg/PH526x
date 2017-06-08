import random

random.choice(["H","T"])

random.choice([0,1])

random.choice([1,2,3,4,5,6])

random.choice(range(1,7))

random.choice([range(1,7)]) #Python will only return on object

#6, 8, 10 face dice

random.choice(random.choice([range(1,7),range(1,9),range(1,11)]))


random.choice(list([1,2,3,4]))


sum(random.sample(range(10),10))
sum(random.choice(range(10),10))
random.sample_sum(range(10), 10)
sum(random.choice(range(10)) for i in range(10))