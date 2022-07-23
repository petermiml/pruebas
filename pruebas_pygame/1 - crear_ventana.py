import pygame, sys
pygame.init()       # Inicializamos la librería

size = (800, 500)   # Creamos una tupla con los valores que queramos que tenga el tamaño de nuestra ventana

# Creamos la ventana
screen = pygame.display.set_mode(size)



# Creamos el bucle infinito principal.
while True:
    for event in pygame.event.get():    # Con este for, lo que hacemos es registrar/identificar todo lo que sucede en la ventana
        if event.type == pygame.QUIT:   # Y si yo pulso el botón de "cerrar" que se cierre la ventana sin dar ningún error.
            sys.exit()
        
        print(event)
