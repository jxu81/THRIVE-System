from __future__ import print_function
import socket
import subprocess
import sys
import time
from adafruit_servokit import ServoKit
import busio
import board
import subprocess
import neopixel_spi as neopixel
import random
import behaivor as behavior

# Initialize the I2C interface and ServoKit
i2c = busio.I2C(board.SCL, board.SDA)
kit = ServoKit(channels=16, i2c=i2c)

NUM_PIXELS = 12
PIXEL_ORDER = neopixel.GRB
BLUE = (0x0000FF)  # Blue color in RGB format
GREEN = (0x00FF00)  # Green color in RGB format
DELAY = 0.1

spi = board.SPI()

pixels = neopixel.NeoPixel_SPI(
    spi, NUM_PIXELS, pixel_order=PIXEL_ORDER, auto_write=False
)


def set_led_color(color):
    for i in range(NUM_PIXELS):
        pixels[i] = color
    pixels.show()

def play_audio(file_path):
    try:
        subprocess.run(["aplay", file_path], check=True)
    except Exception as e:
        print(f"Error playing audio: {e}")


if __name__ == "__main__":
    set_led_color(GREEN)
    behavior.reset_motors()
    time.sleep(5)

    # test 1
    set_led_color(BLUE)
    behavior.pose5()
    random_number = random.randint(0, 10)
    audio_file = f"/home/admin/THRIVE-System/audio_files/intro/{random_number}.wav"
    play_audio(audio_file)
    behavior.reset_motors()
    set_led_color(GREEN)
    time.sleep(5)

    # test 2
    set_led_color(BLUE)
    behavior.say()
    random_number = random.randint(0, 30)
    audio_file = f"/home/admin/THRIVE-System/audio_files/same/{random_number}.wav"
    play_audio(audio_file)
    behavior.reset_motors()
    set_led_color(GREEN)
    time.sleep(5)

    # test 3
    set_led_color(BLUE)
    behavior.say()
    random_number = random.randint(0, 30)
    audio_file = f"/home/admin/THRIVE-System/audio_files/faster/{random_number}.wav"
    play_audio(audio_file)
    behavior.reset_motors()
    set_led_color(GREEN)
    time.sleep(5)

    # test 4
    pose_numbers = [1, 2, 3, 4, 6, 7, 8]
    for num in pose_numbers:
        func_name = f"pose{num}"
    
        set_led_color(BLUE)
    # getattr(module, name) fetches behavior.pose1, behavior.pose2, etc.
        func = getattr(behavior, func_name, None)
        
        if func:
            func()
        else:
            print(f"Function {func_name} not found in behavior.py")
        audio_file = f"/home/admin/THRIVE-System/audio_files/end/{num}.wav"
        play_audio(audio_file)
        behavior.reset_motors()
        set_led_color(GREEN)
        time.sleep(5)




