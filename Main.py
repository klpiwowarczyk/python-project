import pygame
import sys
from pprint import pprint as pp

pygame.init()

#colors
white = (255,255,255)
black = (0,0,0)


# window size
SCREEN_W = 1200
SCREEN_H = 600


class Board(object):
    """Klasa w której tworzony jest obiekt plansza,
    jest on odświeżany na bazie 2 tablic, które zawierają obraz rozgrywki"""

    def __init__(self):
        self.size_x = 10
        self.size_y = 10
        self.board = []

    def create_board(self):
        """Tworzy pustą planszę"""
        for i in range(self.size_x):
            self.board.append([0 for i in range(self.size_y)])

    def return_board(self):
        """Zwraca planszę"""

        return self.board

    def blit_caption_board(self, nr_pos_x, nr_pos_y, txt_pos_x, txt_pos_y):
        """
        Wyświetla współrzędne tablicy gry

        :param nr_pos_x: pozycja x z której ma zacząć wyświetlać współrzędne cyfr
        :param nr_pos_y: pozycja y z której ma zacząć wyświetlać współrzędne cyfr
        :param txt_pos_x: pozycja x z której ma zacząć wyświetlać współrzędne liter
        :param txt_pos_y: pozycja y z której ma zacząć wyświetlać współrzędne liter

        """
        numbers = [1,2,3,4,5,6,7,8,9,10]
        words = ['A','B','C','D','E','F','G','H','I','J']
        font = pygame.font.SysFont('Arial.ttf',24)
        for i in range(len(numbers)):
            numbers_surface = font.render(str(numbers[i]),1,black)
            text_surface = font.render(str(words[i]),1,black)
            screen.blit(numbers_surface,(nr_pos_x, nr_pos_y))
            screen.blit(text_surface,(txt_pos_x, txt_pos_y))
            nr_pos_y += 30
            txt_pos_x += 30


    def draw_board_player(self):
        """Wyświetla planszę gracza, znajduje się po lewej stronie"""
        pos_x = 60
        pos_y = 100
        distance = 30
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                pygame.draw.aalines(screen, black, False,
                                    [(pos_x, pos_y), (pos_x + distance, pos_y), (pos_x + distance, pos_y + distance),
                                     (pos_x, pos_y + distance), (pos_x, pos_y)])
                pos_x += distance
            pos_x = 60
            pos_y += distance
        self.blit_caption_board(40,108,70,80)

    def draw_board_opponent(self):
        """Wyświetla planszę przeciwnika, znajduje się po prawej stronie"""
        pos_x = 620
        pos_y = 100
        distance = 30
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):

                pygame.draw.aalines(screen, black, False,
                                    [(pos_x, pos_y), (pos_x + distance, pos_y), (pos_x + distance, pos_y + distance),
                                     (pos_x, pos_y + distance), (pos_x, pos_y)])
                pos_x += distance
            pos_x = 620
            pos_y += distance
        self.blit_caption_board(600,108,630,80)

    def update(self):
        pygame.display.update()




if(__name__ == "__main__"):

    screen = pygame.display.set_mode((SCREEN_W,SCREEN_H))
    screen.fill(white)

    board = Board()
    board.create_board()
    board.draw_board_player()
    board.draw_board_opponent()
    board.update()
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.flip()
