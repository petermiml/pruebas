import pygame, sys, random
pygame.init()

# Definir colores:

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
BROWN = (128,64,0)

# Coordenadas
cord_x = 400
cord_y = 200

# Velocidad
speed_x = 3
speed_y = 3

size = (800,600)

# Crear ventana
screen = pygame.display.set_mode(size)

# Controlar FPS
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if cord_x > 720 or cord_x < 0:
        speed_x *= -1

    if cord_y > 520 or cord_y <0:
        speed_y *= -1

    cord_x += speed_x
    cord_y += speed_y

    # Poner color de fondo de la pantalla. Tiene que ir antes del area de dibujo, ya que si no, el color de la pantalla tapará el resto
    # al ser dibujado en segundo lugar

    screen.fill(WHITE)

    # ----- Zona de dibujo --------
    
    pygame.draw.rect(screen,RED,[cord_x,cord_y,80,80])
    
    
    

    # Dibuja una linea ( lugar donde se dibujará, color, posición inicial, posición final, grosor de la linea)
    
    
        

    # -----------------------------

    # Hacer que se refresque la pantalla
    pygame.display.flip()
    clock.tick(60)