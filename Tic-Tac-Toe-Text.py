# Cole Lane

def displayBoard(board):
    toPrint = ""
    for i in range(0, 3):
        for q in range(0, 3):
            if board[i][q] == "":
                toPrint = toPrint + "-" + " "
            elif board[i][q] == "X" or board[i][q] == "O":
                toPrint = toPrint + board[i][q] + " "
            if q == 2:
                print(toPrint)
                toPrint = ""
    print()


def getMove(board, locations, player):
    correctMove = False
    while correctMove == False:
        playaInput = input(player + ", enter your move (1-9): ")
        for x in range(0, len(locations)):
            for y in range(0, len(locations)):
                if locations[x][y] == playaInput:
                    # see if the position is valid
                    if board[x][y] != "":
                        print()
                        print("Spot " + playaInput +
                              " is already taken, try again.")
                    else:
                        print()
                        return playaInput


def boardFull(board):
    boardFull = True

    for i in board:
        if "" in i:
            return False

    print("The game is a tie!")
    return boardFull


def checkBoard(board, playerSymbol):
    """ check the board to see if there are any winning plays
     winning plays would be horizontal, vertical, or diagonal """
    boardSize = len(board)
    win = None

    # check rows
    for x in range(boardSize):
        win = True
        for y in range(boardSize):
            if board[x][y] != playerSymbol:
                win = False
                break
        if win:
            return win

    # check columns
    for x in range(boardSize):
        win = True
        for y in range(boardSize):
            if board[y][x] != playerSymbol:
                win = False
                break
        if win:
            return win

    # check forward diagonal
    win = True
    for x in range(boardSize):
        if board[x][x] != playerSymbol:
            win = False
            break
    if win:
        return win

    # check backward diagonal
    win = True
    for x in range(boardSize):
        if board[x][boardSize - 1 - x] != playerSymbol:
            win = False
            break
    if win:
        return win


def playGame():
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]

    locations = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
    ]

    print("This program will allow two players to play the game of tic-tac-toe. \n")

    print("Player 1 has 'X' and player 2 has 'O'. \n")

    p1 = input("Enter the name of Player 1 : ")
    print()

    p2 = input("Enter the name of Player 2 : ")
    print()

    player1Symbol = "X"
    player2Symbol = "O"
    gameWon = False
    turn = 0

    print(p1, "you start. You are playing", player1Symbol + "\n")

    print(p2, "will follow. You are playing", player2Symbol + "\n")

    displayBoard(board)

    while gameWon == False:
        if turn % 2 == 0:
            move = getMove(board, locations, p1)

            for x in range(0, len(locations)):
                for y in range(0, len(locations)):
                    if locations[x][y] == move:
                        board[x][y] = player1Symbol

        if checkBoard(board, player1Symbol):
            gameWon = True
            print(p1 + " won! \n")
            displayBoard(board)

        if turn % 2 == 1:
            move = getMove(board, locations, p2)
            for x in range(0, len(locations)):
                for y in range(0, len(locations)):
                    if locations[x][y] == move:
                        board[x][y] = player2Symbol

        if checkBoard(board, player2Symbol):
            gameWon = True
            print(p2 + " won! \n")
            displayBoard(board)

        if gameWon == False:
            displayBoard(board)
        turn = turn + 1

        if boardFull(board) == True:
            gameWon = True


# main

playGame()
