import pygame
pygame.init()

# COLORES
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Constantes de ancho y alto de las paletas de los jugadores
PLAYER_WIDTH = 15
PLAYER_HEIGHT = 90

# Coordenadas y velocidad del jugador 1:

player_1_x_coor = 50
player_1_y_coor = 300 - (PLAYER_HEIGHT/2) # Esto lo dejamos así para que nos lo coloque en la mitad exacta de la pantalla
player_1_speed = 0

# Coordenadas y velocidad del jugador 2:

player_2_x_coor = 740
player_2_y_coor = 300 - (PLAYER_HEIGHT/2)
player_2_speed = 0

# Coordenadas y velocidad de la pelota

ball_x = 400
ball_y = 300
ball_speed_x = 5
ball_speed_y = 5

# CREAR VENTANA

SCREEN_SIZE = (800, 600)
screen = pygame.display.set_mode(SCREEN_SIZE)

# CREAR RELOJ

clock = pygame.time.Clock()

# Crear variable para salir de bucle principal

game_over = False

while not game_over:
    
    # ========================================== EVENTOS ===============================================

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        # ----------------------------------- PRESIONAR TECLAS ----------------------------------------
        
        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w:
                player_1_speed = -10
            if event.key == pygame.K_s:
                player_1_speed = 10
            
            # Jugador 2
            if event.key == pygame.K_UP:
                player_2_speed = -10
            if event.key == pygame.K_DOWN:
                player_2_speed = 10
        
        # ----------------------------------- LEVANTAR TECLAS --------------------------------------------

        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_w:
                player_1_speed = 0
            if event.key == pygame.K_s:
                player_1_speed = 0

            # Player 2
            if event.key == pygame.K_UP:
                player_2_speed = 0
            if event.key == pygame.K_DOWN:
                player_2_speed = 0
    
    # ============================================================================================================

    screen.fill(BLACK)

    # ========================================= ÁREA DE DIBUJO ====================================================

    player_1 = pygame.draw.rect(screen, WHITE, (player_1_x_coor, player_1_y_coor, PLAYER_WIDTH, PLAYER_HEIGHT))
    player_2 = pygame.draw.rect(screen, WHITE, (player_2_x_coor, player_2_y_coor, PLAYER_WIDTH, PLAYER_HEIGHT))
    ball = pygame.draw.circle(screen, WHITE, (ball_x, ball_y), 10)

    # ==============================================================================================================

    # ============================================ COLISIONES ======================================================
    
    if ball.colliderect(player_1) or ball.colliderect(player_2):    # Si la bola colisiona con el player 1 o el 2
        ball_speed_x *= -1                                          # La velocidad de la bola en el eje x se invierta
        
        if ball_speed_x < 0:
            ball_speed_x -= 1
            ball_speed_y -= 1
        else:
            ball_speed_x += 1
            ball_speed_y += 1

    # ==============================================================================================================
    
    # ============================================= MOVIMIENTO JUGADOR 1============================================

    player_1_y_coor += player_1_speed
    
    if player_1_y_coor < 0:
        player_1_y_coor = 0

    if player_1_y_coor > 507:
        player_1_y_coor = 507
        
    # ==============================================================================================================

    # ============================================ MOVIMIENTO JUGADOR 2 ============================================
    player_2_y_coor += player_2_speed

    if player_2_y_coor < 0:
        player_2_y_coor = 0

    if player_2_y_coor > 507:
        player_2_y_coor = 507

    # ==============================================================================================================

    # ============================================== MOVIMIENTO PELOTA =============================================

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y > 590 or ball_y < 10:
        ball_speed_y *= -1

    if ball_x < 10 or ball_x > 790:
        ball_x = 400
        ball_y = 300
        ball_speed_x = 3
        ball_speed_y = 3

    print(ball_speed_y)
    # ==============================================================================================================


    
    #===================================== REFRESCO DE PANTALLA ====================================================
    pygame.display.flip()
    clock.tick(60)

pygame.quit()