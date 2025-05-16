from adafruit_servokit import ServoKit
import busio
import board
import time
import random

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


def release_motors():
    for servo in [4, 5, 6, 7, 8, 9]:
        kit.servo[servo].angle = None


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

     # additional adjust for arms because elbow can not reach 90 degree
    kit.servo[8].angle = 0
    kit.servo[7].angle = 20
    kit.servo[9].angle = 180

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
    # additional adjust for arms because elbow can not reach 90 degree
    kit.servo[5].angle = 120
    kit.servo[8].angle = 60
    time.sleep(1)

    kit.servo[6].angle = 0
    kit.servo[9].angle = 180
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
    # additional adjust for arms because elbow can not reach 90 degree
    kit.servo[5].angle = 150
    kit.servo[8].angle = 30
    for _ in range(3):
        time.sleep(1)
        kit.servo[6].angle = 50
        kit.servo[9].angle = 130
        time.sleep(1)
        kit.servo[6].angle = 0
        kit.servo[9].angle = 180
        
    
# One hand wave
def pose5():
    kit.servo[5].angle = 90
    time.sleep(0.5)
    kit.servo[4].angle = 180
    time.sleep(0.5)
    # additional adjust for arms because elbow can not reach 90 degree
    kit.servo[5].angle = 160

    kit.servo[6].angle = 0
    time.sleep(0.5)
    kit.servo[6].angle = 60
    time.sleep(0.5)
    kit.servo[6].angle = 0
    time.sleep(0.5)
    kit.servo[6].angle = 60

# Hug
def pose6():
    kit.servo[5].angle = 90
    kit.servo[8].angle = 90
    time.sleep(1)
    kit.servo[4].angle = 110
    kit.servo[7].angle = 110
    time.sleep(1)
    kit.servo[5].angle = 180
    kit.servo[8].angle = 0
    kit.servo[6].angle = 0
    kit.servo[9].angle = 180
    time.sleep(1)
    kit.servo[6].angle = 50
    kit.servo[9].angle = 130

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

    # additional adjust for arms because elbow can not reach 90 degree
    kit.servo[5].angle = 160
    kit.servo[8].angle = 20
    for _ in range(3):
        kit.servo[6].angle = 0
        kit.servo[9].angle = 120
        time.sleep(1)
        kit.servo[6].angle = 70
        kit.servo[9].angle = 180
        time.sleep(1)
    kit.servo[6].angle = 0
    kit.servo[9].angle = 180


def say():
    kit.servo[7].angle = random.randint(110, 180)
    kit.servo[4].angle = random.randint(0, 70)
    # time.sleep(3)
    # kit.servo[7].angle = 180
    # kit.servo[4].angle = 0

# Randomly select a pose to celebrate
def random_celebrate():
    poses = {
    "pose1": pose1,
    "pose2": pose2,
    "pose3": pose3,
    "pose4": pose4,
    "pose6": pose6,
    "pose7": pose7,
    "pose8": pose8,
    }

    random.choice(list(poses.values()))()
    
if __name__ == "__main__":
    reset_motors()
    time.sleep(1)
    say()
    time.sleep(5)

    reset_motors()
    time.sleep(1)
    pose1()
    time.sleep(5)

    reset_motors()
    time.sleep(1)
    pose2()
    time.sleep(5)

    reset_motors()
    time.sleep(1)
    pose3()
    time.sleep(5)

    reset_motors()
    time.sleep(1)
    pose4()
    time.sleep(5)

    reset_motors()
    time.sleep(1)
    pose5()
    time.sleep(5)


    reset_motors()
    time.sleep(1)
    pose6()
    time.sleep(5)


    reset_motors()
    time.sleep(1)
    pose7()
    time.sleep(5)


    reset_motors()
    time.sleep(1)
    pose8()
    time.sleep(5)
    reset_motors()
    