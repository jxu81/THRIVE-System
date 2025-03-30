from adafruit_servokit import ServoKit
import busio
import board
import time

# Initialize the I2C interface and ServoKit
i2c = busio.I2C(board.SCL, board.SDA)
kit = ServoKit(channels=16, i2c=i2c)

def reset_motors():
    kit.servo[4].angle = 0
    kit.servo[7].angle = 180
    kit.servo[5].angle = 180
    kit.servo[8].angle = 0
    kit.servo[6].angle = 90
    kit.servo[9].angle = 90

    # for servo in [4, 5, 6, 7, 8, 9]:
    #     kit.servo[servo].angle = None

# Dub
def pose1():
    kit.servo[5].angle = 90
    kit.servo[8].angle = 90
    time.sleep(1)
    kit.servo[4].angle = 180
    kit.servo[7].angle = 0
    time.sleep(1)
    kit.servo[9].angle = 160
    kit.servo[5].angle = 170

# Victory
def pose2():
    kit.servo[5].angle = 90
    kit.servo[8].angle = 90
    time.sleep(1)
    kit.servo[4].angle = 180
    kit.servo[7].angle = 0
    time.sleep(1)
    kit.servo[5].angle = 170
    kit.servo[8].angle = 10

# Double Arm Bow
def pose3():
    kit.servo[5].angle = 90
    kit.servo[8].angle = 90
    time.sleep(1)
    kit.servo[4].angle = 180
    kit.servo[7].angle = 0
    time.sleep(1)
    kit.servo[6].angle = 20
    kit.servo[9].angle = 160
    time.sleep(1)
    kit.servo[4].angle = 0
    kit.servo[7].angle = 180

# Two hand wave
def pose4():
    kit.servo[5].angle = 90
    kit.servo[8].angle = 90
    time.sleep(1)
    kit.servo[4].angle = 180
    kit.servo[7].angle = 0
    time.sleep(1)
    kit.servo[6].angle = 0
    kit.servo[9].angle = 180
    time.sleep(1)
    kit.servo[6].angle = 50
    kit.servo[9].angle = 130


# One hand wave
def pose5():
    kit.servo[5].angle = 90
    time.sleep(1)
    kit.servo[4].angle = 180
    time.sleep(1)
    kit.servo[6].angle = 0
    time.sleep(0.5)
    kit.servo[6].angle = 30
    time.sleep(0.5)
    kit.servo[6].angle = 0
    time.sleep(0.5)
    kit.servo[6].angle = 30

# Hug
def pose6():
    kit.servo[5].angle = 90
    kit.servo[8].angle = 90
    time.sleep(1)
    kit.servo[4].angle = 90
    kit.servo[7].angle = 90
    time.sleep(1)
    kit.servo[5].angle = 150
    kit.servo[8].angle = 30
    kit.servo[6].angle = 0
    kit.servo[9].angle = 180
    # time.sleep(1)
    # kit.servo[6].angle = 50
    # kit.servo[9].angle = 130

# Chop-Chop dance
def pose7():
    for _ in range(3):
        kit.servo[4].angle = 180
        time.sleep(1)
        kit.servo[7].angle = 0
        time.sleep(1)
        kit.servo[4].angle = 0
        time.sleep(1)
        kit.servo[7].angle = 180
        time.sleep(1)

# Overhead dance
def pose8():
    kit.servo[5].angle = 90
    kit.servo[8].angle = 90
    time.sleep(1)
    kit.servo[4].angle = 180
    kit.servo[7].angle = 0
    time.sleep(1)
    kit.servo[6].angle = 0
    kit.servo[9].angle = 180
    time.sleep(1)
    for _ in range(3):
        kit.servo[6].angle = 40
        kit.servo[9].angle = 140
        time.sleep(1)
        kit.servo[6].angle = 80
        kit.servo[9].angle = 180
        time.sleep(1)
    kit.servo[6].angle = 0
    kit.servo[9].angle = 180

if __name__ == "__main__":
    # for servo in [4, 5, 6, 7, 8, 9]:
    #     kit.servo[servo].angle = None

    # reset_motors()
    # time.sleep(1)
    # pose1()
    # time.sleep(5)

    # reset_motors()
    # time.sleep(1)
    # pose2()
    # time.sleep(5)

    # reset_motors()
    # time.sleep(1)
    # pose3()
    # time.sleep(5)

    # reset_motors()
    # time.sleep(1)
    # pose4()
    # time.sleep(5)


    # reset_motors()
    # time.sleep(1)
    # pose5()
    # time.sleep(5)


    # reset_motors()
    # time.sleep(1)
    # pose6()
    # time.sleep(5)


    # reset_motors()
    # time.sleep(1)
    # pose7()
    # time.sleep(5)


    # reset_motors()
    # time.sleep(1)
    # pose8()
    # time.sleep(5)

    