
import pygame
import pygame as pg
import sys
import random
import pickle
import os

#pygame.init()

fps = 60
WIDTH = 1280;  HEIGHT = 720
MWIDTH1 = 280; MWIDTH2 = 1000
MHEIGHT1 = 0; MHEIGHT2 = 720
clock =pygame.time.Clock()
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('GAME')
bg = pygame.transform.scale(pygame.image.load('grass.png'),(710,710))
bg_2=pygame.image.load("main_bg.png")
QB_images_path = []
for image in os.listdir("QB") :
    
    QB_images_path.append(image)

Run = True
N = 72
n=1
tile_size = HEIGHT/N
nx = WIDTH//tile_size ; ny = HEIGHT//tile_size
lev=1

class Block(pg.sprite.Sprite) :
    def __init__(self,x,y) :
        super().__init__()
        #self.image = pg.Surface((tile_size,tile_size))
        #self.image.fill((0,random.randint(100,255),0))
        self.image = pygame.transform.scale(pygame.image.load('wall.png'),(10,10))
        self.rect = self.image.get_rect()
        self.x = x ; self.y = y
        self.rect.x = x*tile_size ; self.rect.y = y*tile_size
    def update(self) :
        pass
    def getxy(self) :
        return (self.x  , self.y)

class CheckpointBlock(pg.sprite.Sprite) :
    def __init__(self,x,y) :
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load("checkpoint.png"), (tile_size*4, tile_size*4))
        self.rect = self.image.get_rect()
        self.x = x ; self.y = y
        self.rect.x = x*tile_size ; self.rect.y = y*tile_size
    def update(self) :
        if self.rect.colliderect(player) :
            
            question_grp.add(Question())
            self.kill()
            

    def getxy(self) :
        return (self.x  , self.y)
    

class Question(pg.sprite.Sprite) :
    def __init__(self) :
        super().__init__()
        self.image_path = random.choice(QB_images_path)
        self.ans = self.image_path[0]
        self.image = pygame.image.load("QB/" + self.image_path)
        #self.image = pg.Surface((tile_size*N/2,tile_size*N/2))
        #self.image.fill((random.randint(100,255),0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 0; self.rect.y = 0

        
        print(self.rect.x,self.rect.y)
        print(self.rect.topleft)
        player.allow_update = False

        player.cor_ans = None


        self.left = (MWIDTH1 + tile_size*16)
        self.middle = HEIGHT/2
        
    def update(self) :
        #print(self.Arect.topleft,self.Brect.topleft,self.ans)
        mousepoint = pygame.mouse.get_pos()
        print(mousepoint)
        if mousepoint[0] > self.left :
            
            if mousepoint[1] < self.middle and self.ans == "1":
                player.keys += 1
                player.cor_ans = True
                
            elif self.ans == "2":
                player.keys+=1
                player.cor_ans = True
            
            else:
                player.cor_ans = False


            print("keys : ",player.keys)
            player.allow_update = True
            print("nice")
            self.kill()

