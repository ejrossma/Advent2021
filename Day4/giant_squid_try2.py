def giant_squid_try2(input_file):
    file = open(input_file)

    #extract numbers to be read for bingo
    temp = file.readline().strip()
    bingoNumbers = temp.split(',')
    #print(numbers)

    #container for all the boards
    boardContainer = []

    #build the bingo boards
    while True:
        #space between boards
        intake = file.readline()
        if intake:
            #start building board
            board = [[(0, False) for i in range(5)] for j in range(5)]
            for i in range(5):
                temp = file.readline().strip()
                numbersInRow = temp.split()
                for j in range(5):
                    board[i][j] = (numbersInRow[j], False)
            boardContainer.append(board)
        else:
            break

    findWinner(bingoNumbers, boardContainer)



def findWinner(bingoNumbers, boardContainer):
    for num in bingoNumbers:
        for board in boardContainer:
            for i in range(5):
                for j in range(5):
                    if board[i][j][0] == num:
                        board[i][j] = (board[i][j][0], True)
                        if checkForHorizontalWin(board, i):
                            print("Winning number: ", num)
                            for k in range(5):
                                print(board[k])
                            calculateWinningValue(board, num)
                            return
                        elif checkForVerticalWin(board, j):
                            print("Winning number: ", num)
                            for k in range(5):
                                print(board[k])
                            calculateWinningValue(board, num)
                            return


def checkForHorizontalWin(board, i):
    winner = True
    for j in range(5):
        winner = board[i][j][1]
        if winner == False:
            break
    return winner

def checkForVerticalWin(board, j):
    winner = True
    for i in range(5):
        winner = board[i][j][1]
        if winner == False:
            break
    return winner

def calculateWinningValue(board, numberJustCalled):
    winningNumber = 0
    for i in range(5):
        for j in range(5):
            if board[i][j][1] == False:
                winningNumber += int(board[i][j][0])
    winningNumber *= int(numberJustCalled)
    print(winningNumber)




giant_squid_try2("input.txt");