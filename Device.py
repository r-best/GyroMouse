import bluetooth

print("Searching for bluetooth-enabled client devices...\n")
devices = bluetooth.discover_devices()

if devices.__len__() == 1:
    print(devices.__len__() + " device discovered")
else:
    print(devices.__len__() + " devices discovered")

i = 0
for addr, name in devices:
    print(str(i) + " - " + name + '(' + addr + ')')
    i += 1

client_index = input("Please enter the number (shown above) of the device you would like to connect to:")
client_addr = devices[client_index][0]

sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((client_addr, 1997))

sock.send("Back to the future")
