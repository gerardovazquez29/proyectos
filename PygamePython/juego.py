# Pygame

import pygame
import random
import math

# Inicializar Pygame
pygame.init()

# Crear la pantalla
pántalla = pygame.display.set_mode((800, 600))

# Titulo  e icono
pygame.display.set_caption("Invacion Espacial")
icono = pygame.image.load("D:\\programacion\\proyectos\\PygamePython\\ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("D:\\programacion\\proyectos\\PygamePython\\Fondo.jpg")

# variable del Jugador
img_jugador = pygame.image.load("D:\\programacion\\proyectos\\PygamePython\\rocket.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0

# variable del enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("D:\\programacion\\proyectos\\PygamePython\\enemigo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.5)
    enemigo_y_cambio.append(50)


# variable de la bala
img_bala = pygame.image.load("D:\\programacion\\proyectos\\PygamePython\\bala.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 3
bala_visible = False

# puntaje
puntaje = 0


# funcion jugador
def jugador(x,y):
    pántalla.blit(img_jugador, (x, y))

# funcion enemigo
def enemigo(x,y, ene ):
    pántalla.blit(img_enemigo[ene], (x, y))

# funcion disparar bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pántalla.blit(img_bala, (x + 16, y + 10))

# funcion detectar colisiones
def hay_colision(enemigo_x, enemigo_y, bala_x, bala_y):
    distancia = math.sqrt(math.pow(enemigo_x - bala_x, 2) + math.pow(enemigo_y - bala_y, 2))
    if distancia <27:
        return True
    else:
        return False
    
# Loop del juego
se_ejecuta = True
while se_ejecuta:
    # imagen de fondo
    pántalla.blit(fondo,(0,0))
    #pántalla.fill((205,144, 228)) # Color de la pantalla en rgb

    # iterar evento
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:# evento cerrar
            se_ejecuta = False

        # evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 1
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_x = jugador_x
                    disparar_bala(bala_x, bala_y)

        # evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # modifica ubicacion del jugador
    jugador_x += jugador_x_cambio

    # mantiene dentro de los bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modifica ubicacion del enemigo
    for e in range(cantidad_enemigos):
        enemigo_x[e] += enemigo_x_cambio[e]

    # mantiene dentro de los bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 1
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -1  
            enemigo_y[e] += enemigo_y_cambio[e]

        # colisiones
        colision = hay_colision(enemigo_x[e], enemigo_y[e], bala_x, bala_y)
        if colision:
            bala_y = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # movimiento bala
    if bala_y <= -64:
        bala_y = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y -= bala_y_cambio

    jugador(jugador_x, jugador_y)
    pygame.display.update() # actualizar