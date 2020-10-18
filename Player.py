import pygame


class Player:
    def __init__(self, size = 100):
        self.spritesheet = pygame.image.load("images/robotic cleaner spritesheet.png").convert_alpha()
        self.sprites = []
        self.sprites.append(self.get_image(0, 0, 881, 881))
        self.sprites.append(self.get_image(881, 0, 881, 881))
        self.sprites.append(self.get_image(0, 881, 881, 881))
        self.sprites.append(self.get_image(881, 881, 881, 881))
        self.current = 0
        self.size = size

    def get_image(self, x, y, width, height):
        """ Берем одно изображение из большой таблицы
            Переходим в точку (х, у) - местоположение спрайта
        """

        # Создаем новое пустое изображение, указываемм для него попиксельную прозрачность:
        image = pygame.Surface([width, height], pygame.SRCALPHA).convert_alpha()

        # Копируем спрайт с большого листа на меньшее изображение image
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))

        # Возвращаем изображение
        return image

    @property
    def sprite(self):
        self.current = (self.current + 1) % len(self.sprites)
        self.current_sprite = pygame.transform.scale(self.sprites[self.current], (self.size, self.size))
        return self.current_sprite

    @property
    def center(self):
        return self.current_sprite.get_rect().center


