# Day 66 of 100 days of coding challenge
# Program to show name of a person using pygame

import pygame
name = input("Enter your name : ")
pygame.init()
clr = (0,0,0)
w = len(name) * 270 + 100
win = pygame.display.set_mode((w,300))

# set the pygame window name
pygame.display.set_caption('My Name')
t = {}

t['a'] = pygame.image.load('A4.jpg')
t['b'] = pygame.image.load('B.jpg')
t['c'] = pygame.image.load('C.jpg')
t['d'] = pygame.image.load('D.jpg')
t['e'] = pygame.image.load('E.jpg')
t['f'] = pygame.image.load('F.jpg')
t['g'] = pygame.image.load('G.jpg')
t['h'] = pygame.image.load('H.jpg')
t['i'] = pygame.image.load('I4.png')
t['j'] = pygame.image.load('J4.png')
t['k'] = pygame.image.load('K.jpg')
t['l'] = pygame.image.load('L.jpg')
t['m'] = pygame.image.load('M.jpg')
t['n'] = pygame.image.load('N.jpg')
t['o'] = pygame.image.load('O.jpg')
t['p'] = pygame.image.load('P.png')
t['q'] = pygame.image.load('q.png')
t['r'] = pygame.image.load('R.png')
t['s'] = pygame.image.load('S.png')
t['t'] = pygame.image.load('T.png')
t['u'] = pygame.image.load('U.png')
t['v'] = pygame.image.load('V.png')
t['w'] = pygame.image.load('W.png')
t['x'] = pygame.image.load('X.png')
t['y'] = pygame.image.load('Y4.jpg')
t['z'] = pygame.image.load('A4.jpg')


img = []
for ch in name.lower():
    img.append(t[ch])

while True:
    win.fill(clr)
    x = 50
    for i in img:
        win.blit(i,(x,50))
        x += 300

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

