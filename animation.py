import pygame

# ==== CONSTANTS ====
BLACK = (0, 0, 0)
RED = (255, 0, 0)
RESOLUTION = (400, 600)
FPS = 20
SPEED = 20
RECT_SIZE = (100, 100)
CAPTION = 'Animation'
COORDINATES = {
    pygame.K_LEFT: (-SPEED, 0),
    pygame.K_RIGHT: (SPEED, 0),
    pygame.K_DOWN: (0, SPEED),
    pygame.K_UP: (0, -SPEED)
}
# ===================

clock = pygame.time.Clock()
coords = [0, 0]
motion = None

pygame.init()
surface = pygame.display.set_mode(RESOLUTION)
pygame.display.set_caption(CAPTION)


def move_rect(event):
    for coord in range(2):
        coords[coord] += COORDINATES.get(event.key)[coord]


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            move_rect(event)

    surface.fill(BLACK)
    pygame.draw.rect(surface, RED, (coords[0], coords[1], *RECT_SIZE))
    pygame.display.flip()
    clock.tick(FPS)
