import pygame
from pygame import mixer
#import pygame_gui

#making pygame
pygame.init()
mixer.init()
clock=pygame.time.Clock()

#screen of it
Screen_Width=1200
Screen_Height=600
screen = pygame.display.set_mode((Screen_Width,Screen_Height))

base_font=pygame.font.Font(None,32)

#concrete bridge
Concrete_Bridge=[]
distance_Start=0
for i in range(60):
    Concrete=pygame.Rect(distance_Start,450,20,50)
    distance_Start+=20
    Concrete_Bridge.append(Concrete)
# in kg/m3
Concrete_Density=2400

Road_2d_weight=Concrete_Density*50*Screen_Width*5
Total_Weight=0
Bridge_Weight=''

#useless stuff

boom=pygame.image.load("bigboom.png")
boom=pygame.transform.scale(boom,(200,66))

carTemp=pygame.image.load("car.png")
#150 pixels=5meters, 30pixels=1meter
car=pygame.transform.scale(carTemp,(150,66))
CarState="Right"
carX=0
carY=384
carXChange=0
Hitbox=pygame.Rect(carX,570,150,40)


ColorStressHeavy=(255,0,0)
colorStressLight=(0,0,255)

#the amount of support to exist
def beams(support):
    Y=Screen_Width/(support+1)
    return Y

#code to make the beams for it depending on the user
Concrete_Beam=[]
Beam_distance=[]
def build(amount,thickness):
    if len(Concrete_Beam)==amount:
        pass
    else:
        distance=beams(support=amount)
        x=thickness/2

        distance_Start=distance
        for i in range(amount):
            Concrete=pygame.Rect(distance_Start-x,450,thickness,200)
            Beam_distance.append(distance_Start)
            distance_Start+=distance
            Concrete_Beam.append(Concrete)
        return Concrete_Beam,Beam_distance


#asking user input
Beams=''
widthBridge=''
Object_Mass=''

objectInfo='Mass of object'
infoAmt='Amount of beams'
infoWidth='Thickness of beams'

input_object=pygame.Rect(0,40,90,32)
input_bridge=pygame.Rect(200,40,30,32)
input_width_bridge=pygame.Rect(370,40,60,32)

color_active=pygame.Color('lightskyblue3')
color_passive=pygame.Color('gray15')

colorBridgeBox=color_passive

Bridge_Input_Active=False
Bridge_Width_Active=False
Object_Mass_Active=False



#bridge details
amount=0
width_Bridge_Int=0
actual_bridge_size=0

object_Mass_Int=0
weight_object=0
moment=0
force=0
area=0
pressure=0

display_force=''
display_moment=''
display_pressure=''

