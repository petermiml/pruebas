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

# Defino posicion_sol

pos_x = 100
pos_y = 100

# Defino la velocidad

vel_x = 10
vel_y = 10

# Tamaño de la pantalla
size = (800,600)
# Creamos la pantalla
screen = pygame.display.set_mode(size)

# Creamos objeto que controla el refresco del reloj.
clock = pygame.time.Clock()


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    if event.type == pygame.KEYUP:

        if pos_x > 720 or pos_x < 0:
            vel_x *= -1

        if pos_y > 520 or pos_y < 0:
            vel_y *= -1

        pos_x += vel_x
        pos_y += vel_y




    # Poner color de fondo de la pantalla. Tiene que ir antes del area de dibujo, ya que si no, el color de la pantalla tapará el resto
    # al ser dibujado en segundo lugar
    screen.fill(WHITE)

    # ----- Zona de dibujo --------

    # Dibuja una linea ( lugar donde se dibujará, color, posición inicial, posición final, grosor de la linea)
    colorLine = colorAleatorio()
    pygame.draw.line(screen, BLACK, [50,50], [500,500], 10)
    
    pygame.draw.rect(screen,BLUE,[0,0,800,400])
    pygame.draw.rect(screen,GREEN,[0,400,800,600])  # Empieza en la posicion 0,400 y es de tamaño 800x600
    
    
    pygame.draw.circle(screen,YELLOW,[pos_x,pos_y],50)

    # -----------------------------

    # Hacer que se refresque la pantalla
    pygame.display.flip()
    clock.tick(60)