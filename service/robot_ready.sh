#!/bin/bash
# Source the virtual environment
source /home/admin/THRIVE-System/myenv/bin/activate

# Play hello sound
aplay /home/admin/THRIVE-System/audio_files/hello/hello_world.wav

# Run the Python script
python /home/admin/THRIVE-System/run_robot.py

