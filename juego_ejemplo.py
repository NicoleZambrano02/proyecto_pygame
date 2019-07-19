fondo = "fondo.png"
tank =  "tanque.png"
block = "bloques.png"
enemy = "tanque2.png"
import pygame
from pygame.locals import*
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
enemigo = pygame.image.load(enemy).convert_alpha()

position = tanque.get_rect()
screen.blit(tanque, position)
pygame.display.update()

#posiciones random
posX = randint(10,400)
posY = randint(10,400)

x = randint(10,400)
y = randint(10,400)

x2 = randint(10,400)
y2 = randint(10,400)

velocidad=10
angulo_rotacion=90


run=True
while run:
        #cargar imagenes 
	screen.blit(background,(0,0))	
	screen.blit(bloque,(posX,posY))	
	screen.blit(tanque,(x,y))
	screen.blit(enemigo, (x2,y2))
        
        
	pygame.time.delay(2)

	n=90

	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == K_LEFT:
				x-=velocidad
			elif event.key == K_RIGHT:
				x+=velocidad
			elif event.key == K_UP:
				y-=velocidad
			elif event.key == K_DOWN:
				y+=velocidad
			#presionar espacio para mover la imagen
			elif event.key == K_SPACE:
				tanque = pygame.transform.rotate(tanque, angulo_rotacion)

			
                
                
	pygame.display.update()
		



#salir
pygame.quit()