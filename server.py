import socket
from collections import namedtuple

COMMAND = ''
SERVER_ADDRESS = 'XXX.XXX.XXX.XXX'
SERVER_PORT = 0000

Server = namedtuple('Server', 'addr, port')
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(Server(SERVER_ADDRESS, SERVER_PORT))

server.listen()
print('Server opened')

try:
    while True:
        conn, addr = server.accept()
        if conn:
            print('Opened session', addr)
            while True:
                COMMAND = input('Input command: ')
                
                conn.send(bytes(COMMAND.encode()))
                data = conn.recv(65565)
                if data:
                    print(data)
except:
    print('Connection closed', addr)
    conn.close()
    server.close()    
    
conn.close()
server.close()





















