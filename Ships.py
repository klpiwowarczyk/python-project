import pygame
import GameObject
import os

class Ships:
    def __init__(self):
        self.rotated = False
        self.deckers_list = pygame.sprite.RenderUpdates()
        self.single_container = pygame.sprite.GroupSingle()

    def make_sprite(self, img_name):
        ship = GameObject.GameObject(img_name)

        return ship

    def add_to_group(self, ship):
        self.deckers_list.add(ship)

    def display_sprites(self, surface):
        self.deckers_list.draw(surface)

    def display_single_sprite(self,surface, pos_x, pos_y, ship_size):
        """

        :param surface: podajemy nasz screen gry
        :param pos_x:
        :param pos_y:
        :param ship_size:
        :return:
        """
        surface.blit(self.deckers_list.sprites()[ship_size-1].image,(pos_x,pos_y))

    def update_sprites(self):
        self.deckers_list.update()

    def display_rotated_sprite(self, screen, x, y, angle, ship_size):
        count = 1
        for i in self.deckers_list:
            if count == 4:
                i.image = pygame.transform.rotate(i.image,angle)
                self.display_single_sprite(screen, x, y, ship_size)
                i.image = pygame.transform.rotate(i.image,angle)
            count+=1


    def make_group_sprites(self):
        ship1 = self.make_sprite("ship1x1.png")
        self.add_to_group(ship1)

        ship2 = self.make_sprite("ship2x2.png")
        self.add_to_group(ship2)

        ship3 = self.make_sprite("ship3x3.png")
        self.add_to_group(ship3)

        ship4 = self.make_sprite("ship4x4.png")
        self.add_to_group(ship4)


