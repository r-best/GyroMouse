import socket
import time
from sense_hat import SenseHat


def is_in(number, ranges):
    if type(ranges) == list:
        for i in range(0, ranges.__len__()):
            if number >= ranges[i][0] and number <= ranges[i][1]:
                return True
    elif type(ranges) == tuple:
        if number >= ranges[0] and number <= ranges[1]:
            return True
    return False

def calibrate():
    new_zero = sense.get_orientation_degrees()
    global pitch_range_n, pitch_range_l, pitch_range_r
    global roll_range_n, roll_range_l, roll_range_r

    pitch_range_n, pitch_range_l, pitch_range_r = calibrate_axis(int(new_zero["pitch"]))
    roll_range_n, roll_range_l, roll_range_r = calibrate_axis(int(new_zero["roll"]))


def calibrate_axis(zero):
    split = (zero + 180) % 360

    left_bound = zero + 10
    right_bound = zero - 10

    if right_bound < 0:
        right_bound = 360 + right_bound
    if left_bound > 360:
        left_bound = 0 + (left_bound - 360)
    
    range_n = calculate_range(right_bound, left_bound + 1)
    range_l = calculate_range(left_bound, split + 1)
    range_r = calculate_range(split, right_bound + 1)
    
    return range_n, range_l, range_r


def calculate_range(r1, r2):
    if r1 < r2:
        return (r1, r2)
    else:
        return [(0, r2), (r1, 360)]


def calculate_accel():
    orientation = sense.get_orientation_degrees()
    pitch = orientation["pitch"]
    roll = orientation["roll"]

    pitch_accel = 0
    roll_accel = 0

    if is_in(pitch, pitch_range_l):
        pitch_accel = -1
    elif is_in(pitch, pitch_range_r):
        pitch_accel = 1

    if is_in(roll, roll_range_l):
        roll_accel = -1
    elif is_in(roll, roll_range_r):
        roll_accel = 1

    return pitch_accel, roll_accel


pitch_range_n, pitch_range_l, pitch_range_r = 0, 0, 0
roll_range_n, roll_range_l, roll_range_r = 0, 0, 0

sense = SenseHat()
sense.set_imu_config(False, True, False)
sense.low_light = True
calibrate()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('192.168.0.14', 21998))

while True:
    pitch_accel, roll_accel = calculate_accel()
    sock.send(("$" + str(pitch_accel) + " " + str(roll_accel) + "$").encode())

    print(pitch_accel, roll_accel)

    if sense.stick.get_events().__len__() > 0:
        calibrate()

    time.sleep(.01)

sock.close()

