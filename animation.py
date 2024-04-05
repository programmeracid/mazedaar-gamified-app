import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
timer = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.dim = (60,80)
        self.image = pygame.transform.scale(pygame.image.load('sprites/r0.png'),self.dim)
        self.x=100
        self.y=100
        self.rect = self.image.get_rect(center=(self.x,self.y))
        self.counter = 0
        self.idx=0

        self.speed = 3

        self.up = []
        self.down = []
        self.left = []
        self.right = []

        for i in range(4):
            self.up.append(pygame.transform.scale(pygame.image.load(f'sprites/u{i}.png'),self.dim))
            self.down.append(pygame.transform.scale(pygame.image.load(f'sprites/d{i}.png'),self.dim))
            self.left.append(pygame.transform.scale(pygame.image.load(f'sprites/l{i}.png'),self.dim))
            self.right.append(pygame.transform.scale(pygame.image.load(f'sprites/r{i}.png'),self.dim))


    def update(self):

        keys = pygame.key.get_pressed()

        if self.counter>=60: self.counter //= 60

        if self.counter % 6 == 0:
            self.idx = self.counter//15
        self.counter+=1

        if(keys[pygame.K_w]):
            self.y -= self.speed
            self.image = pygame.transform.scale(self.up[self.idx],self.dim)
            self.rect = self.image.get_rect(center=(self.x,self.y))
        if(keys[pygame.K_s]):
            self.y += self.speed
            self.image = pygame.transform.scale(self.down[self.idx],self.dim)
            self.rect = self.image.get_rect(center=(self.x,self.y))
        if(keys[pygame.K_a]):
            self.x -= self.speed
            self.image = pygame.transform.scale(self.left[self.idx],self.dim)
            self.rect = self.image.get_rect(center=(self.x,self.y))
        if(keys[pygame.K_d]):
            self.x += self.speed
            self.image = pygame.transform.scale(self.right[self.idx],self.dim)
            self.rect = self.image.get_rect(center=(self.x,self.y))


        


            
      


player = Player()       
sgroup = pygame.sprite.Group()
sgroup.add(player)

while True:
    timer.tick(60)

    screen.fill((64,64,64))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    sgroup.draw(screen)
    player.update()
    pygame.display.flip()