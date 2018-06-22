import pygame
import sys
import threading

pygame.init()



class User():
    def __init__(self):
        self.size_x = 10
        self.size_y = 10
        self.user_array = []

    def create_user_array(self):
        for i in range(self.size_x):
            self.user_array.append([0 for i in range(self.size_y)])

    def print_array_console(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                print(self.user_array[i][j], end=" ")
            print('')

   # def select_boat(self):
        # wybranie rodzaju statku

   # def set_boat(self, x, y):
        # wstawienie calego statku, jakaś wiadomość, że wstawiony cały
    def check_boat_około(self, x, y, ship_type, direction):

        can_be_placed = True

        for size_ship in range(ship_type):
            if direction == "pionowo":
                if x + size_ship < len(self.user_array) and self.user_array[x+size_ship][y] == 0:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= x + size_ship + j < len(self.user_array) and 0 <= y + i < len(self.user_array):
                                if self.user_array[x+size_ship+j][y+i] == 1:
                                    can_be_placed = False
                            else:
                                None
                else:
                    can_be_placed = False

            elif direction == "poziomo":
                if y + size_ship < len(self.user_array) and self.user_array[x][y+size_ship] == 0:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= x + j < len(self.user_array) and 0 <= y + size_ship + i < len(self.user_array):
                                if self.user_array[x+j][y+size_ship+i] == 1:
                                    can_be_placed = False
                            else:
                                None
                else:
                    can_be_placed = False

        return can_be_placed

    def set_boat(self, x, y, ship_type, direction,screen):
        from Ships import Ships
        ship = Ships()
        ship.make_group_sprites()
        for j in range(ship_type):
            if direction == "pionowo":
                self.user_array[x + j][y] = 1
            elif direction == "poziomo":
                self.user_array[x][y + j] = 1
            else:
                print("Zły kierunek")
        if direction == "pionowo":
            ship.display_single_sprite(screen,y*30+60,x*30+100,ship_type)
        if direction == "poziomo":
            ship.display_rotated_sprite(screen,y*30+60,x*30+100,90,ship_type)

    def shot_in_boat_piece(self, x, y):
        if self.user_array[x][y] == 1:
            self.lost_boat_piece(x, y)
        elif self.user_array[x][y] == 0:
            # przeciwnik nie trafił, jakoś to pokazać i przełączyć, że User strzela
            self.user_array[x][y] = 'x'

    def lost_boat_piece(self, x, y):
        self.user_array[x][y] = -1


