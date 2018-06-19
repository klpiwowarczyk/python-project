import pygame
import sys

pygame.init()

class User(object):
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

    def set_boat_piece(self, x, y):
        # if(nie mozna) return
        self.user_array[x][y] = 1

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
    user.create_user_array()
    user.print_array_console()
    print('')
    user.set_boat_piece(5,5)
    user.set_boat_piece(4,4)
    user.print_array_console()
    print('')
    user.shot_in_boat_piece(4,4)
    user.shot_in_boat_piece(1,1)
    user.print_array_console()

main()


