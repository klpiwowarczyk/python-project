import sys, os
import pygame
from Ships import Ships

# colors
white = (255, 255, 255)
black = (0, 0, 0)

class GameManagement(object):
    """ Klasa do zarządzania grą, oknem intro oraz oknem gry"""

    def __init__(self):
        global screen
        pygame.init()
        SCREEN_W = 1200
        SCREEN_H = 600
        screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
        self.board = Board()
        self.ships = Ships()
        self.ships.make_group_sprites()

    def game_intro(self):
        """ Funkcja zarządzająca oknem początkowym """
        intro = True
        screen.fill((255, 255, 255))
        self.draw_text("Arial.ttf", 54, black, 440, 50, "Bitwa Morska")
        self.draw_button((100, 100, 100), 490, 250, 150, 50)
        self.draw_text("Arial.ttf", 32, black, 540, 264, "Graj!")
        self.draw_button((100, 100, 100), 490, 350, 150, 50)
        self.draw_text("Arial.ttf", 32, black, 520, 364, "Wyjście!")
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if pygame.mouse.get_pressed() == (1, 0, 0):
                pos_x, pos_y = pygame.mouse.get_pos()
                if self.button_clicked(pos_x, pos_y, 490, 250):
                    if self.button_clicked(pos_x, pos_y, 490, 250):
                        intro = False
                if self.button_clicked(pos_x, pos_y, 490, 350):
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
        self.game_choice()


    def game_choice(self):
        game_choice = True
        screen.fill((255, 255, 255))
        self.draw_text("Arial.ttf", 54, black, 440, 50, "Bitwa Morska")
        self.draw_button((100, 100, 100), 300, 250, 150, 50)
        self.draw_text("Arial.ttf", 32, black, 330, 264, "Hot-Seat!")
        self.draw_button((100, 100, 100), 700, 250, 150, 50)
        self.draw_text("Arial.ttf", 32, black, 717, 262, "Multiplayer!")
        while game_choice:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pos_x, pos_y = pygame.mouse.get_pos()
                    if self.button_clicked(pos_x, pos_y, 300, 250):
                        self.game_section()
                    if self.button_clicked(pos_x, pos_y, 700, 250):
                        self.game_section()
                pygame.display.update()

    def button_clicked(self, pos_x, pos_y, butt_pos_x, butt_pos_y):
        """
        Sprawdza czy klawisz graj bądź wyjście został wciśnięty
        :param pos_x: pozycja x kursora
        :param pos_y: pozycja y kursora
        :param butt_pos_x:
        :param butt_pos_y:
        :return: zwraca czy dany przycisk został wciśnięty
        """
        if butt_pos_x <= pos_x <= butt_pos_x+150 and butt_pos_y <= pos_y <= butt_pos_y+150:
            return True
        return False

    def game_section(self):
        """Funkcja zarządzająca oknem gry"""

        while True:
            x, y = pygame.mouse.get_pos()
            print(pygame.mouse.get_pressed())
            self.board.draw_board_player()
            self.board.draw_board_opponent()
            self.display_sprites()
            for event in pygame.event.get():
                # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #     if self.button_clicked(x,y,200,200):
                #         self.ships.rotate_sprite(screen,90,4)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()
            screen.fill(white)

    def display_sprites(self):
        distance = 100
        for i in range(4):
            self.ships.display_single_sprite(screen, 350+distance,100,1)
            if i < 3:
                self.ships.display_single_sprite(screen, 350+distance,150,2)
            if i < 2:
                self.ships.display_single_sprite(screen, 350+distance,230,3)
            if i < 1:
                self.ships.display_single_sprite(screen, 350+distance,350,4)
            distance += 50



    @staticmethod
    def draw_button(color, pos_x, pos_y, width, height):
        """
        Funkcja tworząca przycisk (bez jego obsługi sam wygląd)
        :param color: kolor przycisku
        :param pos_x: pozycja x, z której zacznie się rysowanie
        :param pos_y: pozycja y, z której zacznie się rysowanie
        :param width: szerokość przycisku
        :param height: wysokość przycisku
        :return:
        """
        pygame.draw.rect(screen, color, (pos_x, pos_y, width, height))

    def draw_text(self, font, font_size, color, pos_x, pos_y, text):
        """
        Funkcja tworząca tekst
        :param font: nazwa czcionki przykład ("Arial.ttf")
        :param font_size: rozmiar czcionki
        :param color: kolor czcionki
        :param pos_x: pozycja x czcionki na ekranie
        :param pos_y: pozycja y czcionki na ekranie
        :param text: tekst, który ma zostać napisany
        :return:
        """
        font = pygame.font.SysFont(font, font_size)
        text_surface = font.render(text, 1, color)
        screen.blit(text_surface, (pos_x, pos_y))

class Board(object):
    """Klasa w której tworzony jest obiekt plansza,
    jest on odświeżany na bazie 2 tablic, które zawierają obraz rozgrywki"""

    def __init__(self):
        global screen
        self.size_x = 10
        self.size_y = 10
        self.board = []
        self.create_board()

    def create_board(self):
        """Tworzy pustą planszę"""
        for i in range(self.size_x):
            self.board.append([0 for i in range(self.size_y)])

    def return_board(self):
        """Zwraca planszę"""

        return self.board

    @staticmethod
    def blit_caption_board(nr_pos_x, nr_pos_y, txt_pos_x, txt_pos_y):
        """
        Wyświetla współrzędne tablicy gry

        :param nr_pos_x: pozycja x z której ma zacząć wyświetlać współrzędne cyfr
        :param nr_pos_y: pozycja y z której ma zacząć wyświetlać współrzędne cyfr
        :param txt_pos_x: pozycja x z której ma zacząć wyświetlać współrzędne liter
        :param txt_pos_y: pozycja y z której ma zacząć wyświetlać współrzędne liter

        """
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        words = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        font = pygame.font.SysFont('Arial.ttf', 24)
        for i in range(len(numbers)):
            numbers_surface = font.render(str(numbers[i]), 1, black)
            text_surface = font.render(str(words[i]), 1, black)
            screen.blit(numbers_surface, (nr_pos_x, nr_pos_y))
            screen.blit(text_surface, (txt_pos_x, txt_pos_y))
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
        self.blit_caption_board(40, 108, 70, 80)

    def draw_board_opponent(self):
        """Wyświetla planszę przeciwnika, znajduje się po prawej stronie"""
        pos_x = 780
        pos_y = 100
        distance = 30
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                pygame.draw.aalines(screen, black, False,
                                    [(pos_x, pos_y), (pos_x + distance, pos_y), (pos_x + distance, pos_y + distance),
                                     (pos_x, pos_y + distance), (pos_x, pos_y)])
                pos_x += distance
            pos_x = 780
            pos_y += distance
        self.blit_caption_board(760, 108, 790, 80)

    @staticmethod
    def update():
        """Aktualizuje obraz na ekranie"""
        pygame.display.update()


if __name__ == "__main__":
    game = GameManagement()
    game.game_intro()
