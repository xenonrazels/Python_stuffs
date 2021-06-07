import socket
import threading

PORT= 6060
SERVER='192.168.100.7'

SERVER_NAME=socket.gethostname()
ADDR=(SERVER, PORT)
FORMAT='utf-8'
HEADER=1028
DISCONNECTED="!DISCONNECT"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[new connections] {addr} connected.")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length= int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECTED:
                connected=False
            print(f"[{addr}]:{msg}")
    conn.close() 

def start():
    server.listen()
    print(f"[Listening] the server is listtening")

    while True:
        conn, addr = server.accept()
        thread= threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[Active connections]{threading.activeCount()-1}")

print(f"[STARTING] {SERVER_NAME} {SERVER} the server is running:")

start()