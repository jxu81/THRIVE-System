from __future__ import print_function
import socket
import subprocess
import sys
import time
from adafruit_servokit import ServoKit
import busio
import board

# Initialize the I2C interface and ServoKit
i2c = busio.I2C(board.SCL, board.SDA)
kit = ServoKit(channels=16, i2c=i2c)

def move_servo_step(servo, start_angle, end_angle, step=5, delay=0.1):
    try:
        current_angle = start_angle
        direction = 1  # 1 for increasing, -1 for decreasing

        while True:
            # Move the servo to the current angle
            kit.servo[servo].angle = current_angle
            print(f"Moving servo {servo} to {current_angle} degrees.")
            
            time.sleep(delay)
            
            # Update the angle for the next movement
            current_angle += step * direction
            
            # Reverse direction if the end or start angle is reached
            if current_angle >= end_angle or current_angle <= start_angle:
                direction *= -1  # Reverse direction (increment/decrement)
    
    except KeyboardInterrupt:
        # Release the servo on interrupt (Ctrl+C)
        kit.servo[servo].angle = None
        print(f"Servo {servo} released.")
# Function to control a waving motion of the servo motor with gradual movement
def wave_servo(servo, start_angle, end_angle, step=5, delay=0.1, cycles=2):
    
    def move_gradually_to_angle(servo, target_angle, step, delay):
        """Gradually moves the servo from its current angle to the target angle in steps."""
        current_position = kit.servo[servo].angle
        
        if current_position is None:
            current_position = start_angle  # Start from start_angle if not initialized
        
        # If the target angle is greater, increase in steps
        if current_position < target_angle:
            while current_position < target_angle:
                current_position += step
                if current_position > target_angle:
                    current_position = target_angle  # Avoid overshooting
                kit.servo[servo].angle = current_position
                print(f"Gradually moving servo {servo} to {current_position} degrees.")
                time.sleep(delay)
        # If the target angle is smaller, decrease in steps
        elif current_position > target_angle:
            while current_position > target_angle:
                current_position -= step
                if current_position < target_angle:
                    current_position = target_angle  # Avoid undershooting
                kit.servo[servo].angle = current_position
                print(f"Gradually moving servo {servo} to {current_position} degrees.")
                time.sleep(delay)
    
    for _ in range(cycles):  # Repeat for the given number of cycles
        # Gradually move from start_angle to end_angle
        move_gradually_to_angle(servo, end_angle, step, delay)
        print(f"Servo {servo} reached the final angle: {end_angle} degrees.")
        
        time.sleep(delay)
        
        # Gradually move back from end_angle to start_angle
        move_gradually_to_angle(servo, start_angle, step, delay)
        print(f"Servo {servo} returned to the initial angle: {start_angle} degrees.")
        time.sleep(delay)
    
    # Release the servo (optional)
    kit.servo[servo].angle = None
    print(f"Servo {servo} released after waving motion.")

# Function to move a servo motor from start_angle to end_angle in steps
# Function to move a servo motor from start_angle to end_angle in steps of 10 degrees
def move_servo_in_steps(servo, start_angle, end_angle, step=5, delay=0.1):
    # kit.servo[servo].angle = start_angle
    current_angle = start_angle

    # If start_angle is less than end_angle, move forward (increasing)
    if start_angle < end_angle:
        while current_angle <= end_angle:
            kit.servo[servo].angle = current_angle
            print(f"Moving servo {servo} to {current_angle} degrees.")
            time.sleep(delay)
            current_angle += step
    # If start_angle is greater than end_angle, move backward (decreasing)
    else:
        while current_angle >= end_angle:
            kit.servo[servo].angle = current_angle
            print(f"Moving servo {servo} to {current_angle} degrees.")
            time.sleep(delay)
            current_angle -= step

    # Ensure it reaches the exact end angle
    kit.servo[servo].angle = end_angle
    print(f"Servo {servo} reached the final angle: {end_angle} degrees.")

    # Release the servo (optional)
    kit.servo[servo].angle = None
    print(f"Servo {servo} released.")

