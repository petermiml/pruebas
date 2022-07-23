import pygame, sys, random
from funciones_prueba import colorAleatorio, posicionAleatoria
pygame.init()

# Definir colores:

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BROWN = (128,64,0)

size = (800,600)

screen = pygame.display.set_mode(size)


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    # Poner color de fondo de la pantalla. Tiene que ir antes del area de dibujo, ya que si no, el color de la pantalla tapará el resto
    # al ser dibujado en segundo lugar
    screen.fill(WHITE)

    # ----- Zona de dibujo --------
    pygame.draw.rect(screen,BLUE,[0,0,800,400])
    pygame.draw.rect(screen,GREEN,[0,400,800,600])
    pygame.draw.circle(screen,YELLOW,[100,100],50)

    for i in range(20,780,80):                                  
        pygame.draw.line(screen, BROWN, [i,460], [i,300], 10)       # Dibuja una linea varias veces

    # Dibuja una linea ( lugar donde se dibujará, color, posición inicial, posición final, grosor de la linea)
    
    
        

    # -----------------------------

    # Hacer que se refresque la pantalla
    pygame.display.flip()