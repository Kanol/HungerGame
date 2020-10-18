import pygame
import ctypes
import os
import mousecontroller
import Player
import math
# ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_WINDOW_POS'] = "0, 0"
pygame.init()
user32 = ctypes.windll.user32
screenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
screen = pygame.display.set_mode(screenSize, pygame.NOFRAME)
FPS = 240
FIELD_SIZE = (4000, 4000)
BACKGROUND_TEXTURE = pygame.image.load("images/floor_background.jpg").convert()
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



display_info = pygame.display.Info()
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 28)
game = True

screen_center = screen.get_rect().center
pygame.mouse.set_pos(screen_center)
background_x = int((screen.get_width() - FIELD_SIZE[0]) / 2)
background_y = int((screen.get_height() - FIELD_SIZE[1]) / 2)
controller = mousecontroller.MouseController(screen, 50)
player = Player.Player(200)
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            game = False
    mouse_pos = pygame.mouse.get_pos()


    controller.update_mouse_pos()
    if controller.get_distance(mouse_pos, screen_center) > 20:
        background_x -= (mouse_pos[0] - screen_center[0]) // 3
        background_y -= (mouse_pos[1] - screen_center[1]) // 3
    screen.fill((255, 255, 255))
    fps_data = font.render("FPS: " + str(int(clock.get_fps())), True, (0, 0, 0))
    screen.blit(BACKGROUND, (background_x, background_y))
    angle = -math.degrees(controller.get_angle(screen_center, mouse_pos)) - 90
    player_rotated = pygame.transform.rotate(player.sprite, angle)
    player_rotated_rect = player_rotated.get_rect(center=screen_center)
    screen.blit(player_rotated, player_rotated_rect)
    #pygame.draw.circle(screen, (255, 0, 0), screen_center, 50, 1)
    pygame.draw.circle(screen, (0, 255, 0), screen_center, 20, 1)
    screen.blit(fps_data, (10, 10))
    pygame.display.update()
    clock.tick(FPS)
