import pygame
import ctypes
import os
#ctypes.windll.user32.SetProcessDPIAware()
FPS = 60
FIELD_SIZE = (4000, 4000)
BACKGROUND_TEXTURE = pygame.image.load("images/floor_background.jpg")
BACKGROUND = pygame.Surface(FIELD_SIZE)
MOVE_SPEED = 5
x = 0
y = 0
while y < FIELD_SIZE[1]:
    while x < FIELD_SIZE[0]:
        BACKGROUND.blit(BACKGROUND_TEXTURE, (x, y))
        x += BACKGROUND_TEXTURE.get_width()
    x = 0
    y += BACKGROUND_TEXTURE.get_height()

os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"
pygame.init()
display_info = pygame.display.Info()
clock = pygame.time.Clock()

game = True
user32 = ctypes.windll.user32
screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
screen = pygame.display.set_mode(screenSize, pygame.NOFRAME)
screen_center = (int (screen.get_width () / 2), int (screen.get_height () / 2))
pygame.mouse.set_pos(screen_center)
background_x = int((screen.get_width() - FIELD_SIZE[0]) / 2)
background_y = int((screen.get_height() - FIELD_SIZE[1]) / 2)

while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game = False
    mouse_pos = pygame.mouse.get_pos()
    background_x -= mouse_pos[0] - screen_center[0]
    background_y -= mouse_pos[1] - screen_center[1]
    screen.fill((255, 255, 255))
    screen.blit (BACKGROUND, (background_x, background_y))
    pygame.draw.circle (screen, (255, 0, 0), screen_center, 50, 1)

    pygame.display.update ()
    clock.tick(FPS)