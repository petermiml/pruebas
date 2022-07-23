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
GREY = ((150,150,150))

# Definir las coordenadas:

coord_x = 100
coord_y = 100

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

pygame.mouse.set_visible(0)

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.fill(BLACK)
    
    # ============================== AREA DE DIBUJO ===============================
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
        
    ''' Con el método get_pos() de la clase mouse, obtenemos una lista de 2 elementos que será la posición en la que se
        encuentra el mouse. El eje x sería el elemento 0 de la lista y el eje Y sería el elemento 1.'''
    posicion_raton = pygame.mouse.get_pos()
    
    #pygame.draw.rect(screen,WHITE,(posicion_raton[0], posicion_raton[1],100,100))

    ''' Con esto dibujo un triángulo, y jugando con las posiciones del ratón, consigo que se sitúe en donde tengamos situado 
        el mouse.'''

    pygame.draw.polygon(screen, GREY, (((posicion_raton[0]-20),(posicion_raton[1]+40)),((posicion_raton[0]),(posicion_raton[1]-25)),((posicion_raton[0] + 20),(posicion_raton[1]+40)),(posicion_raton[0],posicion_raton[1]+20)), 0)

    # TODO Vamos a intentar que dispare.

    
    pos_x = posicion_raton[0]
    pos_y = posicion_raton[1]

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            speed_x = -3
            coord_x += speed_x

        if event.key == pygame.K_RIGHT:
            speed_x = 3
            coord_x += speed_x

        if event.key == pygame.K_UP:
            speed_y = -3
            coord_y += speed_y

        if event.key == pygame.K_DOWN:
            speed_y = 3
            coord_y += speed_y

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            speed_x = 0


    pygame.draw.polygon(screen, YELLOW, (((coord_x-20),(coord_y+40)),((coord_x),(coord_y-25)),((coord_x + 20),(coord_y+40)),(coord_x,coord_y+20)), 0)
    
    # =============================================================================

    pygame.display.flip()
    clock.tick(100)

