import pygame, sys
import numpy as np

pygame.init()

#--------------------------------------------------
class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

#--------------------------------------------------
SCREEN = pygame.display.set_mode((700, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/bg.jpeg")


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)


def play():
    import numpy as np
    import pygame
    import sys
    import math

    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    YELLOW = (255, 255, 0)
    ROW_COUNT = 6
    COLUMN_COUNT = 7

    def mainGame():
        def create_board():
            board = np.zeros((ROW_COUNT, COLUMN_COUNT))
            return board

        def drop_piece(board, row, col, piece):
            board[row][col] = piece

        def is_valid_location(board, col):
            return board[ROW_COUNT - 1][col] == 0

        def get_next_open_row(board, col):
            for r in range(ROW_COUNT):
                if board[r][col] == 0:
                    return r

        def print_board(board):
            print(np.flip(board, 0))

        def winning_move(board, piece):
            # Check horizontal locations for win
            for c in range(COLUMN_COUNT - 3):
                for r in range(ROW_COUNT):
                    if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                        c + 3] == piece:
                        return True

            # Check vertical locations for win
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT - 3):
                    if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][
                        c] == piece:
                        return True

            # Check positively sloped diaganols
            for c in range(COLUMN_COUNT - 3):
                for r in range(ROW_COUNT - 3):
                    if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and \
                            board[r + 3][c + 3] == piece:
                        return True

            # Check negatively sloped diaganols
            for c in range(COLUMN_COUNT - 3):
                for r in range(3, ROW_COUNT):
                    if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and \
                            board[r - 3][c + 3] == piece:
                        return True

        def draw_board(board):
            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT):
                    pygame.draw.rect(screen, BLUE,
                                     (c * SQUARESIZE, r * SQUARESIZE + SQUARESIZE, SQUARESIZE, SQUARESIZE))
                    pygame.draw.circle(screen, BLACK, (
                        int(c * SQUARESIZE + SQUARESIZE / 2), int(r * SQUARESIZE + SQUARESIZE + SQUARESIZE / 2)),
                                       RADIUS)

            for c in range(COLUMN_COUNT):
                for r in range(ROW_COUNT):
                    if board[r][c] == 1:
                        pygame.draw.circle(screen, RED, (
                            int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)),
                                           RADIUS)
                    elif board[r][c] == 2:
                        pygame.draw.circle(screen, YELLOW, (
                            int(c * SQUARESIZE + SQUARESIZE / 2), height - int(r * SQUARESIZE + SQUARESIZE / 2)),
                                           RADIUS)
            pygame.display.update()

        board = create_board()
        print_board(board)
        game_over = False
        turn = 0

        pygame.init()

        SQUARESIZE = 100

        width = COLUMN_COUNT * SQUARESIZE
        height = (ROW_COUNT + 1) * SQUARESIZE

        size = (width, height)

        RADIUS = int(SQUARESIZE / 2 - 5)

        screen = pygame.display.set_mode(size)
        draw_board(board)
        pygame.display.update()

        myfont = pygame.font.SysFont("monospace", 75)

        while not game_over:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    posx = event.pos[0]
                    if turn == 0:
                        pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                    else:
                        pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE / 2)), RADIUS)
                pygame.display.update()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pygame.draw.rect(screen, BLACK, (0, 0, width, SQUARESIZE))
                    # print(event.pos)
                    # Ask for Player 1 Input
                    if turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / SQUARESIZE))

                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 1)

                            if winning_move(board, 1):
                                label = myfont.render("Player 1 wins!!", 1, RED)
                                screen.blit(label, (40, 10))
                                game_over = True


                    # # Ask for Player 2 Input
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx / SQUARESIZE))

                        if is_valid_location(board, col):
                            row = get_next_open_row(board, col)
                            drop_piece(board, row, col, 2)

                            if winning_move(board, 2):
                                label = myfont.render("Player 2 wins!!", 1, YELLOW)
                                screen.blit(label, (40, 10))
                                game_over = True

                    print_board(board)
                    draw_board(board)

                    turn += 1
                    turn = turn % 2

                    if game_over:
                        pygame.time.wait(3000)

    mainGame()
    pygame.display.update()

def main_menu():
   while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(80).render('CONNECT FOUR', True, "white")
        MENU_RECT = MENU_TEXT.get_rect(center=(350, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(350, 350),
                             text_input="PLAY", font=get_font(60), base_color="White", hovering_color="#ffff62")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(350, 500),
                             text_input="QUIT", font=get_font(60), base_color="White", hovering_color="#ff3232")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()

#--------------------------------------------------
