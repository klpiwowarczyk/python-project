import sys, os
import pygame
from Ships import Ships
from User import User
# colors
white = (255, 255, 255)
black = (0, 0, 0)

class GameManagement(object):
    """ Klasa do zarządzania grą, oknem intro oraz oknem gry"""

    def __init__(self):
        global screen
        pygame.init()
        self.SCREEN_W = 1200
        self.SCREEN_H = 600
        screen = pygame.display.set_mode((self.SCREEN_W, self.SCREEN_H))
        self.board = Board()
        self.ships = Ships()
        self.ships.make_group_sprites()
        self.isPlaying = True  # po skończonej grze gamePlay ustawiane będzie na False
        self.ship_direction = "poziomo"
        self.ship_type = 1
        self.ship_type_1_amount = 4
        self.ship_type_2_amount = 3
        self.ship_type_3_amount = 2
        self.ship_type_4_amount = 1
        self.ships_amount = 10


    def game_intro(self):
        """ Funkcja zarządzająca oknem początkowym """
        intro = True
        screen.fill((255, 255, 255))
        self.draw_text(font="Arial.ttf", font_size=54, color=black, pos_x=440, pos_y=50, text="Bitwa Morska")
        self.draw_button((100, 100, 100), 490, 250, 150, 50)
        self.draw_text(font="Arial.ttf", font_size=32, color=black, pos_x=540, pos_y=264, text="Graj!")
        self.draw_button((100, 100, 100), 490, 350, 150, 50)
        self.draw_text(font="Arial.ttf", font_size=32, color=black, pos_x=520, pos_y=364, text="Wyjście!")
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
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
        while game_choice:
            self.fill_game_choice()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos_x, pos_y = pygame.mouse.get_pos()
                    if self.button_clicked(pos_x, pos_y, 300, 250):
                        self.game_section()
                    if self.button_clicked(pos_x, pos_y, 700, 250):
                        self.multiplayer_section()
                pygame.display.update()

    def fill_game_choice(self):
        screen.fill(white)
        self.draw_text(font="Arial.ttf", font_size=54, color=black, pos_x=440, pos_y=50, text="Bitwa Morska")
        self.draw_button((100, 100, 100), 300, 250, 150, 50)
        self.draw_text(font="Arial.ttf", font_size=32, color=black, pos_x=330, pos_y=264, text="Hot-Seat!")
        self.draw_button((100, 100, 100), 700, 250, 150, 50)
        self.draw_text(font="Arial.ttf", font_size=32, color=black, pos_x=717, pos_y=262, text="Multiplayer!")

    def multiplayer_section(self):
        import Client
        screen.fill(white)
        self.draw_text(self.SCREEN_W/2-200,self.SCREEN_H/2-50,"Oczekiwanie na połączenie z serwerem...")
        pygame.display.update()
        client = Client.Client('localhost', 2223)
        connected = client.connect_server()
        if connected:
            screen.fill(white)
            self.draw_text(self.SCREEN_W/2-200,self.SCREEN_H/2-50,"Połączono z serwerem! Czekam na połączenie gracza..")
            pygame.display.update()
            msg = client.rcv_message()
            if msg == 'start1':
                screen.fill(white)
                self.draw_text(self.SCREEN_W/2-200,self.SCREEN_H/2-50,"Znaleziono gracza! Następuje przekierowanie do gry...")
                self.draw_text(self.SCREEN_W/2-200,self.SCREEN_H/2,"Jesteś pierwszym graczem więc będziesz zaczynał")
                pygame.display.update()
                pygame.time.delay(1000)
                self.game_section()
            elif msg == 'start2':
                screen.fill(white)
                self.draw_text(self.SCREEN_W/2-200,self.SCREEN_H/2-50,"Znaleziono gracza! Następuje przekierowanie do gry...")
                self.draw_text(self.SCREEN_W/2-200,self.SCREEN_H/2,"Jesteś drugim graczem, przeciwnik zaczyna.")
                pygame.display.update()
                pygame.time.delay(1000)
                self.game_section()

        else:
            screen.fill(white)
            self.draw_text(self.SCREEN_W/2-200,self.SCREEN_H/2-50,"Nie udało się połączyć z serwerem !")
            pygame.display.update()
            pygame.time.delay(1000)


    def game_section(self):
        """Funkcja zarządzająca oknem gry"""

        pygame.display.update()
        screen.fill(white)

        self.board.draw_board_player()
        self.board.draw_board_opponent()
        self.draw_ship_type_buttons()

        user_index_x = 0
        user_index_y = 0

        user = User()
        user.create_user_array()

        while self.isPlaying:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    pos_x, pos_y = pygame.mouse.get_pos()

                    self.set_direction(pos_x, pos_y)
                    self.set_ship_type(pos_x, pos_y)

                    if self.ships_amount > 0:
                        if 60 < pos_x < 360 and 100 < pos_y < 400:
                            for i in range(0, 10):
                                if 60 + 30 * i < pos_x < 90 + 30 * i:
                                    user_index_y = i
                            for j in range(0, 10):
                                if 100 + 30 * j < pos_y < 130 + 30 * j:
                                    user_index_x = j

                            if self.ship_type:
                                user.set_boat(user_index_x, user_index_y, self.ship_type, self.ship_direction, screen)
                                self.dec_ships_type_amount()
                                self.dec_ships_amount()

                            user.print_array_console()

                if event.type == pygame.QUIT:
                    self.isPlaying = False
                    pygame.quit()
                    sys.exit()
            pygame.display.flip()

    def dec_ships_amount(self):
        if self.ships_amount > 0:
            self.ships_amount -= 1

    def dec_ships_type_amount(self):
        if self.ship_type == 1 and self.ship_type_1_amount > 0:
            self.ship_type_1_amount -= 1
        elif self.ship_type == 2 and self.ship_type_2_amount > 0:
            self.ship_type_2_amount -= 1
        elif self.ship_type == 3 and self.ship_type_3_amount > 0:
            self.ship_type_3_amount -= 1
        elif self.ship_type == 4 and self.ship_type_4_amount > 0:
            self.ship_type_4_amount -= 1
        else:
            print("Wybierz statek!")

        if self.ship_type_1_amount == 0 and self.ship_type == 1:
            self.ship_type = False
        if self.ship_type_2_amount == 0 and self.ship_type == 2:
            self.ship_type = False
        if self.ship_type_3_amount == 0 and self.ship_type == 3:
            self.ship_type = False
        if self.ship_type_4_amount == 0 and self.ship_type == 4:
            self.ship_type = False

        self.draw_ship_type_buttons()

    def set_direction(self, pos_x, pos_y):
        if 300 < pos_x < 400 and 460 < pos_y < 485:
            self.ship_direction = "poziomo"

        if 300 < pos_x < 400 and 500 < pos_y < 525:
            self.ship_direction = "pionowo"

    def set_ship_type(self, pos_x, pos_y):
        if 60 < pos_x < 90 and 450 < pos_y < 475:
            self.ship_type = 1
        if 60 < pos_x < 120 and 490 < pos_y < 515:
            self.ship_type = 2
        if 60 < pos_x < 150 and 530 < pos_y < 555:
            self.ship_type = 3
        if 60 < pos_x < 180 and 570 < pos_y < 595:
            self.ship_type = 4

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

    def draw_text(self, pos_x, pos_y, text, font='Arial', font_size=24, color=black):
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

    def draw_ship_type_buttons(self):

        self.draw_text(font="Arial.ttf", font_size=20, color=black, pos_x=60, pos_y=430, text="Wybierz kierunek i rodzaj statku do umieszczenia na tablicy")
        self.draw_button(white,100,455,100,100)
        self.draw_button((100, 100, 100), 60, 450, 30, 25)
        self.draw_text(font="Arial.ttf", font_size=20, color=black, pos_x=100, pos_y=455,
                       text="pozostało : " + str(self.ship_type_1_amount))

        self.draw_button(white,130,495,100,100)
        self.draw_button((100, 100, 100), 60, 490, 60, 25)
        self.draw_text(font="Arial.ttf", font_size=20, color=black, pos_x=130, pos_y=495,
                       text="pozostało : "  + str(self.ship_type_2_amount))

        self.draw_button(white,160,535,100,100)
        self.draw_button((100, 100, 100), 60, 530, 90, 25)
        self.draw_text(font="Arial.ttf", font_size=20, color=black, pos_x=160, pos_y=535,
                       text="pozostało : " + str(self.ship_type_3_amount))

        self.draw_button(white,190,575,100,100)
        self.draw_button((100, 100, 100), 60, 570, 120, 25)
        self.draw_text(font="Arial.ttf", font_size=20, color=black, pos_x=190, pos_y=575,
                       text="pozostało : " + str(self.ship_type_4_amount))

        self.draw_button((0, 153, 51), 300, 460, 100, 25)
        self.draw_text(font="Arial.ttf", font_size=20, color=black, pos_x=320, pos_y=465,
                       text="POZIOMO")

        self.draw_button((179, 179, 0), 300, 500, 100, 25)
        self.draw_text(font="Arial.ttf", font_size=20, color=black, pos_x=320, pos_y=505,
                       text="PIONOWO")

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
