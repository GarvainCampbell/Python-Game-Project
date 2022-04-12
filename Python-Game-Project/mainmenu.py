import pygame
from pygame.locals import *
import sys
sys.path.append("..\\Python-Game-Project\\Games\\Game1\\Game1.py") # for game one
sys.path.append("..\\Python-Game-Project\\Games\\Game 2\\space-impact-master\\space-impact-master\\space_impact.py") # for game two
sys.path.append("..\\Python-Game-Project\\Games\\Game3\\cnt4_menu.py") # for game three
import subprocess

pygame.init()
win = pygame.display.set_mode((700, 500))

snake_ladder = pygame.image.load(".\\Assets\\Play Snake and Ladders.png")
tictactoe = pygame.image.load(".\\Assets\\Play Tic Tac Toe.png")
space_impact = pygame.image.load(".\\Assets\\Play Space Impact.png")
quit_button = pygame.image.load(".\\Assets\\QUIT.png")
bg = pygame.image.load(".\\Assets\\Background.jpg")


class Button:
    def __init__(self, x, y, image, scale):
        self.width = image.get_width()
        self.height = image.get_height()
        self.x_position = x
        self.y_position = y
        self.image = pygame.transform.scale(image, (int(self.width * scale), (int(self.height * scale))))
        self.rect = 0

    def draw(self):
        self.rect = self.image.get_rect()
        self.rect.center = (self.x_position, self.y_position)
        win.blit(self.image, (self.rect.x, self.rect.y))

    def check_click(self, event):
        mouse_position = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        # selection to check if the event was a mouse button press
        if event.type == MOUSEBUTTONDOWN:
            # check if the press was within the button bounds
            if self.rect.collidepoint((mouse_position[0], mouse_position[1])):
                if click:
                    return True
        return False

class Menu:
    def __init__(self):
        self.game_one = Button(350, 100, snake_ladder, 1)
        self.game_two = Button(350, 200, tictactoe, 1)
        self.game_three = Button(350, 200, space_impact, 1)
        # REPLACE oneplayer, toplayer stuff with button images of your own
        self.game_number = self.game_select()

    def game_select(self):
        # Draw background and game selection buttons on screen
        # REPLACE background (bg)
        win.blit(bg, (0, 0))
        # draws menu buttons on screen
        self.game_one.draw()
        self.game_two.draw()
        self.game_three.draw()

        selecting_game = True
        while selecting_game:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                first_game = self.game_one.check_click(event)
                second_game = self.game_two.check_click(event)
                third_game = self.game_three.check_click(event)
                if first_game:
                    return 1
                elif second_game:
                    return 2
                elif third_game:
                    return 3
            pygame.display.update()

def main():
    win.blit(bg, (0, 0))
    run = True
    while run:
        # Pygame event handler loop to get events that happen in the game window.
        for event in pygame.event.get():
            # check for pygame QUIT event which is when player closes the program window
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        menu = Menu()
        if menu.game_number == 1:
             # CHANGE Subprocess paths. Check to see if it works on MAC
            subprocess.Popen("C:\\Users\\joelw\Downloads\\Snake and Ladder (executable, code, and game files)\\Game.exe")
        if menu.game_number == 2:
            subprocess.Popen("C:\\Users\\joelw\Downloads\\Snake and Ladder (executable, code, and game files)\\Game.exe")
        if menu.game_number == 3:
            subprocess.Popen("C:\\Users\\joelw\Downloads\\Snake and Ladder (executable, code, and game files)\\Game.exe")
        pygame.display.update()

if __name__ == "__main__":
    main()
