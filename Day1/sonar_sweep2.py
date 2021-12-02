#Day1 of Advent of Code problem 2
def sonar_sweep2(input_file):
    file = open(input_file)

    input = []
    for x in file:
        input.append(int(x))

    index = 0
    count = 0
    for num in input:
        if index < len(input) - 3:
            temp = num + input[index + 1] + input[index + 2]
            temp2 = input[index + 1] + input[index + 2] + input[index + 3]
            if temp2 > temp:
                count += 1
        index += 1
    print(count)

sonar_sweep2("input.txt")
            

    
    