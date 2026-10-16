import pygame

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
rectangulo = pygame.Rect(380, 280, 40, 40)

velocidad_normal = 5
velocidad_rapida = 15

ejecutando = True
reloj = pygame.time.Clock()

while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                ejecutando = False

    teclas = pygame.key.get_pressed()

    # Detectar si Ctrl y Shift están presionados 
    ctrl_presionado = teclas[pygame.K_LCTRL] or teclas[pygame.K_RCTRL]
    shift_presionado = teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]

    if ctrl_presionado and shift_presionado:
        velocidad = velocidad_rapida
    else:
        velocidad = velocidad_normal

    if teclas[pygame.K_RIGHT]:
        rectangulo.x += velocidad
    if teclas[pygame.K_LEFT]:
        rectangulo.x -= velocidad
    if teclas[pygame.K_UP]:
        rectangulo.y -= velocidad
    if teclas[pygame.K_DOWN]:
        rectangulo.y += velocidad

    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, (255, 0, 0), rectangulo)
    pygame.display.update()

    reloj.tick(60)  

pygame.quit()