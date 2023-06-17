import pygame
from pygame import mixer
import pygame_gui

#making pygame
pygame.init()
mixer.init()
clock=pygame.time.Clock()

#screen of it
Screen_Width=1200
Screen_Height=600
screen = pygame.display.set_mode((Screen_Width,Screen_Height))


#concrete bridge
Concrete_Bridge=[]
distance_Start=0
for i in range(60):
    Concrete=pygame.Rect(distance_Start,450,20,50)
    distance_Start+=20
    Concrete_Bridge.append(Concrete)
# in kg/m3
Concrete_Density=2400

#useless stuff
Ignore=pygame.image.load("EasterEgg.jpg")
Ignore=pygame.transform.scale(Ignore,(1200,650))
boom=pygame.mixer.Sound('SFX1.mp3')
playAmount=0
boom=pygame.image.load("bigboom.png")
boom=pygame.transform.scale(boom,(200,66))

carTemp=pygame.image.load("car.png")
#150 pixels=5meters, 30pixels=1meter
car=pygame.transform.scale(carTemp,(150,66))
CarState="Right"
carX=0
carY=384
carXChange=0

#the stress within the bridge, not good yet

CarBox1=pygame.Rect(carX,450,30,50)
CarBox2=pygame.Rect(carX+30,450,30,50)
CarBox3=pygame.Rect(carX+60,450,30,50)
CarBox4=pygame.Rect(carX+90,450,30,50)
CarBox5=pygame.Rect(carX+120,450,30,50)
#kilograms
weight_Car=1111
ColorStressHeavy=(255,0,0)
colorStressLight=(0,0,255)

#the amount of support to exist
def beams(support):
    Y=Screen_Width/(support+1)
    return Y

#code to make the beams for it depending on the user
Concrete_Beam=[]
def build(amount,thickness):
    distance=beams(support=amount)
    x=thickness/2

    distance_Start=distance
    for i in range(amount):
        Concrete=pygame.Rect(distance_Start-x,450,thickness,200)
        distance_Start+=distance
        Concrete_Beam.append(Concrete)
    return Concrete_Beam







run=True
#running the screen
while run:

    #running in 60fps
    screen.fill((255,255,255))
    clock.tick(120)
    UI_REFRESH_RATE=clock.tick(60)/1000

    #pos=pygame.mouse.get_pos()
    #Concrete.center=pos
    col=(128,128,128)
    coleg=(0,0,0)
    for ConcreteFloor in Concrete_Bridge:
        pygame.draw.rect(screen,col,ConcreteFloor)
    
    build(8,80)
    for ConcreteSupport in Concrete_Beam:
        pygame.draw.rect(screen,col,ConcreteSupport)
    
    #building the template for the stress color in the main road
    pygame.draw.rect(screen,(0,0,255),CarBox1)
    pygame.draw.rect(screen,(128,0, 128),CarBox2)
    pygame.draw.rect(screen,(255,0, 0),CarBox3)
    pygame.draw.rect(screen,(128,0, 128),CarBox4)
    pygame.draw.rect(screen,(0,0, 255),CarBox5)

    screen.blit(car,(carX,carY))
    

    for event in pygame.event.get():
        #quit game
        if event.type ==pygame.QUIT:
            run=False

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            carXChange=5
            if carX>=1050:
                screen.blit(boom,(carX,carY))
                run=False

        if event.key==pygame.K_LEFT:
            carXChange=-5
        if event.key==pygame.K_UP:
            screen.blit(Ignore,(0,0))
            if playAmount==0:
                playAmount+=1
                boom.play()
    
    
    if event.type==pygame.KEYUP:
        carXChange=0  
        playAmount=0 
    
    #follows the car of the stress where it is
    carX+=carXChange
    CarBox1=pygame.Rect(carX,450,30,50)
    CarBox2=pygame.Rect(carX+30,450,30,50)
    CarBox3=pygame.Rect(carX+60,450,30,50)
    CarBox4=pygame.Rect(carX+90,450,30,50)
    CarBox5=pygame.Rect(carX+120,450,30,50)

    
    pygame.display.flip()

        