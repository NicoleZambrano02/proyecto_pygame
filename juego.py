fondo = "fondo.png"
tank =  "tanque.png"
block = "bloques.png"
import pygame
from random import randint

pygame.init()
size=768, 768
screen=pygame.display.set_mode(size)

#titulo
pygame.display.set_caption("BATALLA DE TANQUES")

#asignar imagenes a una variable
background=pygame.image.load(fondo).convert()
bloque = pygame.image.load(block).convert_alpha()
tanque = pygame.image.load(tank).convert_alpha()

position = tanque.get_rect()
screen.blit(tanque, position)
pygame.display.update()

#posiciones random
posX = randint(10,400)
posY = randint(10,400)

x = randint(10,400)
y = randint(10,400)

run=True
while run:
        
	pygame.time.delay(2)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
			
                #cargar imagenes 
		screen.blit(background,(0,0))
		screen.blit(tanque,(x,y))
		screen.blit(bloque,(posX,posY))
		pygame.display.update()

#supuesta funcion para mover imagenes
	#for x in range(100):
        #screen.blit(background, position, position)
        #position = position.move(2, 0)
        #screen.blit(tanque, position)
        #pygame.display.update()

pygame.time.delay(100) 






#salir
pygame.quit()
