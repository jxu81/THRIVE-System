#!/bin/bash

# Create the 'slower' directory if it doesn't exist
mkdir -p ./slower

# Array of utterances with text-to-speech compatible formatting
utterances=(
    "Fantastic! Let us move at the exact same speed."
    "Fantastic! Keep moving at this exact speed!"
    "Great job! Maintain this pace!"
    "Awesome! Stay at this speed, just like that!"
    "You are doing great! Keep your movement steady!"
    "Perfect! Let us continue at this pace!"
    "Nice work! Keep going at this speed!"
    "Super! Hold this rhythm steady!"
    "Wonderful! Maintain this exact speed!"
    "You are crushing it! Keep up this steady pace!"
    "Excellent! Stay at this same speed!"
    "Amazing work! Keep moving just like this!"
    "You are doing fantastic! No need to speed up or slow down!"
    "Keep going! Stay right at this pace!"
    "That is it! Keep your movement smooth and steady!"
    "Great effort! Let us keep this exact rhythm!"
    "You are nailing it! Stick with this speed!"
    "Stay strong! Keep this pace steady!"
    "Well done! Keep your movement just like this!"
    "Awesome work! Let us keep this same speed!"
    "You have got it! Maintain this steady pace!"
    "Perfect speed! Just keep moving like this!"
    "You are a superstar! Keep the same rhythm!"
    "Brilliant! Keep up this perfect pace!"
    "Just right! Stay steady at this speed!"
    "You are doing so well! Keep your movements at this tempo!"
    "Keep rocking! No need to change your speed!"
    "Way to go! Keep your pace just like this!"
    "You are on fire! Maintain this awesome speed!"
    "You have got the rhythm! Keep it just like this!"
    "Steady and strong! Keep moving just like that!"
)

# Loop through each utterance and generate audio files
for i in "${!utterances[@]}"; do
  # Get the current utterance
  utterance="${utterances[$i]}"
  
  # Generate the audio file (WAV)
  echo "$utterance" | sudo text2wave -eval "(voice_cmu_us_slt_cg)" -o "./slower/$i.wav"
  
  # Convert the WAV file to MP3 using ffmpeg, and set stereo (2 channels)
  ffmpeg -i "./slower/$i.wav" -ac 2 -q:a 0 "./slower/$i.mp3"
  
  # Optional: Print out which files are being processed
  echo "Generated ./slower/$i.wav and ./slower/$i.mp3"
done

echo "All audio files (WAV and MP3) have been generated!"
