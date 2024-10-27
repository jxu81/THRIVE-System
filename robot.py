from __future__ import print_function # Allows print functions to work as they do in Python 3
import socket
import subprocess
import sys

def speak(text):
    try:
        command = f"echo '{text}' | festival --tts"
        result = subprocess.run(command, shell=True, capture_output=True)
        print("STDOUT:", result.stdout.decode())
        print("STDERR:", result.stderr.decode())
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# Socket setup
backlog = 1
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('192.168.50.11', 12345))  # Bind creates one unique address
s.listen(backlog)

print('Waiting for a connection')

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
            
            # Call the speak function with received data
            if data.decode() == '0':
                speak('Hello. My name is Maki-Mini and I will be playing Super Pop with you today. I will ask you to complete the series of tasks and I would love it if you would follow my instructions. When you are ready, please raise both of your hands as high as you can.')
            elif data.decode() == '1':
                speak('Fantastic! Let us move at the exact same speed.')
            elif data.decode() == '2':
                speak('Keep up the good work. Move a little faster.')
            elif data.decode() == '3':
                speak('Fantastic! Wow! Good game. Let us play another one.')
                
            # Send the acknowledgment back to the client
            print('Sending data back to the client')
            connection.sendall(data)
        
finally:
    print("Closing socket")
    connection.close()
    s.close()
