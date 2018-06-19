import socket
import pickle


class Client(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.buffer_size = 1024

    def connect_server(self):
        try:
            self.sock.connect((self.host,self.port))
            return True

        except:
            print("Nie udało się połączyć z serwerem.")

    def exit_server(self):
        try:
            self.sock.close()
        except:
            print("Nie jesteś połączony z serwerem !")

    def send_message(self, msg):
        message = pickle.dumps(msg)
        try:
            self.sock.send(message)
        except:
            print("Nie udało się wysłać wiadomości")

    def rcv_message(self):
        msg = self.sock.recv(self.buffer_size)
        message = pickle.loads(msg)

        return message

    def start_game(self):
        try:
            msg = self.rcv_message()
            if msg == '1':
                print('Zaczynasz ! Wyślij wiadomość')
                wiad = input('>> ')
                self.send_message(wiad)
            if msg == '2':
                print('Jesteś drugi! Zaczekaj na wiadomość..')
                wiad = self.rcv_message()
                print('Otrzymałeś wiadomość! "'+wiad+'"')
        except:
            print("Rozłączono z serwerem!")

if __name__ == "__main__":
    client = Client('localhost',2223)
    client.connect_server()