class Door(pg.sprite.Sprite) :
    def __init__(self,x,y) :
        super().__init__()
        self.image=pygame.transform.scale(pygame.image.load("door.png"), (tile_size*6, tile_size*6))
        self.rect = self.image.get_rect()
        self.x = x ; self.y = y
        self.rect.x = x*tile_size ; self.rect.y = y*tile_size
        self.counter = 0
        self.time_second = 3
    
    def update(self) :
        global run
        print('yes')
        if self.rect.colliderect(player.rect) :
            print('yo')

            font = pygame.font.Font('font.ttf', 16)
            text = font.render(f'Mining the rock {self.time_second- (self.counter//fps)}', True,"#FFFFFF")
            screen.blit(text, (MWIDTH2,HEIGHT/4))
            if ((self.counter//20)%2 == 0):
                self.pick=pygame.transform.scale(pygame.image.load('key.png'),(tile_size*10,tile_size*10))
                screen.blit(self.pick,(tile_size*2,tile_size*16))


            self.counter += 1
            if self.counter >= fps * self.time_second :
                if player.keys > 0 : 
                    player.keys -= 1
                    print("keys : ",player.keys)

                    self.kill()

                else :
                    print("insufficient keys")
                    run=False

                        #ADD LABEL HERE FOR INSUFFICIENT KEYS
        

        
            if self.rect.colliderect(player.rect) :
                
                if player.direction.x < 0 and player.rect.left + player.speed  == self.rect.right : 
                    self.rect.left = self.rect.right
                    
                if player.direction.x > 0 and player.rect.right - player.speed == self.rect.left : 
                    player.rect.right = self.rect.left

        
            if self.rect.colliderect(player.rect) :
                print(self.rect.top,self.rect.bottom)
                if player.direction.y > 0 and player.rect.bottom > self.rect.top  :
                    player.rect.bottom = self.rect.top
                    
                    #self.direction.y = 0
                    
                if player.direction.y < 0 and player.rect.top < self.rect.bottom:
                    player.rect.top = self.rect.bottom

        elif self.counter > 0 :
            self.counter = 0

    def getxy(self) :
        return (self.x  , self.y)

    
class Player(pg.sprite.Sprite) :
    def __init__(self,x,y) :
        super().__init__()
        #self.image = pg.Surface((tile_size*2,tile_size*2))
        self.direction = pg.math.Vector2()
        self.speed = (tile_size/10) * 2
        self.allow_update = True       
        self.dim = (40,40)
        self.image = pygame.transform.scale(pygame.image.load('sprites/r0.png'),self.dim)
        self.rect = self.image.get_rect()
        self.rect.x = x ; self.rect.y = y
        self.counter = 0
        self.idx=0
        self.keys=0
        self.cor_ans = None

        self.up = []
        self.down = []
        self.left = []
        self.right = []

        for i in range(4):
            self.up.append(pygame.transform.scale(pygame.image.load(f'sprites/u{i}.png'),self.dim))
            self.down.append(pygame.transform.scale(pygame.image.load(f'sprites/d{i}.png'),self.dim))
            self.left.append(pygame.transform.scale(pygame.image.load(f'sprites/l{i}.png'),self.dim))
            self.right.append(pygame.transform.scale(pygame.image.load(f'sprites/r{i}.png'),self.dim)) 
        
        
    def update(self) :
            if self.allow_update :
                
                self.input()
                self.horizontal_collisions()
                self.vertical_collisions()
                self.animation()


    def animation(self):
        keys = pygame.key.get_pressed()

        if self.counter>=60: self.counter //= 60

        if self.counter % 6 == 0:
            self.idx = self.counter//15
        self.counter+=1

        if(keys[pygame.K_w]):
            #self.y -= self.speed
            self.image = pygame.transform.scale(self.up[self.idx],self.dim)
            self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
        if(keys[pygame.K_s]):
            #self.y += self.speed
            self.image = pygame.transform.scale(self.down[self.idx],self.dim)
            self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
        if(keys[pygame.K_a]):
            #self.x -= self.speed
            self.image = pygame.transform.scale(self.left[self.idx],self.dim)
            self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))
        if(keys[pygame.K_d]):
            #self.x += self.speed
            self.image = pygame.transform.scale(self.right[self.idx],self.dim)
            self.rect = self.image.get_rect(center=(self.rect.centerx,self.rect.centery))


    def input(self) :
        keys = pg.key.get_pressed()
        if keys[pg.K_d] : self.direction.x  = 1
        elif keys[pg.K_a] : self.direction.x  = -1
        else : self.direction.x = 0
        keys = pg.key.get_pressed()
        if keys[pg.K_w] : self.direction.y  = -1
        elif keys[pg.K_s] : self.direction.y  = 1
        else : self.direction.y = 0
        self.rect.x += self.direction.x * self.speed 
        self.rect.y += self.direction.y * self.speed 
        
            
    def horizontal_collisions(self) :
        for block in block_grp :
            if block.rect.colliderect(self.rect) :
                
                if self.direction.x < 0 and self.rect.left + self.speed  == block.rect.right : 
                    self.rect.left = block.rect.right
                    
                if self.direction.x > 0 and self.rect.right - self.speed == block.rect.left : 
                    self.rect.right = block.rect.left
            
        
              
              
                
    def vertical_collisions(self) :
        for block in block_grp :
            if block.rect.colliderect(self.rect) :
                print(self.rect.top,block.rect.bottom)
                if self.direction.y > 0 and self.rect.bottom > block.rect.top  :
                    self.rect.bottom = block.rect.top
                    
                    #self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0 and self.rect.top < block.rect.bottom:
                    self.rect.top = block.rect.bottom
                    
                    #self.direction.y = 0
       
                
       
        

    def border_collisions(self) :
        if self.rect.right > WIDTH :
            self.rect.right = WIDTH
        if self.rect.left < 0 :
            self.rect.left = 0
    
    def new_collisions(self) :
        for block in block_grp :
            if block.rect.colliderect(self.rect) :
                if self.direction.y > 0 :
                    self.rect.bottom = block.rect.top

                if self.direction.y < 0 :
                    self.rect.top = block.rect.bottom

                if self.direction.x < 0  : 
                    self.rect.left = block.rect.right
                    
                if self.direction.x > 0  : 
                    self.rect.right = block.rect.left
        



