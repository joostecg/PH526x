numbers = range(10)
squares = []
for number in numbers:
    square = number**2
    squares.append(square)
squares

squares2 = [number**2 for number in numbers]    #very fast and in one line
squares2

sum([i**2 for i in range(3)])

sum([i for i in range(1,10,2)])
