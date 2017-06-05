import bluetooth

server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

server_sock.bind(("", 21997))
server_sock.listen(1)

client_sock, address = server_sock.accept()
print("Received connection from " + str(address))

data = client_sock.recv(1024)
print("Received " + str(data))

client_sock.close()
server_sock.close()