def draw_grid() :
    for line in range(0,N) :
        pygame.draw.line(screen,(255,0,0),(MWIDTH1,(line*tile_size)),(MWIDTH2,line*tile_size))
        pygame.draw.line(screen,(255,0,0),(MWIDTH1 + line*tile_size,MHEIGHT1),(MWIDTH1 + line*tile_size,MHEIGHT2))

spawnx,spawny = MWIDTH1-50,tile_size*44

player = Player(spawnx,spawny)
block_grp = pg.sprite.Group()
player_grp = pg.sprite.Group()
checkpoint_grp = pg.sprite.Group()
question_grp = pg.sprite.Group()
door_grp = pg.sprite.Group()
all_sprites_grp = pg.sprite.Group()
display_surface = pg.display.get_surface()


def custom_draw() :
        #self.moving_camera()
        for sprite in block_grp :
            
                offset_pos = sprite.rect.topleft# - self.offset
                display_surface.blit(sprite.image,offset_pos)
        
        display_surface.blit(player.image,player.rect.topleft)
        
        for ckb in checkpoint_grp :
            display_surface.blit(ckb.image,ckb.rect.topleft)

        for door in door_grp :
            display_surface.blit(door.image,door.rect.topleft)

        for question in question_grp :
            #print(question.rect.topleft)
            display_surface.blit(question.image,question.rect.topleft )

        text_data= "Pickaxes left : "+ str(player.keys)

        font = pygame.font.Font('font.ttf', 32)
        text = font.render(text_data, True,"#FEFCB2")
        screen.blit(text, (tile_size*2,tile_size*2))

        if player.cor_ans == True:
            font = pygame.font.Font('font.ttf', 32)
            text = font.render('Correct', True,"#00FF00")
            screen.blit(text, (tile_size*2,tile_size*10))

        if player.cor_ans == False:
            font = pygame.font.Font('font.ttf', 32)
            text = font.render('Wrong', True,"#FF0000")
            screen.blit(text, (tile_size*2,tile_size*10))

                
        

def setrandomblocks() :
    n = random.randint(0,nx)
    for i in range(n) :
        block_grp.add(Block(random.randint(0,nx),random.randint(0,ny)))
 
def setblocks() :
    for x in range(nx) :
        block_grp.add(Block(x,(ny-2)))

def addtoallspritesgrp() :
    for block in block_grp  :
        
            all_sprites_grp.add(block)

