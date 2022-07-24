import pygame, sys
from funciones_prueba import posicionAleatoria

''' IDEA PARA FUTURA IMPLEMENTACION: Hacer que cuando aceleras la nave, no pueda decelerar a no ser que use retropropulsores
pero esos retropropulsores gastan combustible.'''

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

coord_x_nave1 = 500
coord_y_nave1 = 300

coord_x_nave2 = 100
coord_y_nave2 = 300


# Definir la velocidad:
speed_x_nave1 = 0
speed_y_nave1 = 0

speed_x_nave2 = 0
speed_y_nave2 = 0

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

        # EVENTOS DE TECLADO (tienen que ir en este punto).
        # Revisar https://www.pygame.org/docs/ref/key.html para ver todas las teclas

        if event.type == pygame.KEYDOWN:        # Si el tipo de evento es de tipo "presionar una tecla"     
            if event.key == pygame.K_LEFT:      # Si la tecla presionada es la flecha de direccion izquierda
                speed_x_nave1 = -3                    # Pone la velocidad a menos tres.
                
            if event.key == pygame.K_RIGHT:
                speed_x_nave1 = 3
                
            if event.key == pygame.K_UP:
                speed_y_nave1 = -3
                
            if event.key == pygame.K_DOWN:
                speed_y_nave1 = 3
                
        if event.type == pygame.KEYUP:          # Si el tipo de evento es de tipo "dejar de presionar una tecla"
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                speed_x_nave1 = 0                     # sea la tecla que sea, la velocidad se iguala a 0
            if event.key == pygame.K_DOWN:
                speed_y_nave1=0
            if event.key == pygame.K_UP:
                speed_y_nave1=0
    
        # Eventos para la nave 2

        if event.type == pygame.KEYDOWN:        # Si el tipo de evento es de tipo "presionar una tecla"     
            if event.key == pygame.K_a:      # Si la tecla presionada es la flecha de direccion izquierda
                speed_x_nave2 = -3                    # Pone la velocidad a menos tres.
                
            if event.key == pygame.K_d:
                speed_x_nave2 = 3
                
            if event.key == pygame.K_w:
                speed_y_nave2 = -3
                
            if event.key == pygame.K_s:
                speed_y_nave2 = 3
                
        if event.type == pygame.KEYUP:          # Si el tipo de evento es de tipo "dejar de presionar una tecla"
            if event.key == pygame.K_a:
                speed_x_nave2 = 0                     
            if event.key == pygame.K_d:
                speed_x_nave2 = 0
            if event.key == pygame.K_s:
                speed_y_nave2 = 0
            if event.key == pygame.K_w:
                speed_y_nave2 = 0

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

    pygame.draw.polygon(screen, YELLOW, (((coord_x_nave1-20),(coord_y_nave1+40)),((coord_x_nave1),(coord_y_nave1-25)),((coord_x_nave1 + 20),(coord_y_nave1+40)),(coord_x_nave1,coord_y_nave1+20)), 0)
    coord_x_nave1 += speed_x_nave1
    coord_y_nave1 += speed_y_nave1

    pygame.draw.polygon(screen, RED, (((coord_x_nave2-20),(coord_y_nave2+40)),((coord_x_nave2),(coord_y_nave2-25)),((coord_x_nave2 + 20),(coord_y_nave2+40)),(coord_x_nave2,coord_y_nave2+20)), 0)
    coord_x_nave2 += speed_x_nave2
    coord_y_nave2 += speed_y_nave2
    # =============================================================================

    pygame.display.flip()
    clock.tick(100)

