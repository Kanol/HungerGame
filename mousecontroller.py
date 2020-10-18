import math

import pygame


class MouseController:
    def __init__(self, screen, radius, debug=False):
        self.screen = screen
        self.screen_center = screen.get_rect().center
        self.radius = radius
        self.debug = debug

    def update_mouse_pos(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.get_distance(mouse_pos, self.screen_center) > self.radius:
            angle = self.get_angle(mouse_pos, self.screen_center)
            pygame.mouse.set_pos(self.get_end_coords(angle, self.radius))

    def get_distance(self, p1, p2):
        return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    def get_end_coords(self, angle, length):
        return self.screen_center[0] -int(math.cos(angle) * length) ,  self.screen_center[1] - int(math.sin(angle) * length)

    def get_angle(self, p1, p2):
        return math.atan2(p2[1] - p1[1], p2[0] - p1[0])

