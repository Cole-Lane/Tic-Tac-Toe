# Cole Lane

# imports
import io
import PySimpleGUI as gui

from PIL import Image

blank_image = "assets/blank.png"
x_image = "assets/X.png"
y_image = "assets/O.png"


def boardFull(board):
    """check to see if the squares on the board are filled"""
    boardFull = True

    for i in board:
        if "" in i:
            return False

    return boardFull


def checkBoardForWinner(board, playerSymbol, buttons):
    """check the board to see if there are any winning plays and then mark them on the gui
    winning plays would be horizontal, vertical, or diagonal"""
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
            highlightWin([buttons[x][0], buttons[x][1], buttons[x][2]])
            return win

    # check columns
    for x in range(boardSize):
        win = True
        for y in range(boardSize):
            if board[y][x] != playerSymbol:
                win = False
                break
        if win:
            highlightWin([buttons[0][x], buttons[1][x], buttons[2][x]])
            return win

    # check forward diagonal
    win = True
    for x in range(boardSize):
        if board[x][x] != playerSymbol:
            win = False
            break
    if win:
        highlightWin(
            [buttons[x - 2][x - 2], buttons[x - 1][x - 1], buttons[x][x]])
        return win

    # check backward diagonal
    win = True
    for x in range(boardSize):
        if board[x][boardSize - 1 - x] != playerSymbol:
            win = False
            break

    if win:
        highlightWin(
            [
                buttons[x - 2][boardSize - 1],
                buttons[x - 1][boardSize - x],
                buttons[x][boardSize - 1 - x],
            ]
        )
        return win

    if boardFull(board):
        return False


def clearBoard(board):
    """clears the board for a new game"""
    boardSize = len(board)
    for column in range(boardSize):
        for row in range(boardSize):
            board[column][row] = ''


def playGame():
    """main 'function' that creates the main window and allows for user interaction"""
    board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]

    layout = [
        [
            gui.Button(
                size=(10, 6),
                key=(row, col),
                button_color=("white", "white"),
                image_filename=blank_image,
            )
            for col in range(3)
        ]
        for row in range(3)
    ]

    window = gui.Window(title="Tic-Tac-Toe", layout=layout, margins=(100, 100))

    turn = 0
    while True:
        event, values = window.read()
        if event == "Exit" or event == gui.WIN_CLOSED:
            break
        if isinstance(event, tuple):
            btn_clicked = window[event]
            turn = updateGame(btn_clicked, turn, board, layout)
            if turn == -1:
                break
    window.close()


def updateGame(button, turn, board, layout):
    """
    Update the game when one of the buttons is clicked
    """
    player1Symbol = "X"
    player2Symbol = "O"
    playAgain = True

    if turn % 2 == 0:
        filename = x_image
        symbolToUse = player1Symbol
    else:
        filename = y_image
        symbolToUse = player2Symbol

    bio = io.BytesIO()
    image = Image.open(filename)
    image.save(bio, format="PNG")

    if not button.metadata:
        button.update(image_data=bio.getvalue())
        button.metadata = symbolToUse
        board[button.key[0]][button.key[1]] = symbolToUse
        if checkBoardForWinner(board, symbolToUse, layout):
            playAgain = gameEnd(symbolToUse)
            if playAgain is False:
                # Quit Game
                return -1
            else:
                gameReset(layout, board)
                return 0

        elif checkBoardForWinner(board, symbolToUse, layout) != None:
            playAgain = gameEnd(None)
            if playAgain is False:
                # Quit Game
                return -1
            else:
                gameReset(layout, board)
                return 0

        return turn + 1


def highlightWin(buttons):
    """
    Highlight the winning buttons with a different background color
    """
    for button in buttons:
        button.update(button_color=("green", "green"))


def gameEnd(player):
    """
    Ask players if they want to play again or quit
    """
    if player is None:
        message = "Tied Game!"
    else:
        message = f"{player} won!"
    layout = [
        [gui.Text(f"{message} Do you want to play again or quit?")],
        [gui.Button("Restart"), gui.Button("Quit")],
    ]
    event, values = gui.Window(
        "Play Again?", layout, modal=True).read(close=True)
    return True if event == "Restart" else False


def gameReset(buttons, board):
    """
    Reset the game to play again
    """
    bio = io.BytesIO()
    image = Image.open(blank_image)
    image.save(bio, format="PNG")
    for row in buttons:
        for button in row:
            button.update(
                image_data=bio.getvalue(), button_color=["white", "white"]
            )
            button.metadata = None
    clearBoard(board)


# main
playGame()
