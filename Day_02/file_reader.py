filename="file_reader_sourse.txt"
for line in open(filename):
    print(line)

for line in open(filename):
    line = line.rstrip()
    print(line)

for line in open(filename):
    line = line.rstrip().split(" ")
    print(line)

for line in open(filename):
    line = line.rstrip().split("\n")
    print(line)

