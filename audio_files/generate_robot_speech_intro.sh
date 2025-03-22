#!/bin/bash

# Create the 'intro' directory if it doesn't exist
mkdir -p ./intro

# Array of utterances with text-to-speech compatible formatting
utterances=(
  "Hello. My name is Thrive and I will be playing Super Pop with you today. I will ask you to complete a series of tasks and I would love it if you could follow my instructions. When you are ready, please raise both of your hands as high as you can."
  "Hi there! I am Thrive, and today we are going to play Super Pop! I will guide you through some fun tasks, and I would love for you to follow my instructions. When you are ready, raise both hands as high as you can!"
  "Hello! My name is Thrive, and I am super excited to play Super Pop with you today! I have some fun tasks for you, so when you are ready, lift both hands up as high as possible!"
  "Hey there! I am Thrive, your game buddy for today! We are going to play Super Pop, and I will give you some fun challenges. Ready? Raise both hands up high!"
  "Hi! I am Thrive, and I cannot wait to play Super Pop with you! I will be giving you some fun tasks. When you are ready, reach up high with both hands!"
  "Hello, my friend! I am Thrive, and today we will play Super Pop together! I will guide you through some awesome tasks. If you are ready, stretch both hands up high!"
  "Hey! I am Thrive, and I am thrilled to play Super Pop with you today! I have some cool challenges for you. When you are ready, raise both hands as high as you can!"
  "Hi! I am Thrive, and I will be your game buddy today! Super Pop is going to be so much fun! Let us start, raise your hands high when you are ready!"
  "Hello! My name is Thrive, and I am excited to play Super Pop with you! I will be giving you instructions. When you are ready, lift your hands way up high!"
  "Hey, superstar! I am Thrive, and we are going to have a blast playing Super Pop! I will guide you through some tasks, so when you are ready, stretch those hands up high!"
  "Hi there! I am Thrive! Today, we are going to play Super Pop together! Follow my instructions and, when you are ready, raise both hands as high as you can!"
)

# Loop through each utterance and generate audio files
for i in "${!utterances[@]}"; do
  # Get the current utterance
  utterance="${utterances[$i]}"
  
  # Generate the audio file (WAV)
  echo "$utterance" | sudo text2wave -eval "(voice_cmu_us_slt_cg)" -o "./intro/$i.wav"
  
  # Convert the WAV file to MP3 using ffmpeg, and set stereo (2 channels)
  ffmpeg -i "./intro/$i.wav" -ac 2 -q:a 0 "./intro/$i.mp3"
  
  # Optional: Print out which files are being processed
  echo "Generated ./intro/$i.wav and ./intro/$i.mp3"
done

echo "All audio files (WAV and MP3) have been generated!"