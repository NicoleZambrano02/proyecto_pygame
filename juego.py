fondo = "fondo.png"
tank =  "tanque.png"
block = "bloques.png"
import pygame
from pygame.locals import *
from random import randint
pygame.init()
size=768, 768
screen=pygame.display.set_mode(size)
fuente = pygame.font.SysFont("tahoma", 30)

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
velocidad = 10

#tiempo en pantalla de juego
def tiempo():
	time = int(pygame.time.get_ticks()/1000)
	mensaje = fuente.render('Tiempo transcurrido: '+str(time),True,(255,255,255))
	screen.blit(mensaje,(300,10))

run=True
while run:
	#cargar imagenes 
	screen.blit(background,(0,0))
	screen.blit(tanque,(x,y))
	screen.blit(bloque,(posX,posY))
	pygame.time.delay(2)
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
		elif event.type == pygame.KEYUP:
			if event.key == K_LEFT:
					print("TECLA IZQUIERDA LIBERADA")
			elif event.key == K_RIGHT:
					print("TECLA DERECHA LIBERADA")
	
	tiempo()
	pygame.display.update()	





#salir
pygame.quit()
