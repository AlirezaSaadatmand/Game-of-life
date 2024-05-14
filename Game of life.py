import pygame
from sys import exit
import random



WIDTH , HEIGHT = 1000 , 600

UNIT = 20

blocks = []

class Block:
    def __init__(self , xpos , ypos , x , y , id):
        self.x = x
        self.y = y
        
        self.xpos = xpos
        self.ypos = ypos
        
        self.id = id
        
        self.color = "black"
    
        self.neigh = []
        
         
        self.sur = pygame.Surface( (UNIT , UNIT) )
        self.sur_rect = self.sur.get_rect(topleft = (self.xpos , self.ypos))
        
        
    def get_beighbors(self):
        x = self.x
        y = self.y
        
        if x - 1 < 0:
            x = WIDTH // UNIT + 1
        elif x + 1 > 0:
            x = -1
            
        if y - 1 < 0:
            y = HEIGHT // UNIT + 1
        elif y + 1 > 0:
            y = -1
            
        top = [x , y-1]
        buttom = [x , y+1]
        left = [x-1 , y]
        right = [x+1 , y]
        topLeft = [x-1 , y-1]
        topRight = [x+1 , y-1]
        buttomLeft = [x-1 , y+1]
        buttomRight = [x+1 , y+1]
        
        for block in blocks:
            if [block.x , block.y] in [top , buttom , left , right , topLeft , topRight , buttomLeft , buttomRight]:
                self.neigh.append(block)
    
    def next_tick(self):
        count = 0
        for n in self.neigh:
            if n.color == "white":
                count += 1
                
                
        if self.color == "black" and count == 3:
            self.color = "white"
            return 
        else:
            if count == 3 or count == 2:
                self.color = "white"
                return
        self.color = "black"
        
        
        
    def draw(self):
        self.sur.fill(self.color)
        screen.blit(self.sur , self.sur_rect)
        pygame.draw.rect(screen , "black", self.sur_rect,  1, 0)
    
def create_board():

    count = 1
    for i in range(0 , HEIGHT // UNIT):
        for j in range(0 , WIDTH // UNIT):
            blocks.append(Block(j * UNIT , i * UNIT ,  j , i , count))
            count += 1
create_board()

def random_lifes():
    for block in blocks:
        if random.random() > .5:
            block.color = "white"
random_lifes()

def get():
    for block in blocks:
        block.get_beighbors()
get()
def draw():
    for block in blocks:
        block.draw()
        block.next_tick()

pygame.init()
screen = pygame.display.set_mode( (WIDTH , HEIGHT) )
screen.fill("#f59563")
pygame.display.set_caption("KNIGHT PROBLEM")
clock = pygame.time.Clock()


while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    draw()
    pygame.display.update()
    clock.tick(10)