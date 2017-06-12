import socket
import win32api as win32

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 21998))
server_sock.listen(1)
print("listening on port 21998...")

client_sock, address = server_sock.accept()
print("Received connection from " + str(address))

while True:
    data = client_sock.recv(1024).decode()

    # print(str(data))
    # print(str(data).split("$"))

    current_pos = win32.GetCursorPos()
    accel = str(data).split("$")[1].split(" ")

    # print("B" + accel[0] + "B")
    # print("B" + accel[1] + "B")
    # print()

    accel_horiz = int(accel[0])
    accel_vert = int(accel[1])

    # print(accel_horiz, accel_vert)

    win32.SetCursorPos((current_pos[0] + accel_horiz * 10, current_pos[1] - accel_vert * 10))
