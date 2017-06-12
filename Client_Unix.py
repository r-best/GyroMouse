import socket
from pymouse import PyMouse

mouse = PyMouse()

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 21998))
server_sock.listen(1)
print("listening on port 21998...")

client_sock, address = server_sock.accept()
print("Received connection from " + str(address))

while True:
    data = client_sock.recv(1024).decode()

    current_pos = mouse.position()
    accel = str(data).split(" ")

    mouse.move(current_pos[0] + int(accel[0]), current_pos[1] + int(accel[1]))