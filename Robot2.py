from __future__ import print_function
import socket
import subprocess
import sys

def speak(audio_file):
    try:
        # Use aplay for .wav files or mpg123 for .mp3 files
        command = f"aplay {audio_file}"  # For .wav files
        # command = f"mpg123 {audio_file}"  # For .mp3 files
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
            
            # Call the speak function with the appropriate audio file
            if data.decode() == '0':
                speak('audio_file_0.mp4')  # Replace with the path to your audio file
            elif data.decode() == '1':
                speak('audio_file_1.mp4')  # Replace with the path to your audio file
            elif data.decode() == '2':
                speak('audio_file_2.mp4')  # Replace with the path to your audio file
            elif data.decode() == '3':
                speak('audio_file_3.mp4')  # Replace with the path to your audio file
                
            # Send the acknowledgment back to the client
            print('Sending data back to the client')
            connection.sendall(data)
        
finally:
    print("Closing socket")
    connection.close()
    s.close()