activity=False
beam_dist=0
totalbeams=0

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
    
    screen.blit(car,(carX,carY))
    Hitbox.center=(carX+70,480)
    pygame.draw.rect(screen,col,Hitbox)
    for ConcreteFloor in Concrete_Bridge:
        if ConcreteFloor.colliderect(Hitbox):
            if pressure>15168:
                pygame.draw.rect(screen,(255,0,0),ConcreteFloor)
            elif pressure<10000 and pressure>8000:
                pygame.draw.rect(screen,(0,0,255),ConcreteFloor)
            else:
                pygame.draw.rect(screen,(0,255,0),ConcreteFloor)
        else:    
            pygame.draw.rect(screen,col,ConcreteFloor)
    

    for event in pygame.event.get():
        #quit game
        if event.type ==pygame.QUIT:
            run=False

        #choose bridge amount
        if event.type==pygame.KEYDOWN:
            if Bridge_Input_Active==True:
                if event.key==pygame.K_BACKSPACE:
                    Beams=Beams[0:-1]

                else:
                    Beams+=event.unicode
                    amount=int(Beams)
        
        #choose bridge thickness
        if event.type==pygame.KEYDOWN:
            if Bridge_Width_Active==True:
                if event.key==pygame.K_BACKSPACE:
                    widthBridge=widthBridge[0:-1]

                else:
                    widthBridge+=event.unicode
                    width_Bridge_Int=float(widthBridge)*30
                    actual_bridge_size=float(widthBridge)

        #object mass
        if event.type==pygame.KEYDOWN:
            if Object_Mass_Active==True:
                if event.key==pygame.K_BACKSPACE:
                    Object_Mass=Object_Mass[0:-1]

                else:
                    Object_Mass+=event.unicode
                    object_Mass_Int=float(Object_Mass)
                    weight_object=object_Mass_Int*9.81
                    display_force=str(weight_object)
                    
        

    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            carXChange=5
            if carX>=1050:
                screen.blit(boom,(carX,carY))
                pygame.draw.rect(screen,col,Hitbox)
                run=False

        if event.key==pygame.K_LEFT:
            carXChange=-5

    
    if event.type==pygame.KEYUP:
        carXChange=0  
        playAmount=0 


    #select box input
    if event.type==pygame.MOUSEBUTTONDOWN:
        if input_bridge.collidepoint(event.pos):
            Bridge_Input_Active=True
        else:
            Bridge_Input_Active=False
        
        if input_width_bridge.collidepoint(event.pos):
            Bridge_Width_Active=True
        else:
            Bridge_Width_Active=False

        if input_object.collidepoint(event.pos):
            Object_Mass_Active=True
        else:
            Object_Mass_Active=False


    #enter object weigth
    text_info_object=base_font.render(objectInfo,True,(0,0,0))
    screen.blit(text_info_object,(0,0))
    pygame.draw.rect(screen,colorBridgeBox,input_object)
    text_object=base_font.render(Object_Mass+'kg',True,(255,255,255))
    screen.blit(text_object,(0,40))


    #enter bridge amount
    text_info_amount=base_font.render(infoAmt,True,(0,0,0))
    screen.blit(text_info_amount,(170,0))
    pygame.draw.rect(screen,colorBridgeBox,input_bridge)
    text_amount=base_font.render(Beams,True,(255,255,255))
    screen.blit(text_amount,(200,40))


    #enter bridge width
    text_info_width=base_font.render(infoWidth,True,(0,0,0))
    screen.blit(text_info_width,(370,0))
    pygame.draw.rect(screen,colorBridgeBox,input_width_bridge)
    text_width=base_font.render(widthBridge+'m',True,(255,255,255))
    screen.blit(text_width,(370,40))
    
    #total bridge mass
    

    
    for ConcreteSupport in Concrete_Beam:
        if ConcreteSupport.colliderect(Hitbox):
            if pressure>15168:
                pygame.draw.rect(screen,(255,0,0),ConcreteSupport)
            elif pressure<10000 and pressure>8000:
                pygame.draw.rect(screen,(0,0,255),ConcreteSupport)
            else:
                pygame.draw.rect(screen,(0,255,0),ConcreteSupport)
        else:    
            pygame.draw.rect(screen,col,ConcreteSupport)
    if Beams=='':
        Concrete_Beam=[]
        totalbeams=0
        Beam_distance=[]
        Total_Weight=Road_2d_weight
        Bridge_Weight=str(Total_Weight)
        activity=False
    else:
        Total_Weight=Road_2d_weight+(3.3*actual_bridge_size*amount*5*Concrete_Density) #5 is width of bridge
        Bridge_Weight=str(Total_Weight)


    build(amount,width_Bridge_Int)
    
    Text_bridge_mass=base_font.render("Bridge weight:"+Bridge_Weight+"kg",True,(0,0,0))
    screen.blit(Text_bridge_mass,(700,0))

    Text_Force_Object=base_font.render("Object Weight:"+display_force+"N",True,(0,0,0))
    screen.blit(Text_Force_Object,(700,40))

    
    
    if activity==False:
        for obstacles in Beam_distance:
            if carX<=obstacles:
                totalbeams+=1
        activity=True
    
    if amount!=0 and actual_bridge_size!=0:
        currentBeam=len(Beam_distance)-totalbeams
        
        dist=carX-Beam_distance[currentBeam-1]
        moment=dist*weight_object
        if moment<0:
            moment=moment*-1
            moment=int(moment)
            force=moment/1000
        display_moment=str(moment)
        

    Text_moment_Object=base_font.render("Moment to pillar:"+display_moment+"Nm",True,(0,0,0))
    screen.blit(Text_moment_Object,(700,80))

    #compression
    area=5*actual_bridge_size
    if area!=0:
        pressure=force/area
        display_pressure=str(pressure)
    #compressive strength of concrete is 2200 psi or
    if pressure>15168:
        color_pressure=(255,0,0)
    else:
        color_pressure=(0,0,0)
    Text_pressure_Object=base_font.render("Compression:"+display_pressure+"Pa",True,color_pressure)
    screen.blit(Text_pressure_Object,(700,120))


        

    #follows the car of the stress where it is
    carX+=carXChange
    

    
    pygame.display.flip()
    pygame.display.update()

        
