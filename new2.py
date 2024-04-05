import pygame,sys
from pygame import mixer
from button import Button
from tkinter import messagebox

pygame.init()
SCREEN = pygame.display.set_mode((800,600))

pygame.display.set_caption("MAZEdaar")

icon=pygame.image.load('gamelogo.png')
pygame.display.set_icon(icon)
BGimg = pygame.image.load("front_screen.png") 
SCREEN.blit(BGimg, (0,0))
def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("font.ttf", size)


mixer.music.load('menumusic.mp3')
mixer.music.play(-1)
 
#Basically nothing after this is working idk why someone help
while True:
        SCREEN.blit(BGimg, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        GAME1_BUTTON = Button(image= None, pos=(250, 250), 
                            text_input="Play", font=get_font(20), base_color="#d7fcd4", hovering_color="white")
        GAME2_BUTTON = Button(image=None,pos=(250, 450), 
                            text_input="Instructions", font=get_font(18), base_color="#d7fcd4", hovering_color="white")
        GAME3_BUTTON = Button(image=None,pos=(500, 250), 
                            text_input="Settings", font=get_font(16), base_color="#d7fcd4", hovering_color="white")

        for button in [GAME1_BUTTON, GAME2_BUTTON,GAME3_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                output=messagebox.askyesno('Confirm','Are you sure you want to exit MAZEdaar?')
                if output :
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    output=messagebox.askyesno('Confirm','Are you sure you want to exit MAZEdaar?')
                    if output :
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if GAME1_BUTTON.checkForInput(MENU_MOUSE_POS):
                    None
                if GAME2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    None
                if GAME3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    None
