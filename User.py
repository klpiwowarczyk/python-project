import pygame
import sys

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

    def set_boat(self, x, y, ship_type, direction,screen):
        from Ships import Ships
        # if(nie mozna) return
        ship = Ships()
        ship.make_group_sprites()
        for i in range(1, 5):
            if ship_type == i:
                for j in range(0, i):
                    if direction == "pionowo":
                        self.user_array[x + j][y] = 1
                    elif direction == "poziomo":
                        self.user_array[x][y + j] = 1
                    else:
                        print("Zły kierunek")
        if direction == "pionowo":
            #print(x*30+60)
            ship.display_single_sprite(screen,y*30+60,x*30+100,ship_type)
        if direction == "poziomo":
            #ship.display_single_sprite(screen,y*30+60,x*30+100,ship_type)
            ship.display_rotated_sprite(screen,y*30+60,x*30+100,90,ship_type)

      #  self.user_array[x][y] = 1

    def shot_in_boat_piece(self, x, y):
        if self.user_array[x][y] == 1:
            self.lost_boat_piece(x, y)
        elif self.user_array[x][y] == 0:
            # przeciwnik nie trafił, jakoś to pokazać i przełączyć, że User strzela
            self.user_array[x][y] = 'x'

    def lost_boat_piece(self, x, y):
        self.user_array[x][y] = -1

def main():
    user = User()
    # user.create_user_array()
    # user.print_array_console()
    # user.print_array_console()
    # print('')
    # user.shot_in_boat_piece(4,4)
    # user.shot_in_boat_piece(1,1)
    # user.print_array_console()

main()


