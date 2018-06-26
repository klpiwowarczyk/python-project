import pygame
from Ships import Ships

pygame.init()

class User():
    def __init__(self):
        self.size_x = 10
        self.size_y = 10
        self.user_array = []
        self.ship = Ships()
        self.ship.make_group_sprites()
        self.check_array = []
        self.pieces_to_shot = 20

    def create_user_array(self):
        for i in range(self.size_x):
            self.user_array.append([0 for i in range(self.size_y)])

    def create_check_array(self):
        for i in range(self.size_x):
            self.check_array.append([0 for i in range(self.size_y)])



    def print_array_console(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                print(self.user_array[i][j], end=" ")
            print('')
        print("\n")
    def return_array(self):
        return self.user_array

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

        for j in range(ship_type):
            if direction == "pionowo":
                self.user_array[x + j][y] = 1
            elif direction == "poziomo":
                self.user_array[x][y + j] = 1
            else:
                print("Zły kierunek")
        if direction == "pionowo":
            self.ship.display_single_sprite(screen,y*30+60,x*30+100,ship_type)
        if direction == "poziomo":
            self.ship.display_rotated_sprite(screen,y*30+60,x*30+100,90,ship_type)

    def is_it_end(self):
        return self.pieces_to_shot == 0

    def shot_in_boat_piece(self, x, y, enemy_array, screen):

        if enemy_array[y][x] == 1 and self.check_array[y][x] == 0:
            #self.lost_boat_piece(x, y)
            self.ship.display_single_sprite(screen,x*30+780,y*30+100,1)
            self.check_array[y][x] = 1
            self.pieces_to_shot -= 1
            print("lost boat piece")
        elif enemy_array[y][x] == 0 and self.check_array[y][x] == 0:
            # przeciwnik nie trafił, jakoś to pokazać i przełączyć, że User strzela
            self.ship.display_single_sprite(screen,x*30+780,y*30+100,5)
            self.check_array[y][x] = 1
            print("not lost boat piece")