def move_two_servos_in_steps(servo1, start_angle1, end_angle1, servo2, start_angle2, end_angle2, step=5, delay=0.1):
    # Determine the direction of movement for both servos
    direction1 = 1 if start_angle1 < end_angle1 else -1
    direction2 = 1 if start_angle2 < end_angle2 else -1

    current_angle1 = start_angle1
    current_angle2 = start_angle2

    # Continue until both servos reach their end angles
    while (direction1 == 1 and current_angle1 <= end_angle1) or (direction1 == -1 and current_angle1 >= end_angle1) or \
          (direction2 == 1 and current_angle2 <= end_angle2) or (direction2 == -1 and current_angle2 >= end_angle2):
        
        # Move servo 1 if it has not reached the end angle
        if (direction1 == 1 and current_angle1 <= end_angle1) or (direction1 == -1 and current_angle1 >= end_angle1):
            kit.servo[servo1].angle = current_angle1
            current_angle1 += step * direction1
            print(f"Moving servo {servo1} to {current_angle1} degrees.")

        # Move servo 2 if it has not reached the end angle
        if (direction2 == 1 and current_angle2 <= end_angle2) or (direction2 == -1 and current_angle2 >= end_angle2):
            kit.servo[servo2].angle = current_angle2
            current_angle2 += step * direction2
            print(f"Moving servo {servo2} to {current_angle2} degrees.")

        time.sleep(delay)

    # Ensure both servos reach their final angles
    kit.servo[servo1].angle = end_angle1
    kit.servo[servo2].angle = end_angle2
    print(f"Servo {servo1} reached the final angle: {end_angle1} degrees.")
    print(f"Servo {servo2} reached the final angle: {end_angle2} degrees.")

    # Optionally release the servos
    kit.servo[servo1].angle = None
    kit.servo[servo2].angle = None
    print(f"Servos {servo1} and {servo2} released.")

    
def reset_motors():
    kit.servo[4].angle = 0
    kit.servo[7].angle = 180
    kit.servo[5].angle = 180
    kit.servo[8].angle = 0
    kit.servo[6].angle = 90
    kit.servo[9].angle = 90

def set_max_volume():
    try:
        # Set the master volume to 100% (maximum volume)
        subprocess.run(["amixer", "sset", "'Master'", "100%"], check=True)
        print("Volume set to 100% (maximum).")
    except subprocess.CalledProcessError as e:
        print(f"Error setting volume: {e}")

# information about the speaker
# https://wiki.seeedstudio.com/ReSpeaker_2_Mics_Pi_HAT_Raspberry/
def play_audio(file_path, device="plughw:3,0"):
    try:
        # Command to play the audio file with the specified device
        subprocess.run(["aplay", "-D", device, file_path], check=True)
        print(f"Playing {file_path} on device {device}")
    except subprocess.CalledProcessError as e:
        print(f"Error playing audio file: {e}")



if __name__ == "__main__":
    # Set speaker
    set_max_volume()

    # Socket setup
    backlog = 1
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.1.100', 12345))  # Bind creates one unique address
    s.listen(backlog)

    print('Waiting for a connection')
    reset_motors()
    try:
        while True:
            connection, client_address = s.accept()
            print('Connection from', client_address)
            
            while True:
                data = connection.recv(size)
                if not data:
                    print('No more data from', client_address)
                    break
                
                print('Received "%s"' % data.decode())
                
                # Call the speak function with the appropriate audio file
                if data.decode() == '0':
                        move_servo_in_steps(servo=7, start_angle=180, end_angle=20, step=5, delay=0.1)
                        time.sleep(1)
                        wave_servo(servo=8, start_angle=5, end_angle=25, step=5, delay=0.1)
                        move_servo_in_steps(servo=4, start_angle=0, end_angle=20, step=5, delay=0.1)
                        audio_file = "/home/admin/THRIVE-System/audio_file_0.wav"  # Specify your audio file path here
                        play_audio(audio_file)
                elif data.decode() == '1':
                    move_servo_in_steps(servo=4, start_angle=20, end_angle=45, step=5, delay=0.1)
                    audio_file = "/home/admin/THRIVE-System/audio_file_1.wav"
                    play_audio(audio_file)
                elif data.decode() == '2':
                    move_servo_in_steps(servo=7, start_angle=160, end_angle=135, step=5, delay=0.1)
                    audio_file = "/home/admin/THRIVE-System/audio_file_2.wav"
                    play_audio(audio_file)
                elif data.decode() == '3':
                    move_two_servos_in_steps(servo1=7, start_angle1=150, end_angle1=30,
                            servo2=4, start_angle2=30, end_angle2=150, step=5, delay=0.1)
                    time.sleep(1)
                    move_servo_in_steps(servo=9, start_angle=140, end_angle=90, step=5, delay=0.1)
                    move_servo_in_steps(servo=6, start_angle=50, end_angle=90, step=5, delay=0.1)
                    audio_file = "/home/admin/THRIVE-System/audio_file_3.wav"
                    play_audio(audio_file)
                # Send the acknowledgment back to the client
                print('Sending data back to the client')
                connection.sendall(data)
            
    finally:
        print("Closing socket")
        connection.close()
        s.close()