import pygame
import random



class Food(pygame.sprite.Sprite):
    def __init__(self, images_dict, selected_key, screensize, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.screensize = screensize
        self.image = images_dict[selected_key]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.bottom = random.randint(20, screensize[0]-20), -10
        self.speed = random.randrange(3, 8)
        self.score = 1
        self.angle = 0
        self.angular_velocity = random.randrange(1, 5)
        self.rotate_ticks = 3
    def rotate(self):
        self.rotate_ticks -= 1
        if self.rotate_ticks == 0:
            self.angle = (self.angle + self.angular_velocity) % 60
            orig_rect = self.image.get_rect()
            rot_image = pygame.transform.rotate(self.image, self.angle)
            rot_rect = orig_rect.copy()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()
            self.image = rot_image
            self.rotate_ticks = 5

    def update(self):
        self.rect.bottom += self.speed
        if self.rect.top > self.screensize[1]:
            return True
        return False