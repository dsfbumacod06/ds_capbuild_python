# sockets and network programming
# 1 internet socket vs unix socket
# 2 TCP vs UDP - tcp accuracy, udp speed
# 3 which IP to use.
# 4 which port to use

#service script
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # defines internet socket, and TCP in the parameters - SOCK_DGRAM (UDP)
s.bind(('127.0.0.1',55555))
s.listen()

while True:
    client, address = s.accept()
    print(f'Connected to {address}')
    client.send("You are connected.".encode())
    client.close()