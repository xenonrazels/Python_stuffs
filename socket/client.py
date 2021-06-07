import socket
import threading

PORT= 6060
SERVER= '192.168.100.7'

ADDR=(SERVER, PORT)
FORMAT='utf-8'
HEADER=1028
DISCONNECTED="!DISCONNECT"
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message=msg.encode(FORMAT)
    send_length=str(len(message)).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length)) 
    client.send(send_length)
    client.send(message)
send(input("[Type your message]"))
send(DISCONNECTED)
