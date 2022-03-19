# Importing packages for the main menu
import pygame, sys
from button import Button

pygame.init()

#Setting up the screen size
SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("assets/Background.png")

# Initialising the font of the main menu
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def game1():
    while True:
        GAME1_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        GAME1_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        GAME1_RECT = GAME1_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(GAME1_TEXT, GAME1_RECT)

        GAME1_BACK = Button(image=None, pos=(640, 460),
                              text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        GAME1_BACK.changeColor(GAME1_MOUSE_POS)
        GAME1_BACK.update(SCREEN)

        GAME1_BACK.changeColor(GAME1_MOUSE_POS)
        GAME1_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME1_BACK.checkForInput(GAME1_MOUSE_POS):
                    main_menu()

        pygame.display.update()
    
def game2():
    while True:
        GAME2_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        GAME2_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        GAME2_RECT = GAME2_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(GAME2_TEXT, GAME2_RECT)

        GAME2_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        GAME2_BACK.changeColor(GAME2_MOUSE_POS)
        GAME2_BACK.update(SCREEN)

        GAME2_BACK.changeColor(GAME2_MOUSE_POS)
        GAME2_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME2_BACK.checkForInput(GAME2_MOUSE_POS):
                    main_menu()

        pygame.display.update()
def game3():
    while True:
        GAME3_MOUSE_POS = pygame.mouse.get_pos()

        SCREEN.fill("black")

        GAME3_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
        GAME3_RECT = GAME3_TEXT.get_rect(center=(640, 260))
        SCREEN.blit(GAME3_TEXT, GAME3_RECT)

        GAME3_BACK = Button(image=None, pos=(640, 460),
                            text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

        GAME3_BACK.changeColor(GAME3_MOUSE_POS)
        GAME3_BACK.update(SCREEN)

        GAME3_BACK.changeColor(GAME3_MOUSE_POS)
        GAME3_BACK.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME3_BACK.checkForInput(GAME3_MOUSE_POS):
                    main_menu()

        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        Game1_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 230),
                            text_input="Game 1", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        Game2_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 350),
                            text_input="Game 2", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        Game3_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 470),
                              text_input="Game 3", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 590),
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [Game1_BUTTON, Game2_BUTTON, Game3_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Game1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game1()
                if Game2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game2()
                if Game3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game3()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()