def modifyblocks(group) :
    if group == (Block) : grp = block_grp
    elif group == CheckpointBlock : grp = checkpoint_grp
    elif group == Door : grp = door_grp
        
    
    #asp = all_sprites_grp
    mx,my = pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]
    #x = mx - mx%tile_size + asp.offset.x ; y = my - my % tile_size + asp.offset.y
    x = mx - mx%tile_size ; y = my - my % tile_size

    if not deleteblocks(x,y,group, True) :
    
        
        grp.add(group(x//tile_size,y//tile_size))
        #all_sprites_grp.add(group(x//tile_size,y//tile_size))

def massmodifyblocks(group) :
    if group == (Block) : grp = block_grp
    elif group == CheckpointBlock : grp = checkpoint_grp
    elif group == Door : grp = door_grp

    if pg.key.get_pressed()[pg.K_f] : 
        #asp = all_sprites_grp
        mx,my = pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]
        #x = mx - mx%tile_size + asp.offset.x ; y = my - my % tile_size + asp.offset.y
        x = mx - mx%tile_size  ; y = my - my % tile_size 
        if not deleteblocks(x,y,group, False) :
            
            grp.add(group(x//tile_size,y//tile_size))
            #all_sprites_grp.add(group(x//tile_size,y//tile_size))
    if pg.key.get_pressed()[pg.K_g] :
        #asp = all_sprites_grp
        mx,my = pg.mouse.get_pos()[0],pg.mouse.get_pos()[1]
        #x = mx - mx%tile_size + asp.offset.x ; y = my - my % tile_size + asp.offset.y
        x = mx - mx%tile_size  ; y = my - my % tile_size
        deleteblocks(x,y,group, True)
        
        
            
def deleteblocks(x,y,group,kill) :
    if group == (Block) : grp = block_grp
    elif group == CheckpointBlock : grp = checkpoint_grp
    elif group == Door : grp = door_grp
    
    for block in grp :
        if block.getxy() == (x//tile_size,y//tile_size) and isinstance(block,group) :
            if kill : 
                block.kill() 
                return True
                

    '''
    for block in all_sprites_grp :
        if isinstance(block,group) :
            if block.getxy() == (x//tile_size ,y//tile_size ) :
                if kill : block.kill()
                pg.display.update()
                return True
    '''
    
    return False



    

def clear_screen() :
    for block in block_grp :
        block.kill()
    for ckb in checkpoint_grp :
        ckb.kill()
    for door in door_grp :
        door.kill()
    for block in all_sprites_grp :
        if not isinstance(block,Player) :
            block.kill()
            pg.display.update()
    

def random_level() :
    clear_screen()
    setrandomblocks()
    addtoallspritesgrp()
            
def store_levels() :
    #level1.dat
    f = open(f'level{lev}.dat','ab')
    L = []
    for block in block_grp :
        if not isinstance(block,Player) :
            x,y = block.getxy()
            L.append((x,y,type(block)))
    for block in checkpoint_grp :
        if not isinstance(block,Player) :
            x,y = block.getxy()
            L.append((x,y,type(block)))
    for block in door_grp :
        if not isinstance(block,Player) :
            x,y = block.getxy()
            L.append((x,y,type(block)))
    

    
    pickle.dump(L,f)
    f.close()
    
def load_levels() :
    global n

    player.cor_ans = None
    #global lev
    #print('length of file ',  len_file())
    #print(n)
    clear_screen()
   
    f = open(f'level{lev}.dat','rb')
    #n = 3
    #for i in range(n) :
    L = pickle.load(f)
    
    if len_file() != 0 :
        for (x,y,block) in L :
            #if block == Ladder : ladder_grp.add(block(x,y))
            if block == Block : 
                block_grp.add(block(x,y))
                #all_sprites_grp.add(block(x,y))

            elif block == CheckpointBlock : checkpoint_grp.add(block(x,y))
            elif block == Door : door_grp.add(block(x,y))
            
    n += 1

def len_file() :
    f = open('level1.dat','rb')
    n = 0
    while True :
        try : x = pickle.load(f)
        except : return n
        else : n += 1
    
def ticks(tick) :
    tick += 1
    return tick
 

for block in block_grp :
    all_sprites_grp.add(block)
for block in checkpoint_grp :
    all_sprites_grp.add(block)
all_sprites_grp.add(player)
player_grp.add(player)

def next_level():
    global lev
    global run

    if lev == 1 and player.rect.right == MWIDTH2:
            lev = 2
            clear_screen()
            load_levels()
            load_levels()
            player.rect.x=spawnx
            player.rect.y=tile_size*36
    if lev == 2 and player.rect.right == MWIDTH2:
            lev = 3
            clear_screen()
            load_levels()
            load_levels()
            player.rect.x=spawnx
            player.rect.y=tile_size*51

    if lev == 3 and player.rect.right == MWIDTH2:
        run=False
        
run=True


def main() :
    pygame.init()
    load_levels()
    load_levels()

    global lev
    global run

    lev = 1

    run = True
    player.rect.x= spawnx
    player.rect.y=spawny

    group = Block
    while run :
        screen.fill((0,0,0))
        screen.blit(bg_2, (0,0))
        screen.blit(bg,(MWIDTH1,0))
        for event in pg.event.get() :
            if event.type == pg.MOUSEBUTTONDOWN :
                #if event.button == 1  : modifyblocks(group)
                if event.button == 1 : question_grp.update()
                
            if event.type == pg.KEYDOWN :
                
                #if event.key == pg.K_c  : clear_screen()
                #if event.key == pg.K_l : load_levels()
                #if event.key == pg.K_r : random_level()
                #if event.key == pg.K_UP: player.creative = True
                #if event.key == pg.K_DOWN : player.creative = False
                #if event.key ==pg.K_1 : group = Block
                #if event.key == pg.K_2 : group = CheckpointBlock
                #if event.key == pg.K_3 : group = Door
                
                #if event.key == pg.K_k  :
                #    if os.path.exists(f'level{lev}.dat') : os.remove(f'level{lev}.dat')
                #    store_levels() 
                pass
        
                
            if event.type == pg.QUIT :
                pg.quit()
                sys.exit()        

        player_grp.update()
        #massmodifyblocks(group)
        #all_sprites_grp.update()
        
        block_grp.update()
        checkpoint_grp.update()
        door_grp.update()
        #mob_grp.update()
        custom_draw()
        next_level()
        #draw_grid()
        pg.display.flip()
        clock.tick(fps)




