import pygame, sys
from funciones_prueba import posicionAleatoria

pygame.init()

# Definir los colores:

WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BROWN = (128,64,0)
BLACK = (0,0,0)

# Definir las coordenadas:

pos_x = 100
pos_y = 200

# Definir la velocidad:
speed_x = 3
speed_y = 3

size = 800,600
screen = pygame.display.set_mode((size))

# Definir el tiempo de refresco:

clock = pygame.time.Clock()

# Vamos a definir una lista de coordenadas antes del bucle principal, donde almacenaremos coordenadas 60 coordenadas aleatorias.

lista_coordenadas = []

for i in range (60):
    lista_coordenadas.append(posicionAleatoria())

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(BLACK)
    
    ''' Con el siguiente FOR, iteramos la lista de las coordenadas que creamos al inicio. Dibujamos un circlo blanco de 2 
        de radio, en la primera coordenada, despues otro en la segunda, etc. Posteriormente, aumentamos en 1 el eje Y de 
        la coordenada que se está iterando (para que de la sensación de estar cayendo)''' 

    for coordenadas in lista_coordenadas:
        pygame.draw.circle(screen,WHITE,coordenadas,2)
        coordenadas[1] += 1
        
        ''' 
        Con el siguiente IF, indicamos que si la posición de la coordenada supera 600 (el bode inferior de la pantalla) en el eje y, 
        se reinicie a 0. Esto es para que de la sensación de que se están generando mas círculos.'''

        if coordenadas[1] > 600:
            coordenadas[1] = 0
        
    pygame.display.flip()
    clock.tick(60)

