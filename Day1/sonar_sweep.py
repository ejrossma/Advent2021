#Day 1 of Advent of Code
def sonar_sweep(input_file):
    file = open(input_file, "r")
    
    input = []
    for x in file:
        input.append(int(x))
    count = 0
    prev = 10000
    for x in input:
        if x > prev: #y is the previous value
            count += 1
        prev = x
    print(count)

sonar_sweep("input.txt")