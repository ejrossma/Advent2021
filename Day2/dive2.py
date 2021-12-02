#Day 2 Advent of Code 2021
def dive2(input_file):
    file = open(input_file)

    input = []
    for x in file:
        input.append(x)
        
    depth = 0
    pos = 0
    aim = 0
    for x in input:
        temp = x.split(' ')
        if temp[0] == "forward":
            pos += int(temp[1])
            depth += aim * int(temp[1])
        elif temp[0] == "up":
            aim -= int(temp[1])
        elif temp[0] == "down":
            aim += int(temp[1])
    print(depth * pos)

dive2("input.txt")