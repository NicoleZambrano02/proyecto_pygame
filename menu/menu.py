fondo = "fondomenu.jpg"
boton1= "boton1.png"
boton2= "boton2.png"
import pygame
from pygame.locals import *
from sys import exit

pygame.init()
size=1000, 563
screen=pygame.display.set_mode((size),0,32)

#titulo
pygame.display.set_caption("Menu")

#asignar imagenes a una variable
background=pygame.image.load(fondo).convert()
btn1 = pygame.image.load(boton1).convert_alpha()


pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
        screen.blit(background,(0,0))
        screen.blit(btn1,(300,450))
        pygame.display.update()

pygame.quit()
