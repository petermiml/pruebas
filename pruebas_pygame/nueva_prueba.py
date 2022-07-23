from turtle import speed
import pygame, sys
pygame.init()

# Definimos constantes.

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 255)

# Definimos variables
# - Posición y velocidad en ambos ejes
pos_x = 400
pos_y = 400
speed_x = 3
speed_y = 3

# Reloj
clock = pygame.time.Clock()

# Definimos tamaño de la pantalla y la construimos

size = (800, 600)
screen = pygame.display.set_mode(size)

# Creamos bucle principal
while True:

    # Creamos for para que nos permita cerrar la ventana del juego.
    # Hará una iteración sobre todos los eventos que toma la funcion "get" y si uno de ellos es el de "cerrar", cerrará el programa.
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Definimos color de fondo de la pantalla.
    screen.fill(WHITE)

    # ================= ZONA DE DIBUJO =====================

    pygame.draw.rect(screen,RED,(pos_x,pos_y,50,50))    # Dibujamos un cuadrado de 50x50 en la posicion de las variables pos_x y pos_y definidas arriba

    
    if pos_x > 750 or pos_x < 0:
        speed_x *= -1

    pos_x += speed_x

    # ======================================================

    pygame.display.flip()
    clock.tick(60)

