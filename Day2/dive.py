#Day 2 Advent of Code 2021
def dive(input_file):
    file = open(input_file)

    input = []
    for x in file:
        input.append(x)
        
    depth = 0
    pos = 0
    for x in input:
        temp = x.split(' ')
        if temp[0] == "forward":
            pos += int(temp[1])
        elif temp[0] == "up":
            depth -= int(temp[1])
        elif temp[0] == "down":
            depth += int(temp[1])
    print(depth * pos)

dive("input.txt")
        