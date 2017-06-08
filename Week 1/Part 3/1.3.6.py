filename = "input.txt"
for line in open(filename):
    print(line)

for line in open(filename):
    line = line.rstrip()
    print(line)

for line in open(filename):
    line = line.rstrip().split(" ")
    print(line)

F = open("output.txt", "w")
F.write("Python\n")
F.close()

F = open("course.txt", "w")
F.write("Hello\nWorld")
F.close()
lines = []
for line in open("course.txt"):
    lines.append(line.strip())
print(lines)