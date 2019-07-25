fondo = "fondomenu.jpg"

import pygame
from pygame.locals import *
from sys import exit

pygame.init()
size=1000, 563
pantalla=pygame.display.set_mode((size),0,32)

#titulo
pygame.display.set_caption("Menu")

#asignar imagenes a una variable
background=pygame.image.load(fondo).convert()

pygame.display.update()

#clases
class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

class Boton(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,x=300,y=450):
        self.imagenNormal = imagen1
        self.imagenSeleccion = imagen2
        self.imagenActual= self.imagenNormal
        self.sonido = pygame.mixer.Sound("grabacion.ogg")
        self.rect = self.imagenActual.get_rect()
        self.rect.left,self.rect.top = (x,y)

    def update(self,pantalla,cursor):
        if cursor.colliderect(self.rect):#si el cursor choca con nuestro rectangulo
            self.imagenActual = self.imagenSeleccion
            if self.continuar:
                self.sonido.play()
                
                self.continuar = False
     
        else:
            self.imagenActual = self.imagenNormal
            self.continuar = True
            

        pantalla.blit(self.imagenActual,self.rect)

img1=pygame.image.load("boton1.png")
img2=pygame.image.load("boton2.png")
boton1=Boton(img1,img2)
cursor1=Cursor()
pygame.mixer.music.set_volume(0.9) #Configuracion del Volumen
pygame.mixer.music.load("fondo.mp3") #Carga de mp3 sonido de fondo
pygame.mixer.music.play(-1, 0.0) #Bucle infinito de reproduccion del sonido


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit()
    pantalla.blit(background,(0,0))
    cursor1.update()
    boton1.update(pantalla,cursor1)
    pygame.display.update()

pygame.quit()


