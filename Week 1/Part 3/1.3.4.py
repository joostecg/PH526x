for x in range(10):
    print(x)

names = ['Jim', 'Tom','Nick',  'Pam', 'Sam','Tim']

for name in names:      #python way to cycle through list
    print(name)

for i in range(len(names)):     # not very Python way to do it
    print(names[i])

age = {"Tim":29, "Jim":31, "Pam":27, "Sam":35, "Tim":31, "Tom":50}
age.keys()

for name in age.keys():
    print(name, age[name])

for name in age:
    print(name, age[name])

for name in sorted(age.keys()):
    print(name, age[name])

for name in sorted(age.keys(), reverse = True):
    print(name, age[name])

#for loop - you do know how many times you will run the code
#while loop - do not know how many times you will do the loop

bears = {"Grizzly":"angry", "Brown":"friendly", "Polar":"friendly"}
for bear in bears:
    if bears[bear] == "friendly":
        print("Hello, "+bear+" bear!")
    else:
        print("odd")


n = 10
is_prime = True
for i in range(2,n):
    if n%i == 0:
        is_prime = False
print(is_prime)

not any([n%i==0 for i in range(2,n)])

n=100
number_of_times = 0
while n >= 1:
    n /= 2
    number_of_times += 1
print(number_of_times)