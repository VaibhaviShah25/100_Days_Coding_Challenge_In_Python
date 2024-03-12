# Day 32 of 100 days of coding challenge in Python
# Program for a dice game using GUI
import random
import time
import pygame
p =["","","","","",""]
p[0] = pygame.image.load("d1.png")
p[1] = pygame.image.load("d2.png")
p[2] = pygame.image.load("d3.png")
p[3] = pygame.image.load("d4.png")
p[4] = pygame.image.load("d5.png")
p[5] = pygame.image.load("d6.png")
name1 = input("Enter Player 1 name : ")
name2 = input("Enter Player 2 name : ")
val1 = random.randint(1,6)
val2 = random.randint(1,6)
if val1 > val2:
    text3 = name1 + " Wins"
elif val2 > val1:
    text3 = name2 + " Wins"
else:
    text3 = "It's a DRAW"
pygame.init()
white = (255,255,255)
green = (0,255,0)
blue = (0,0,128)
font = pygame.font.Font('freesansbold.ttf',32)
text1 = font.render(name1,True,green,blue)
text2 = font.render(name2,True,green,blue)
text3 = font.render(text3,True,green,blue)
# Create a rectangular object
textRect1 = text1.get_rect()
textRect2 = text1.get_rect()
textRect3 = text1.get_rect()
# Set the center of the rectangle object.
textRect1.center = (200,100)
textRect2.center = (450,100)
textRect3.center = (350,500)
win = pygame.display.set_mode((700,700)) #Creating window for pygame
while True:
    win.fill("black")
    win.blit(text1,textRect1)
    win.blit(text2,textRect2)
    win.blit(text3,textRect3)
    win.blit(p[val1 - 1],(100,200))
    win.blit(p[val2 - 1], (400, 200))
    time.sleep(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()




