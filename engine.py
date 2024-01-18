import pygame,random,sys,name

clock = pygame.time.Clock
from pygame.locals import *
pygame.init()

window=[1284,750]
screen = pygame.display.set_mode(window,0,32)
display= pygame.Surface((642,375))

#variables
moving_right=False
moving_left=False
frame=0
moving_up=moving_down=moving_left=moving_right = False
sheep_cord=[random.randint(0,600),random.randint(0,260)]
flip=False
vel_x=0.03
x=10
y=10
r=0
right_or_left=0
current_animation='idle'
write = pygame.font.SysFont('arial',12)
sheeps=[]
object_list=[]
scroll_x=0
scroll_y=0

global animation
animation = {}

def add_animation(obj_name,anim_name,no_of_frame):
    anim_list=[]
    for i in range(int(no_of_frame)):
        anim_list.append(pygame.image.load('animations/'+obj_name+'/'+anim_name+'/'+anim_name+'_'+str(i)+'.png'))
    animation[anim_name] = anim_list
        
add_animation('sheep','sheep_idle',3)
add_animation('sheep','run',7)
add_animation('player','player_idle',3)
add_animation('player','runup',2)
add_animation('player','rundown',2)
add_animation('player','runleft',3)
add_animation('player','runright',3)

class Trees:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.img_id= random.randint(1,10)
        self.image = pygame.image.load('decor/9.png')
        
    def show(self,display):
        imag_path=str("decor/"+str(self.img_id)+'.png')
        self.image = pygame.image.load(imag_path).convert_alpha()
        self.image.set_colorkey((255,255,255))
        display.blit(pygame.transform.scale(self.image,(192,192)) ,(self.x-scroll_x,self.y-scroll_y))


class Player:
    def __init__(self,x,y,moving_up,moving_down,moving_left,moving_right):
                self.x = 200
                self.y = 100
                self.moving_up = moving_up
                self.moving_down = moving_down
                self.moving_right = moving_right
                self.moving_left = moving_left
                self.current_animation = 'player_idle'
                self.image = animation['player_idle'][0]
                self.frame = 0
                self.camx = 0
                self.camy=0
    def walk(self,scroll_x,scroll_y):        
        if self.moving_right:
            self.x+=1
            self.current_animation='runright'
            self.camx = 1
        
        if self.moving_left:
            self.x-= 1
            self.current_animation='runleft'
            self.camx = -1
          
        if self.moving_down:
            self.y+=1
            self.current_animation='rundown'
            self.camy = 1
            
          
        if self.moving_up:
            self.y-=1
            self.current_animation='runup'
            self.camy = -1
      
             
        if not self.moving_up and not self.moving_down and not self.moving_left and not self.moving_right:
            self.current_animation='player_idle'
            self.camx=self.camy=0
  
    def animate(self,display):
        self.frame+=0.05
        if self.frame>len(animation[self.current_animation]):
            self.frame=0
        self.player_image= animation[self.current_animation][int(self.frame)]
        display.blit(pygame.transform.scale(self.player_image,(128,128)) ,(self.x,self.y))
        

class Sheep:
    def __init__(self):
        self.name = name.randname()
        self.x = random.randint(0,600)
        self.y = random.randint(0,260)
        self.moving_right = False
        self.moving_left = False
        self.flip = name.trueorfalse()
        self.r=0
        self.right_or_left = 0
        self.current_animation = 'sheep_idle'
        self.image = animation['sheep_idle'][0]
        self.frame = 0
    def walk(self):
        self.r+=1
        if self.r==200:
            self.right_or_left =random.randint(-10,10)
            self.r=0
        
        if self.right_or_left <= -8:
            self.moving_left = True
            self.moving_right = False    
        
        if self.right_or_left >= 8:
            self.moving_left = False
            self.moving_right = True
        
        elif -8<self.right_or_left<8:
            self.moving_right = False
            self.moving_left = False
            
    
        if self.moving_right:
            self.x+=vel_x
            self.current_animation='run'
            self.flip=False
            
        if self.moving_left:
            self.x-=vel_x
            self.current_animation='run'
            self.flip=True
             
        if not self.moving_left and not self.moving_right:
            self.current_animation='sheep_idle'
            
            
    def animate(self,display):
        self.frame+=0.05
        if self.frame>len(animation[self.current_animation]):
            self.frame=0
        self.sheep_image= animation[self.current_animation][int(self.frame)]
        display.blit(pygame.transform.scale(pygame.transform.flip(self.sheep_image,sheep.flip,False),(64,64)), (self.x-scroll_x,self.y-scroll_y))
        display.blit(write.render(self.name,False,(0,0,0)),(self.x+50-scroll_x,self.y+10-scroll_y))

for s in range(5):
    sheep = Sheep()
    sheeps.append(sheep)
    
player = Player(x,y,moving_up,moving_down,moving_left,moving_right)

for y in range(5):
    for x in range(6):
        tree = Trees(x*192,y*192)
        object_list.append(tree)


while True:
    
    display.fill((25,204,0))
    scroll_x+=player.camx
    scroll_y+=player.camy
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_UP:
                player.moving_up = True
            if event.key == pygame.K_DOWN:
                player.moving_down = True
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.moving_up = False
            if event.key == pygame.K_DOWN:
                player.moving_down = False
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
            
    for o in object_list:
        o.show(display)
    for sheep in sheeps:
        sheep.walk()
        sheep.animate(display)
    player.walk(scroll_x,scroll_y)
    player.animate(display)

    screen.blit(pygame.transform.scale(display,window),(0,0))
    
    pygame.display.update()
            
