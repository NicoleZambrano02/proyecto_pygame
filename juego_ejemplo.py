fondo = "fondo.png"
tank =  "tanque.png"
block = "bloques.png"
enemy = "tanque2.png"
bala = "bala.png"
boom = "explosion.png"
import pygame
from pygame.locals import*
import random    
from random import randint

pygame.init()
size=768, 700
screen=pygame.display.set_mode(size)
fuente = pygame.font.SysFont("tahoma", 30)

#CANTIDAD DE VIDAS
vida =3

#PUNTAJE
puntaje=0

#posiciones random
posX = randint(10,400)
posY = randint(10,400)

x = randint(10,400)
y = randint(10,400)

x2 = randint(10,400)
y2 = randint(10,400)

cantidadEnemigos = 10

#TITULO
pygame.display.set_caption("BATALLA DE TANQUES")

#CREACION DE RECTANGULOS PARA LAS IMAGENES
background=pygame.image.load(fondo).convert_alpha()
bloque = pygame.image.load(block).convert_alpha()
rectangulo_bloque = bloque.get_rect()

tanque = pygame.image.load(tank).convert_alpha()
rectangulo_tanque=tanque.get_rect()
rectangulo_tanque.left = 350
rectangulo_tanque.top = 650


enemigo = pygame.image.load(enemy).convert_alpha()
rectangulo_enemigo = { }          # Nuevo en 0.07
enemigosVisibles = { }             # Nuevo en 0.07
velocidadesX = { }                  # Nuevo en 0.07
velocidadesY = { }                  # Nuevo en 0.07

for i in range(0,cantidadEnemigos+1):                      # Nuevo en 0.07
    rectangulo_enemigo[i] = enemigo.get_rect()     # Nuevo en 0.07
    rectangulo_enemigo[i].left = random.randrange(50,650) # Nuevo en 0.07
    rectangulo_enemigo[i].top = random.randrange(10,301)  # Nuevo en 0.07
    enemigosVisibles[i] = True                             # Nuevo en 0.07
    velocidadesX[i] = 1                                     # Nuevo en 0.07
    velocidadesY[i] = 1   

disparo = pygame.image.load(bala).convert_alpha()
rectanguloDisparo = disparo.get_rect()
disparoActivo = False
jugador = True

explosion = pygame.image.load(boom).convert_alpha()
rectangulo_explosion = explosion.get_rect()
explosionActiva = False

#MUSICA Y SONIDOS
music_fondo =pygame.mixer.Sound("musica_fondo.wav")
music_fondo.play(1)

music_shoot = pygame.mixer.Sound("disparo.wav")
music_explode = pygame.mixer.Sound("explosion_tanque.wav")


pygame.display.update()


#VARIABLES DE VELOCIDAD Y LIMITES DE MOVIMIENTO
velocidad=10
angulo_rotacion=90

ancho = 768
alto = 700
velocidadX = 1
velocidadY = 1

#RELOJ
def tiempo():
	time = int(pygame.time.get_ticks()/1000)
	mensaje = fuente.render('Tiempo transcurrido: '+str(time),True,(255,255,255))
	screen.blit(mensaje,(300,10))

def vida():
	vida = 3
	mensaje = fuente.render('VIDAS: '+str(vida),True,(255,255,255))


run=True
while run:

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    
    #MOVIMIENTO DEL JUGADOR        
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        rectangulo_tanque.left -= 2
    if keys[K_RIGHT]:
        rectangulo_tanque.left += 2

    #REALIZAR DISPARO
    if keys[K_SPACE] and not disparoActivo:
        disparoActivo = True
        rectanguloDisparo.left = rectangulo_tanque.left + 18
        rectanguloDisparo.top = rectangulo_tanque.top - 25

    #ACTUALIZAR ESTADO
    for i in range(0,cantidadEnemigos+1):               
        rectangulo_enemigo[i].left += velocidadesX[i]  
        rectangulo_enemigo[i].top += velocidadesY[i]
        if rectangulo_enemigo[i].left < 0 or rectangulo_enemigo[i].right > ancho:
            velocidadesX[i] = -velocidadesX[i]
        if rectangulo_enemigo[i].top < 0 or rectangulo_enemigo[i].bottom > alto:
            velocidadesY[i] = -velocidadesY[i]
 	
 	#AVANCE DE DISPARO
    if disparoActivo:
        music_explode.stop()
        music_shoot.play(1)
        rectanguloDisparo.top -= 1
        if rectanguloDisparo.top <= 0:
            disparoActivo = False

	#COMPROBAR CONTACTO CON LA BALA
    for i in range(0,cantidadEnemigos+1):              
        if enemigosVisibles[i]:                        
            if rectangulo_tanque.colliderect( rectangulo_enemigo[i] ):
                run = True
 
            if disparoActivo:
                if rectanguloDisparo.colliderect( rectangulo_enemigo[i]) :
                    music_shoot.stop()
                    music_explode.play(1)
                    screen.blit(explosion, rectangulo_enemigo[i])
                    enemigosVisibles[i] = False
                    disparoActivo = False
                    
 
    cantidadEnemigosVisibles = 0                         
    for i in range(0,cantidadEnemigos+1):                
        if enemigosVisibles[i]:                          
            cantidadEnemigosVisibles = cantidadEnemigosVisibles + 1

    if puntaje == 30:
        screen.blit(enemigo, rectangulo_enemigo)

    #FIN DEL JUEGO 
    if vida == 0:
        screen.blit(pygame.image.load("gameover.png"), (300, 300))
                           
 
    # MOSTRAR ELEMENTOS EN LA PANTALLA
    screen.fill( (0,0,0) )
    screen.blit(background,(0,0))
    
    for i in range(0,cantidadEnemigos+1):                
        if enemigosVisibles[i]:
            screen.blit(enemigo, rectangulo_enemigo[i]) #IMAGEN ENEMIGO
    
    if disparoActivo:
        screen.blit(disparo, rectanguloDisparo)# IMAGEN DISPARO
    
    screen.blit(tanque, rectangulo_tanque)	
    screen.blit(bloque,(posX,posY))
    tiempo()  
    vida()
    pygame.display.flip()


	


#SALIR
pygame.quit()
