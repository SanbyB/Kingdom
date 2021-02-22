import socket
import pickle
from _thread import *
from player import players

server = '192.168.1.164'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)

print('waiting for connection, server started')

tb = [players[0].troops, players[1].troops]

'''
The information needed to be sent is just the troops and buildings of each player,
not the entire player object, this gives the error that the pygame.surface object cannot be pickled,
also there is no need to send the buttons info, or the resources info
'''


def theaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))

    reply = ''
    while True:
        try:
            data = pickle.loads(conn.recv(2048 * 4))
            players[player] = data

            if not data:
                print("disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

            conn.sendall(pickle.dumps(reply))

        except:
            break

    print('lost connection')
    conn.close()


currentplayer = 0
while True:
    conn, addr = s.accept()
    print('conected to: ', addr)

    start_new_thread(theaded_client, (conn, currentplayer))

    currentplayer += 1
