import bluetooth

# print("Searching for bluetooth-enabled client devices...\n")
#
# while True:
#     devices = bluetooth.discover_devices(duration=10, lookup_names=True)
#
#     if devices.__len__() != 0:
#         break
#     print("No devices found, retrying...")
#
# if devices.__len__() == 1:
#     print(str(devices.__len__()) + " device discovered")
# else:
#     print(str(devices.__len__()) + " devices discovered")
#
# i = 0
# for addr, name in devices:
#     print(str(i) + " - " + name + '(' + addr + ')')
#     i += 1
#
# client_index = input("Please enter the number (shown above) of the device you would like to connect to:")
# client_addr = devices[client_index][0]

# service_matches = bluetooth.find_service(uuid="abcd")
#
# if len(service_matches) == 0:
#     print("Couldn't find the service")
#
# first_match = service_matches[0]
# port = first_match["port"]
# name = first_match["name"]
# host = first_match["host"]
#
# print("Connecting to " + str(name) + " on " + str(host))
#
# sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# sock.connect((host, port))
# # sock.connect((client_addr, 20))
#
# sock.send("Back to the future")
#
# sock.close()

import socket
import time
from sense_hat import SenseHat


def calibrate():
    new_zero = sense.get_orientation_degrees()
    global zero_pitch, zero_roll
    zero_pitch = new_zero["pitch"]
    zero_roll = new_zero["roll"]


def calculate_accel():
    orientation = sense.get_orientation_degrees()
    pitch = orientation["pitch"]
    # roll = orientation["roll"]

    accel_horiz = 0
    # accel_vert = 0

    if pitch < zero_pitch:
        accel_horiz = -1
    elif pitch > zero_pitch:
        accel_horiz = 1

    # if roll < zero_roll:
    #     accel_vert = -1
    # elif roll > zero_roll:
    #     accel_vert = 1

    return accel_horiz#, accel_vert


def inc_notificator():
    global note
    note = note + 1
    if note >= 10:
        note = 0

note = 0
zero_pitch = 0
zero_roll = 0

sense = SenseHat()
sense.set_imu_config(False, True, False)
sense.low_light = True
calibrate()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.0.14', 21997))

while True:
    sense.show_letter(note)
    inc_notificator()

    accel_horiz = calculate_accel()
    sock.send(str(accel_horiz).encode())# + ':' + str(accel_vert)).encode())
    time.sleep(.001)

sock.close()
