import socket
from game import Game

HOST = "localhost"
PORT = 63337
SIZE = 1024
FORMAT = "utf-8"

game = Game()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        log_msg = f"Connection established with {HOST}:{PORT}"
        intro_msg = f"This application is a Rock, Paper, Scissors game \
(popularly known as Jokenpô).\
\n\nAt each iteration you will be given 4 options, representated by their \
name and followed by their hotkey in parentheses. You must press the \
assigned hotkey to activate the desired function.\
\n\nIf you choose Rock(r), paper(p) or scissors(s) you will play a round of \
the game, the server will reply with its move and the result of the \
round will be shown on your screen.\
\n\nIf you choose disconnect(d), you will be disconnected from the server \
and the game will end.\
\n\nHave fun!!\
\n\n---------------------------------------------------------"
        print(log_msg, end='\n\n')
        print(intro_msg, end='\n\n')

        while True:
            client_action = input("Rock(r), paper(p), scissors(s) or disconnect(d) > ").lower()
            while not game.is_valid(client_action):
                error_msg = f"Please type a valid input."
                print(error_msg, end='\n\n')


                client_action = input("Rock(r), paper(p), scissors(s) or disconnect(d) > ").lower()

            s.send(client_action.encode(FORMAT))

            if game.check_disconnection(client_action):
                outro_msg = f"Connection closed with {HOST}:{PORT}. Thanks for playing!"
                print(outro_msg)
                break

            else:
                server_action = s.recv(SIZE).decode(FORMAT)
                print(f"[{HOST}:{PORT}] played {game.get_action_fullname(server_action)}")

                game_result = game.resolve_game(client_action, server_action)
                out_msg = f""

                if game_result == 1:
                    out_msg = f"You win. Congratulations!"
                elif game_result == 2:
                    out_msg = f"You lose. Better luck next time!"
                else:
                    out_msg = f"It's a draw!"

                print(out_msg, end='\n\n')

        s.close()

if __name__ == "__main__":
    main()
