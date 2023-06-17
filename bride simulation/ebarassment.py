import pygame
from bridgesim import carX, screen

def stress_boxes():
    public:
    CarBox1=pygame.Rect(carX+50,450,10,50)
    CarBox2=pygame.Rect(carX+50,450,10,50)
    CarBox3=pygame.Rect(carX+50,450,10,50)
    CarBox4=pygame.Rect(carX+50,450,10,50)
    CarBox5=pygame.Rect(carX+50,450,10,50)
    CarBox6=pygame.Rect(carX+50,450,10,50)
    CarBox7=pygame.Rect(carX+50,450,10,50)
    CarBox8=pygame.Rect(carX+50,450,10,50)
    CarBox9=pygame.Rect(carX+50,450,10,50)
    CarBox10=pygame.Rect(carX+50,450,10,50)
    CarBox11=pygame.Rect(carX+50,450,10,50)
    CarBox12=pygame.Rect(carX+50,450,10,50)
    CarBox13=pygame.Rect(carX+50,450,10,50)
    CarBox14=pygame.Rect(carX+50,450,10,50)
    CarBox15=pygame.Rect(carX+50,450,10,50)

def showStress():
    pygame.draw.rect(screen,(0,0,255),CarBox1)
    pygame.draw.rect(screen,(39,0, 219),CarBox2)
    pygame.draw.rect(screen,(75,0, 183),CarBox3)
    pygame.draw.rect(screen,(111,0, 147),CarBox4)
    pygame.draw.rect(screen,(147,0, 111),CarBox5)
    pygame.draw.rect(screen,(183,0, 75),CarBox6)
    pygame.draw.rect(screen,(219,0, 39),CarBox7)
    pygame.draw.rect(screen,(255,0, 3),CarBox8)
    pygame.draw.rect(screen,(255,0, 3),CarBox9)
    pygame.draw.rect(screen,(219,0, 39),CarBox10)
    pygame.draw.rect(screen,(147,0, 111),CarBox11)
    pygame.draw.rect(screen,(111,0, 147),CarBox12)
    pygame.draw.rect(screen,(75,0,183),CarBox13)
    pygame.draw.rect(screen,(39,0,219),CarBox14)
    pygame.draw.rect(screen,(0,0,255),CarBox15)