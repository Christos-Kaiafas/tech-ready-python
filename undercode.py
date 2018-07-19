# import pygame module
import pygame

pygame.init()
#This is the code for the first slide. I used the same code for each one
#I created it as a function so i could easily activate it
def intro1():
#This line creates the screen and its dimensions
    screen = pygame.display.set_mode((900, 800))
#This gives you the foundation for text. You can choose the size and font
    font = pygame.font.SysFont('comic sans', 42)
#This is the text for the first slide, the numbers at the end code for white, the text color
    text = font.render("Long ago, two races ruled over Earth: Humans and Monsters", True, (255, 255, 255))
#This chooses the image that will be displayed onscreen
    intro_1 = pygame.image.load("undertale_intro_1.jpg")
#This changes the size of the image without distorting it  
    intro_1=pygame.transform.scale(intro_1, (800,600))

    intro_1rect = intro_1.get_rect()

    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
#This is the code to set the background as black
        screen.fill( (0, 0, 0) )
#This changes the position of the text with (x,y) being co-ordinates on the screen    
        screen.blit(text, (30, 675))
#This chnages the position of the image      
        screen.blit(intro_1,(50, 0))
#This updates the screen
        pygame.display.flip()
#This line stalls the computer so that it cannot perform any functions for (x) amount of milliseconds
        pygame.time.wait(5000)
#This stops the code from runnning, which makes the second slide able to be pulled up  
        break

def intro2():
    screen = pygame.display.set_mode((900, 800))


    font = pygame.font.SysFont('comic sans', 42)

    text = font.render("One day war broke out bewtween the two races", True, (255, 255, 255))
    intro_2 = pygame.image.load("undertale_intro_2.jpg")
    intro_2=pygame.transform.scale(intro_2, (800,600))
    intro_2rect = intro_2.get_rect()

    active = True


    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(text, (125, 675))
        screen.blit(intro_2,(50, 0))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

def intro3():
    screen = pygame.display.set_mode((900, 800))


    font = pygame.font.SysFont('comic sans', 42)

    text = font.render("After a long battle, the humans were victorious", True, (255, 255, 255))
    intro_3 = pygame.image.load("undertale_intro_3.jpg")
    intro_3=pygame.transform.scale(intro_3, (800,600))
    intro_3rect = intro_3.get_rect()

    active = True


    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(text, (125, 675))
        screen.blit(intro_3,(50, 0))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

def intro4():
    screen = pygame.display.set_mode((900, 800))


    font = pygame.font.SysFont('comic sans', 42)

    text = font.render("They sealed the monsters underground with a magic spell", True, (255, 255, 255))
    intro_4 = pygame.image.load("undertale_intro_4.jpg")
    intro_4=pygame.transform.scale(intro_4, (800,600))
    intro_4rect = intro_4.get_rect()

    active = True


    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(text, (50, 675))
        screen.blit(intro_4,(50, 0))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

def intro5():
    screen = pygame.display.set_mode((900, 800))

    font = pygame.font.SysFont('comic sans', 100)

    text = font.render("Many years later. . .", True, (255, 255, 255))
    
    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(text, (125, 350))
        pygame.display.flip()
        pygame.time.wait(7000)
        break

def intro6():
    screen = pygame.display.set_mode((900, 800))

    font = pygame.font.SysFont('comic sans', 42)

    text = font.render("Legends say that those who climb Mt. Ebott never return", True, (255, 255, 255))
    intro_6 = pygame.image.load("undertale_intro_6.jpg")
    intro_6=pygame.transform.scale(intro_6, (800,600))
    intro_6rect = intro_6.get_rect()

    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(text, (40, 625))
        screen.blit(intro_6,(50, 0))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

def intro7():
    screen = pygame.display.set_mode((900, 800))

    font = pygame.font.SysFont('comic sans', 42)

    text = font.render("But one human child dares to climb the mountain", True, (255, 255, 255))
    intro_7 = pygame.image.load("undertale_intro_7.jpg")
    intro_7=pygame.transform.scale(intro_7, (800,600))
    intro_7rect = intro_7.get_rect()

    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(text, (125, 675))
        screen.blit(intro_7,(50, 0))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

def intro8():
    screen = pygame.display.set_mode((900, 800))

    font = pygame.font.SysFont('comic sans', 56)

    text = font.render("This is their story", True, (255, 255, 255))
    intro_8 = pygame.image.load("undertale_intro_8.jpg")
    intro_8=pygame.transform.scale(intro_8, (800,600))
    intro_8rect = intro_8.get_rect()

    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(text, (300, 675))
        screen.blit(intro_8,(50, 0))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

def intro9():
    screen = pygame.display.set_mode((900, 800))

    intro_9 = pygame.image.load("undertale_intro_9.jpg")
    intro_9=pygame.transform.scale(intro_9, (800,600))
    intro_9rect = intro_9.get_rect()

    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(intro_9,(50, 0))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

def intro10():
    screen = pygame.display.set_mode((900, 800))

    intro_10 = pygame.image.load("undertale_intro_10.jpg")
    intro_10=pygame.transform.scale(intro_10, (800,600))
    intro_10rect = intro_10.get_rect()

    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(intro_10,(50, 0))
        pygame.display.flip()
        pygame.time.wait(5000)
        break

def Title():
    screen = pygame.display.set_mode((900, 800))
    Undertale = pygame.image.load("Undertale.jpg")
    Undertale=pygame.transform.scale(Undertale, (800,600))
    Undertalerect = Undertale.get_rect()

    active = True

    while active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
    
        screen.fill( (0, 0, 0) )
        screen.blit(Undertale,(50, 0))
        pygame.display.flip()
        pygame.time.wait(8000)
        break
#This brings up a breif description of the game, making it wait a few seconds before starting the actual game
def Description():
    print("A human falls into the underground, filled with many monsters")
    print("They have the choice to show love and compassion, and spare the monsters,")
    print("Or to show no mercy and kill all the monsters.")
    print("Every choice matters in the end.")
    print("Will the fallen child make them friends?")
    print("Or will they give in, kill them all?")
    print("Who knows when an angel will fall...")
#This strings together all slides into one command
def Intro_All():
    intro1()
    intro2()
    intro3()
    intro4()
    intro5()
    intro6()
    intro7()
    intro8()
    intro9()
    intro10()
    Title()
#This brings the description and all the slides into one command
def Intro_full():
    Description()
    pygame.time.wait(8000)
    Intro_All()
Intro_full()


screen = pygame.display.set_mode((900, 800))
    
flowerbed = pygame.image.load("flower_bed.jpg")
flowerbed=pygame.transform.scale(flowerbed, (900,800))
flowerbedrect = flowerbed.get_rect()

frisk = pygame.image.load("frisk.jpg")
frisk=pygame.transform.scale(frisk, (75,100))
friskrect = frisk.get_rect()
frisk_x=400
frisk_y=330
active = True
clock = pygame.time.Clock()

active = True

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
    pressed = pygame.key.get_pressed()
    
    if pressed[pygame.K_UP]:
        frisk_y -= 1
    if pressed[pygame.K_DOWN]:
        frisk_y += 1
    if pressed[pygame.K_LEFT]:
        frisk_x -= 1
    if pressed[pygame.K_RIGHT]:
        frisk_x += 1

    screen.blit(flowerbed, (0, 0))
    screen.blit(frisk, (frisk_x, frisk_y))     
    clock.tick(300)
    pygame.display.flip()

