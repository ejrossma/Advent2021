#Day 4 of Advent of Code 2021
def giant_squid(input_file):
    file = open(input_file)

    #first line is numbers to be drawn
    temp = file.readline().strip()
    numbers = temp.split(',')
    print(numbers)
    
    boards = []
    #5x5 boards are given followed by a space
    while True:
        #space
        intake = file.readline()
        if intake:
            #lines 1 to 5
            board = [[0 for i in range(5)] for j in range(5)]
            for i in range(5):
                line = file.readline().strip()
                column = 0
                temp = line.split()
                for num in temp:
                    board[i][column] = (num, False)
                    column += 1
            boards.append(board)
        else:
            break

        win(boards)

        # for num in numbers:
        #     print("Loop")
            #go through each board
                #go through each value on board
                    #if num == val[0]
                        #val[1] == True
                        #if win()
                            #break

def win(boards):
    #use this to reference vertically (I THINK THIS ONLY CHECKS FIRST VALUE)
    test = True
    for board in boards:
        for val in board:
            print(val[0]) #the first vertical column
            if val[0][1] == False:
                test = False
        print("End of Column")
        if test == True:
            print("Winner")
        
        #use this to check if correct horizontally (I THINK THIS ONLY CHECKS FIRST VALUE)
        # for val in board:
        #     test = True
        #     for num in val: #first horizontal row
        #         #print(num)
        #         test = True
        #         if num[0][1] == False:
        #             test = False
        #     if test == True:
        #         print("Winner")

giant_squid("input.txt")