import socket

server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_sock.bind(('', 21998))
server_sock.listen(1)
print("listening on port 21998...")

client_sock, address = server_sock.accept()
print("Received connection from " + str(address))

while True:
    data = client_sock.recv(1024).decode()
    print(data)
