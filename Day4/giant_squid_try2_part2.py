def giant_squid_try2_part2(input_file):
    file = open(input_file)

    #extract numbers to be read for bingo
    temp = file.readline().strip()
    bingoNumbers = temp.split(',')

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
                            lastBoard = True
                            for b in boardContainer:
                                if b == board:
                                    continue
                                lastBoard = hasBoardWon(b)
                                if lastBoard == False:
                                    break
                            if lastBoard:
                                calculateWinningValue(board, num)
                                return
                        elif checkForVerticalWin(board, j):
                            lastBoard = True
                            for b in boardContainer:
                                if b == board:
                                    continue
                                lastBoard = hasBoardWon(b)
                                if lastBoard == False:
                                    break
                            if lastBoard:
                                calculateWinningValue(board, num)
                                return

def hasBoardWon(board):
    for i in range(5):
        winner = checkForHorizontalWin(board, i)
        if winner:
            return True
    for j in range(5):
        winner = checkForVerticalWin(board, j)
        if winner:
            return True
    return False

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




giant_squid_try2_part2("input.txt");