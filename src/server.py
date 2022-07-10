import threading
import socket
import random
from game import Game

HOST = "localhost"
PORT = 63337
SIZE = 1024
FORMAT = "utf-8"

game = Game()

def client_connection_handler(conn, addr):
    while True:
        client_action = conn.recv(SIZE).decode(FORMAT)
        if not client_action or game.check_disconnection(client_action):
            print(f"Connection closed by {addr}")
            break
        else:
            print(f"[{addr}] > {client_action}")

            server_action = random.choice(game.get_valid_actions())
            print(f"[SERVER] > {server_action}")

            conn.send(server_action.encode(FORMAT))

    conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        print(f"Server is listening on {HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            print(f"Connection established with {addr}")
            thread = threading.Thread(target=client_connection_handler, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    main()
