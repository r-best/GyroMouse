import socket
import time
from sense_hat import SenseHat


def calibrate():
    new_zero = sense.get_orientation_degrees()
    global zero_pitch, zero_roll
    zero_pitch = new_zero["pitch"]
    # zero_roll = new_zero["roll"]

    # roll_split = (zero_roll + 180) % 360

    left_bound = zero_pitch

    total_range = range(0, 361)
    neutral_range =
    left_range =

def calibrate_pitch(zero):
    split = (zero + 180) % 360

    left_bound = zero + 10
    right_bound = zero - 10

    if right_bound < 0:
        right_bound = 360 + right_bound
    if left_bound > 360:
        left_bound = 0 + (left_bound - 360)

    return range()


def calculate_accel():
    orientation = sense.get_orientation_degrees()
    pitch = orientation["pitch"]
    # roll = orientation["roll"]

    accel_horiz = 0
    # accel_vert = 0

    # if pitch < zero_pitch - 10:
    #     accel_horiz = -1
    # elif pitch > zero_pitch + 10:
    #     accel_horiz = 1
    #
    # if roll < zero_roll:
    #     accel_vert = -1
    # elif roll > zero_roll:
    #     accel_vert = 1



    return accel_horiz#, accel_vert

zero_pitch = 0
zero_roll = 0

sense = SenseHat()
sense.set_imu_config(False, True, False)
sense.low_light = True
calibrate()

# sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect(('192.168.0.14', 21998))

while True:
    accel_horiz = calculate_accel()
    # sock.send(str(accel_horiz).encode())

    if sense.stick.get_events().__len__() > 0:
        calibrate()

    time.sleep(.01)

sock.close()
