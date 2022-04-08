import pygame, sys
import numpy as np

pygame.init()

# constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BRD_ROW = 3
BRD_COL = 3
SQUARE_SIZE = WIDTH//BRD_COL
CIRCLE_RADIUS = SQUARE_SIZE//3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE//4

# rgb colours
BG_COLOUR = (166, 211, 160) # light green
BLUE = (36, 123, 160) # cross colour
PINK = (238, 99, 82) # circle colour
LINE = (198, 222, 166)
WIN_LINE = (0,0,0) # black

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE')
screen.fill(BG_COLOUR)

# board
board = np.zeros((BRD_ROW,BRD_COL))

def drawLines():
    # 1st horizontal line
    pygame.draw.line(screen, LINE, (0,SQUARE_SIZE),(WIDTH,SQUARE_SIZE),LINE_WIDTH)
    # 2nd horizontal line
    pygame.draw.line(screen, LINE, (0,2*SQUARE_SIZE), (WIDTH, 2*SQUARE_SIZE), LINE_WIDTH)

    # 1st vertical line
    pygame.draw.line(screen, LINE, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    # 2nd horizontal line
    pygame.draw.line(screen, LINE, (2*SQUARE_SIZE, 0), (2*SQUARE_SIZE, HEIGHT), LINE_WIDTH)

def drawFigures():
    for row in range(BRD_ROW):
        for col in range(BRD_COL):
            if board[row][col] == 1:
                pygame.draw.circle(screen, PINK, (int(col*SQUARE_SIZE + SQUARE_SIZE//2),int(row*SQUARE_SIZE + SQUARE_SIZE//2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, BLUE, (col*SQUARE_SIZE + SPACE, row*SQUARE_SIZE + SQUARE_SIZE - SPACE), (col*SQUARE_SIZE + SQUARE_SIZE - SPACE, row*SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, BLUE, (col*SQUARE_SIZE + SPACE, row*SQUARE_SIZE + SPACE), (col*SQUARE_SIZE + SQUARE_SIZE - SPACE, row*SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def markSpace(row, col, player):
    board[row][col] = player

def isSpaceFree(row,col):
    return board[row][col] == 0

def isBoardFull():
    for row in range(BRD_ROW):
        for col in range(BRD_COL):
            if board[row][col] == 0:
                return False
    return True

def checkWinner(player):
    # vertical win check
    for col in range(BRD_COL):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            vertWinLine(col,player)
            return True

    # horizontal win check
    for row in range(BRD_ROW):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            hozWinLine(row,player)
            return True

    # ascending diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        ascDiagonal(player)
        return True

    # descending diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        descDiagonal(player)
        return True

    return False # no winner


def vertWinLine(col,player):
    posX = col*SQUARE_SIZE + SQUARE_SIZE//2

    if player == 1:
        colour = PINK
    elif player == 2:
        colour = BLUE

    pygame.draw.line(screen,colour,(posX,15), (posX, HEIGHT - 15), 15)

def hozWinLine(row,player):
    posY = row*SQUARE_SIZE+SQUARE_SIZE//2

    if player == 1:
        colour = PINK
    elif player == 2:
        colour = BLUE

    pygame.draw.line(screen,colour,(15,posY), (WIDTH - 15,posY), 15)

def ascDiagonal(player):
    if player == 1:
        colour = PINK
    elif player == 2:
        colour = BLUE

    pygame.draw.line(screen, colour, (15,HEIGHT - 15), (WIDTH - 15, 15), 15)

def descDiagonal(player):
    if player == 1:
        colour = PINK
    elif player == 2:
        colour = BLUE

    pygame.draw.line(screen, colour, (15,15), (WIDTH - 15, HEIGHT - 15), 15)

def restart():
    screen.fill(BG_COLOUR)
    drawLines()
    player = 1
    for row in range(BRD_ROW):
        for col in range(BRD_COL):
            board[row][col] = 0

drawLines()

player = 1
gameover = False


# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not gameover:

            mouseX = event.pos[0] #x coordinate
            mouseY = event.pos[1] #y coordinate

            clickedRow = int(mouseY // SQUARE_SIZE)
            clickedCol = int(mouseX // SQUARE_SIZE)

            if isSpaceFree(clickedRow, clickedCol):
                markSpace(clickedRow,clickedCol,player)
                if checkWinner(player):
                    gameover = True
                player = player % 2 + 1

                drawFigures()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: # press r to restart game
                restart()
                gameover = False

    pygame.display.update()


# class Tic_Tac_Toe():
    # ------------------------------------------------------------------
    # Initialization Functions:
    # ------------------------------------------------------------------
#     def __init__(self):
#         self.window.title('Tic-Tac-Toe')
#         self.canvas.pack()
#         # Input from user in form of clicks
#         self.window.bind('<Button-1>', self.click)
#
#         self.initialize_board()
#         self.player_X_turns = True
#         self.board_status = np.zeros(shape=(3, 3))
#
#         self.player_X_starts = True
#         self.reset_board = False
#         self.gameover = False
#         self.tie = False
#         self.X_wins = False
#         self.O_wins = False
#
#         self.X_score = 0
#         self.O_score = 0
#         self.tie_score = 0
#
#     def mainloop(self):
#         self.window.mainloop()
#
#     def initialize_board(self):
#         for i in range(2):
#             self.canvas.create_line((i + 1) * board / 3, 0, (i + 1) * board / 3, board)
#
#         for i in range(2):
#             self.canvas.create_line(0, (i + 1) * board / 3, board, (i + 1) * board / 3)
#
#     def play_again(self):
#         self.initialize_board()
#         self.player_X_starts = not self.player_X_starts
#         self.player_X_turns = self.player_X_starts
#         self.board_status = np.zeros(shape=(3, 3))
#
#     def display_gameover(self):
#
#         if self.X_wins:
#             self.X_score += 1
#             text = 'Player 1 (X)'
#             color = PINK
#         elif self.O_wins:
#             self.O_score += 1
#             text = 'Player 2 (O)'
#             color = BLUE
#         else:
#             self.tie_score += 1
#             text = 'Its a tie'
#             color = 'gray'