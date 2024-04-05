import pygame
from pygame import mixer
from button import Button
import toggle
from tkinter import messagebox
from tkinter import Scale
import sys
import MazeDasNew2
from MazeDasNew2 import *
import pickle,os

def game_over():
    SCREEN = pygame.display.set_mode((1280,720))

    pygame.display.set_caption("MAZEdaar - Game Over")
    icon=pygame.image.load('gamelogo.png')
    pygame.display.set_icon(icon)

    BGimg = pygame.image.load("gameover_screen2.png") 
    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("font.ttf", size)
    
    while True:
        SCREEN.blit(BGimg, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        GAME1_BUTTON = Button(image= None, pos=(360,400), 
                            text_input="Return to Main Menu", font=get_font(20), base_color="#d7fcd4", hovering_color="#B637BC")
        GAME2_BUTTON = Button(image=None,pos=(360,450), 
                            text_input="Exit", font=get_font(18), base_color="#d7fcd4", hovering_color="#B637BC")

        for button in [GAME1_BUTTON, GAME2_BUTTON]:
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
                    main_menu()
                if GAME2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    output=messagebox.askyesno('Confirm','Are you sure you want to exit MAZEdaar?')
                    if output :
                        pygame.quit()
                        sys.exit()
        pygame.display.flip()

def play_music():
    mixer.music.load('menumusic.mp3')
    mixer.music.play(-1)

flag=False
def music_toggle():
    global flag
    if flag:
        mixer.music.load('menumusic.mp3')
        mixer.music.play(-1)
    
    else :
        mixer.music.stop()
    flag = not flag
        

def settings():
    SCREEN = pygame.display.set_mode((1280,720))
    purple="#B637BC"
    white = "#d7fcd4"
    pygame.display.set_caption("MAZEdaar - Settings")

    icon=pygame.image.load('gamelogo.png')
    pygame.display.set_icon(icon)
    SCREEN.fill("#13002D")

    font2 = pygame.font.Font('font2.otf', 70)
    text=font2.render("Settings",True,purple)
    SCREEN.blit(text,(45,45))

    font1 = pygame.font.Font("font.ttf", 16)
    text=font1.render("Turn off Music ", True,white)
    goback_text=font2.render("<", True, purple)
    SCREEN.blit(text, (50,180))
    #SCREEN.blit(goback_text, (700,45))

    image_on = pygame.image.load("toggle_button_on.png")
    image_off = pygame.image.load("toggle_button_off.png")
    button = toggle.ToggleButton(310, 165, image_on, image_off)
   
    running=True
    
    while running:
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running= False
            if event.type== pygame.KEYDOWN :
                if event.key == pygame. K_ESCAPE:
                    running=False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button.rect.collidepoint(event.pos):
                    button.toggle()
                    music_toggle()
                    #mixer.music.stop()


        button.draw(SCREEN)
        pygame.display.flip()

def instructions():
    SCREEN = pygame.display.set_mode((1280,720))
    purple="#B637BC"
    white = "#d7fcd4"
    pygame.display.set_caption("MAZEdaar - Instructions")

    icon=pygame.image.load('gamelogo.png')
    pygame.display.set_icon(icon)
    SCREEN.fill("#13002D")

    font2 = pygame.font.Font('font2.otf', 70)
    text=font2.render("Instructions",True,purple)
    SCREEN.blit(text,(45,45))

    font1 = pygame.font.Font("font.ttf", 16)
    textA=font1.render("Use WASD to move the player.\n", True,white)
    textB=font1.render("Use ESC to go back to the previous menu.\n.\n", True,white)
    textC=font1.render("Left click on the option to lock the answer in the projected question.\n", True,white)
    textD=font1.render("Keep moving towards the rock for 3 or more seconds to open the maze.\n", True,white)
    textE=font1.render("Earn pickaxes to break the rocks, to move to the next Level.\n", True,white)


    SCREEN.blit(textA, (50,180))
    SCREEN.blit(textB, (50,220))
    SCREEN.blit(textC, (50,260))
    SCREEN.blit(textD, (50,300))
    SCREEN.blit(textE, (50,340))

    goback_text=font2.render("<", True, purple)
    #SCREEN.blit(goback_text, (700,45))

    running=True

    while running:
        
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running= False
            if event.type== pygame.KEYDOWN :
                if event.key == pygame. K_ESCAPE:
                    running=False
        pygame.display.flip()


def main_menu():
    SCREEN = pygame.display.set_mode((1280,720))

    pygame.display.set_caption("MAZEdaar")
        
    play_music()
    icon=pygame.image.load('gamelogo.png')
    pygame.display.set_icon(icon)

    
    BGimg = pygame.image.load("main_Screen.png") 
    def get_font(size): # Returns Press-Start-2P in the desired size
        return pygame.font.Font("font.ttf", size)
    
    while True:
        SCREEN.blit(BGimg, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        GAME1_BUTTON = Button(image= None, pos=(360, 400), 
                            text_input="Play", font=get_font(20), base_color="#d7fcd4", hovering_color="#B637BC")
        GAME2_BUTTON = Button(image=None,pos=(360, 450), 
                            text_input="Instructions", font=get_font(18), base_color="#d7fcd4", hovering_color="#B637BC")
        GAME3_BUTTON = Button(image=None,pos=(360, 500), 
                            text_input="Settings", font=get_font(16), base_color="#d7fcd4", hovering_color="#B637BC")

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
                    MazeDasNew2.main()
                    game_over()
                if GAME2_BUTTON.checkForInput(MENU_MOUSE_POS):
                    instructions()
                if GAME3_BUTTON.checkForInput(MENU_MOUSE_POS):
                    settings()
        pygame.display.flip()

def start_menu():
    SCREEN = pygame.display.set_mode((800,450),pygame.NOFRAME)
    logo=pygame.image.load('front_screen.png')
    running = True

    while running:
        
        SCREEN.blit(logo,(0,0))

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running= False
            if event.type== pygame.KEYDOWN :
                if event.key == pygame. K_ESCAPE:
                    running=False

            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    running= False
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    running=False
                    main_menu()
                
        pygame.display.update()


pygame.init()
start_menu()