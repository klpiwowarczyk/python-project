import pickle
import socket, select
import threading
import pprint
from threading import Lock


lock = Lock()
class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        server.match_players()

class Server(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.sock.bind((self.host,self.port))
        self.count_players = 0
        self.buffer_size = 1024
        self.input = [self.sock]
        print('Server started ! Waiting for connections...')

    def listen(self):
        self.sock.listen(5)
        conn, addr = self.sock.accept()
        print('-----------------------------')
        print('Client accepted !\n Welcome !')
        print('-----------------------------')
        self.count_players += 1
        if self.count_players % 2 == 0:
            return conn, True
        return conn, False

    def match_players(self):
        pair_of_players = [[], []]
        is_a_pair = False

        while is_a_pair is not True:
            lock.acquire()
            conn, is_a_pair = self.listen()
            if not pair_of_players[0]:
                pair_of_players[0].append(conn)
            else:
                pair_of_players[1].append(conn)
            lock.release()

        print('----------------------------------------------------')
        print('Okay ! We got a pair of players matched.\n Let`s go!')
        print('----------------------------------------------------')
        self.start_game(pair_of_players[0][0], pair_of_players[1][0])



    def start_game(self, conn1, conn2):
        try:
            self.send_message(conn1,'start1')
            self.send_message(conn2,'start2')
            while True:
                msg = self.recv_msg(conn1)
                self.send_message(conn2, msg)
                msg = self.recv_msg(conn2)
                self.send_message(conn1, msg)
        except Exception :
            print("Unexpected error")

    def send_message(self, conn, msg):
        message = pickle.dumps(msg)
        try:
            conn.send(message)
        except Exception as e:
            print(e)

    def recv_msg(self, conn):
        msg = conn.recv(1024)
        message = pickle.loads(msg)
        return message

    def shutdown(self):
        self.sock.close()


if __name__ == "__main__":
    try:
        server = Server('127.0.0.1',2223)
        threads = []
        thread = threading.Thread(target=server.match_players, args=()).start()

    except Exception as e:
        print(e)
