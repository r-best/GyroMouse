# import bluetooth
#
# server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
#
# server_sock.bind(("", 0))
# server_sock.listen(1)
# print("Listening...")
#
# bluetooth.advertise_service(sock=server_sock, name="Test Service", service_id="abcd")
# print("Advertising service")
#
# while True:
#     client_sock, address = server_sock.accept()
#     print("Received connection from " + str(address))
#
#     data = client_sock.recv(1024)
#     print("Received " + str(data))
#
# client_sock.close()
# server_sock.close()

import socket
import pymouse

mouse = pymouse.PyMouse()

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('127.0.0.1', 21997))
server_sock.listen(1)
print("listening on port 21997...")

while True:
    client_sock, address = server_sock.accept()
    print("Received connection from " + str(address))

    data = str(client_sock.recv(1024).decode()).split(':')

    current_pos = mouse.position()
    mouse.move(current_pos[0] + data[0], current_pos[1] + data[1])
