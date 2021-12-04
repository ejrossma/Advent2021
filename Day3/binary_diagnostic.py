#Day 2 of Advent of Code 2021
def binary_diagnostic(input_file):
    file = open(input_file)

    input = []
    for x in file:
        input.append(x)

    #track values for each column

    output = ""
    for index in range(0, len(input[0]) - 1):
        count = 0
        for x in input:
            if (x[index] != '\n'):
                if int(x[index]) == 0:
                    count -= 1
                elif int(x[index]) == 1:
                    count += 1
        if count < 0:
            output += '0'
        else:
            output += '1'  

    print("Gamma Rate: " + output)
    output2 = ""
    for x in output:
        if int(x) == 0:
            output2 += '1'
        else:
            output2 += '0'
    print("Epsilon Rate: " + output2)

binary_diagnostic("input.txt")

    