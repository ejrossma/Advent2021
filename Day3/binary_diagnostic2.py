def binary_diagnostic(input_file):
    file = open(input_file)

    input = []
    for x in file:
        temp = x.split('\n')
        input.append(temp[0])

    oxygen = []
    for x in input:
        oxygen.append(x)

    coTwo = []
    for x in input:
        coTwo.append(x)

    #loop through to find oxygen
    bit_sifter(oxygen, 0)
    #loop through to find co2
    bit_sifter_two(coTwo, 0)
        
def bit_sifter(values, index):
    if len(values) == 1:
        print("Found Oxygen: " + values[0])
        return
    #if reached the end
    if index == len(values[0]):
        print("reached end")
        return

    count = 0
    common = 1
    #go through each bit and find whether 1 or 0 is more common
    for x in values:
        if int(x[index]) == 1:
            count += 1
        else:
            count -= 1
    if count < 0:
        common = 0

    temp = []
    for x in values:
        if int(x[index]) == common:
            temp.append(x)
    if len(temp) == 0:
        print("Found Oxygen: " + values[-1])
        return
    else:
        bit_sifter(temp, index + 1)

def bit_sifter_two(values, index):
    if len(values) == 1:
        print("Found Co2: " + values[0])
        return
    #if reached the end
    if index == len(values[0]):
        print("reached end")
        return

    count = 0
    common = 0
    #go through each bit and find whether 1 or 0 is more common
    for x in values:
        if int(x[index]) == 1:
            count += 1
        else:
            count -= 1
    if count < 0:
        common = 1

    temp = []
    for x in values:
        if int(x[index]) == common:
            temp.append(x)
    if len(temp) == 0:
        return
    else:
        bit_sifter_two(temp, index + 1)

binary_diagnostic("input.txt")
