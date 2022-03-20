# printing the game board
"""
[
    [-,-,-],
    [-,-,-],
    [-,-,-]
]
"""
# take player input
"""
userInput -> something 1-9 to correspond to spot on board
if they enter anything else: tell them to go again
check if userInput is already taken
add it to the board
"""
# check for win or tie
"""
check if user won: checking rows, column, diagonals
"""
# switch the player
"""
toggle between users upon successful moves
"""

board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def printBoard(board):
    for row in board:
        for slot in row:
            print(f"{slot} ", end="")
        print()

printBoard(board)

def quit(userInput):
    if userInput == "q":
        print("Thanks for playing! :)")
        return True
    else:
        return False



while True:
    userInput = input("Enter a position 1 through 9, or enter \"q\" to quit: ")
    if quit(userInput):
        break