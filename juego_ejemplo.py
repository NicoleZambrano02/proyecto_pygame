fondo = "fondo.png"
tank =  "tanque.png"
block = "bloques.png"
enemy = "tanque2.png"
bala = "bala.png"
boom = "explosion.png"
final ="gameover.png"
import pygame
from pygame.locals import*
import random    
from random import randint

pygame.init()
size=768, 700
screen=pygame.display.set_mode(size)
fuente = pygame.font.SysFont("tahoma", 30)
fuente2 = pygame.font.SysFont("tahoma", 30)
fuente3 = pygame.font.SysFont("tahoma", 30)

#CANTIDAD DE VIDAS
vida =3

#PUNTAJE
puntaje=0

#posiciones random
posX = randint(10,400)
posY = randint(10,400)

x = randint(1,10)
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
rectangulo_enemigo = { }          
enemigosVisibles = { }             
velocidadesX = { }                  
velocidadesY = { }                  

for i in range(0,cantidadEnemigos+1):                      
    rectangulo_enemigo[i] = enemigo.get_rect()     
    rectangulo_enemigo[i].left = random.randrange(50,650) 
    rectangulo_enemigo[i].top = random.randrange(10,301)  
    enemigosVisibles[i] = True                             
    velocidadesX[i] = 1                                     
    velocidadesY[i] = 1   

disparo = pygame.image.load(bala).convert_alpha()
rectanguloDisparo = disparo.get_rect()
rectanguloDisparo2 = disparo.get_rect()
disparoActivo = False
disparoActivo2 = False
jugador = True

explosion = pygame.image.load(boom).convert_alpha()
rectangulo_explosion = explosion.get_rect()
explosionActiva = False

#MUSICA Y SONIDOS
music_fondo =pygame.mixer.Sound("musica_fondo.wav")# REPRODUCIR MUSICA DE FONDO
music_fondo.play(1)

music_shoot = pygame.mixer.Sound("disparo.wav")
music_explode = pygame.mixer.Sound("explosion_tanque.wav")
music_explode.stop()# DETENER SONIDO EXPLOSION

pygame.display.update()


#VARIABLES DE VELOCIDAD Y LIMITES DE MOVIMIENTO
velocidad=10
angulo_rotacion=90

ancho = 768
alto = 450
velocidadX = 1
velocidadY = 1

#ANGULO DE ROTACION
#angulo = pygame.transform.rotate(tanque, 90)

#RELOJ
def tiempo():
	time = int(pygame.time.get_ticks()/1000)
	mensaje = fuente.render('Tiempo transcurrido: '+str(time),True,(255,255,255))
	screen.blit(mensaje,(450,10))

#DISMINUCION DE VIDA POR CONTACTO CON ENEMIGOS
def vidas():
    global vida 
    vida -= 1
    #FIN DEL JUEGO 
    if vida <= 0:
        end = pygame.image.load("gameover.png").convert_alpha()
        screen.blit(end, (300, 300))
    
def disp():
    global music_shoot
    music_shoot.play()
    
def puntajes():
    global puntaje
    puntaje += 10

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
    if keys[K_UP]:
        rectangulo_tanque.top -= 2
    if keys[K_DOWN]:
        rectangulo_tanque.top += 2

    #ROTACION
    if keys[K_LSHIFT] and not disparoActivo2:
        disparoActivo2 = True
        rectanguloDisparo2.left = rectangulo_enemigo[2].left + 18
        rectanguloDisparo2.top = rectangulo_enemigo[2].top + 25
        
    #REALIZAR DISPARO
    if keys[K_SPACE] and not disparoActivo:
        disp()
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
        music_explode.stop()# DETENER SONIDO DE EXPLOSION
        #music_shoot.play() # REPRODUCIR SONIDO DE DISPARO
        rectanguloDisparo.top -= 1
        if rectanguloDisparo.top <= 0:
            disparoActivo = False

    if puntaje == 10:
        music_explode.stop()
        disparoActivo2 = True
        rectanguloDisparo2.left = rectangulo_enemigo[x].left + 18
        rectanguloDisparo2.top = rectangulo_enemigo[x].top - 25

    if disparoActivo2:
        # DETENER SONIDO DE EXPLOSION
        #music_shoot.play() #REPRODUCIR SONIDO DE DISPARO
        rectanguloDisparo2.top -= 1
        if rectanguloDisparo2.top <= 0:
            disparoActivo2 = False

	#COMPROBAR CONTACTO CON LA BALA
    for i in range(0,cantidadEnemigos+1):              
        if enemigosVisibles[i]:                        
            if rectangulo_enemigo[i].colliderect(rectangulo_tanque):
                run = True

            if disparoActivo2:
                if rectanguloDisparo2.colliderect( rectangulo_tanque) :
                    
                     #DETENER SONIDO DE DISPARO
                    music_explode.play() #REPRODUCIR SONIDO DE EXPLOSION
                    screen.blit(explosion, rectangulo_tanque) #IMAGEN DE EXPLOSION
                    jugador = False
                    disparoActivo2 = False
                    vidas()

            if disparoActivo:
                if rectanguloDisparo.colliderect( rectangulo_enemigo[i]) :
                    music_explode.play() #REPRODUCIR SONIDO DE EXPLOSION
                    screen.blit(explosion, rectangulo_enemigo[i]) #IMAGEN DE EXPLOSION
                    enemigosVisibles[i] = False
                    disparoActivo = False
                    puntajes()
                    
 
    cantidadEnemigosVisibles = 0                         
    for i in range(0,cantidadEnemigos+1):                
        if enemigosVisibles[i]:                          
            cantidadEnemigosVisibles = cantidadEnemigosVisibles + 1

    if puntaje == 400:               
        rectangulo=enemigo.get_rect()
        screen.blit(rectangulo, (500,500)) #IMAGEN ENEMIGO

    
                           
 
    # MOSTRAR ELEMENTOS EN LA PANTALLA
    screen.fill( (0,0,0) )
    screen.blit(background,(0,0))
    
    for i in range(0,cantidadEnemigos+1):                
        if enemigosVisibles[i]:
            screen.blit(enemigo, rectangulo_enemigo[i]) #IMAGEN ENEMIGO
    
    if disparoActivo:
        screen.blit(disparo, rectanguloDisparo)# IMAGEN DISPARO
    
    screen.blit(tanque, rectangulo_tanque) # IMAGEN TANQUE

    texto = fuente2.render("Vida: " + str(vida), True, (255, 124, 0))
    screen.blit(texto,(10,10))
    texto2 = fuente3.render("Puntaje: " + str(puntaje), True, (255, 124, 0))
    screen.blit(texto2,(250,10))
    tiempo()  
    
    
    pygame.display.flip()


	


#SALIR
pygame.quit()
