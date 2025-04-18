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
    
    # Socket setup
    backlog = 1
    size = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('192.168.1.200', 12345))  # Bind creates one unique address
    s.listen(backlog)
    print('Waiting for a connection')
    
    behavior.reset_motors()
    
    try:
        while True:
            connection, client_address = s.accept()
            print('Connection from', client_address)
            
            try:
                # Handle the client connection here
                while True:
                    data = connection.recv(size)
                    if not data:
                        print('No more data from', client_address)
                        break
                    
                    print('Received "%s"' % data.decode())
                    
                    # Call the appropriate behavior based on received data
                    if data.decode() == '0':
                        set_led_color(BLUE)
                        behavior.pose5()
                        random_number = random.randint(0, 10)
                        audio_file = f"/home/admin/THRIVE-System/audio_files/intro/{random_number}.wav"
                        play_audio(audio_file)
                        behavior.reset_motors()
                    elif data.decode() == '1':
                        set_led_color(BLUE)
                        behavior.say()
                        random_number = random.randint(0, 30)
                        audio_file = f"/home/admin/THRIVE-System/audio_files/same/{random_number}.wav"
                        play_audio(audio_file)
                    elif data.decode() == '2':
                        set_led_color(BLUE)
                        behavior.say()
                        random_number = random.randint(0, 30)
                        audio_file = f"/home/admin/THRIVE-System/audio_files/faster/{random_number}.wav"
                        play_audio(audio_file)
                    elif data.decode() == '3':
                        set_led_color(BLUE)
                        behavior.random_celebrate()
                        random_number = random.randint(0, 10)
                        audio_file = f"/home/admin/THRIVE-System/audio_files/end/{random_number}.wav"
                        play_audio(audio_file)
                        behavior.reset_motors()
                    
                    set_led_color(GREEN)
                    print('Sending data back to the client')
                    connection.sendall(data)
            
            except Exception as e:
                print(f"Error handling the client connection: {e}")
            
            finally:
                print(f"Closing connection from {client_address}")
                connection.close()  # Close client connection, but keep server running
    
    except KeyboardInterrupt:
        print("Server stopped manually")
    
    finally:
        print("Server shutting down.")
        s.close()  # Close the server socket when the program is finished
