#!/bin/bash

# Create the 'faster' directory if it doesn't exist
mkdir -p ./faster

# Array of utterances with text-to-speech compatible formatting
utterances=(
    "Keep up the good work. Move a little faster."
    "You are doing great! Let us pick up the pace a little!"
    "Awesome job! Try moving just a bit faster!"
    "Keep going! Can you speed up a little?"
    "You are on fire! Let us go a tiny bit quicker!"
    "Wow, you are doing amazing! Try moving a bit faster!"
    "Fantastic effort! Let us see if you can go a little quicker!"
    "Great work! Can you move just a little bit faster?"
    "You are rocking this! Let us speed up a tiny bit!"
    "Keep it up! Try picking up the pace a little!"
    "You are doing so well! Let us see if you can move a bit faster!"
    "Amazing energy! Can we speed things up a tiny bit?"
    "You are crushing it! Try going just a little faster!"
    "Fantastic! Let us see if you can move a little quicker!"
    "Keep up the good work! Can you go a bit faster?"
    "You are doing great! Let us try a slightly faster pace!"
    "Impressive! See if you can speed up just a bit!"
    "Nice job! Let us go a little faster this time!"
    "You are a superstar! Try moving just a bit quicker!"
    "Wonderful effort! Let us add a little more speed!"
    "Great going! Let us push the pace a tiny bit more!"
    "You are doing fantastic! Let us pick up the speed just a little!"
    "Great job! Can you go just a tiny bit faster?"
    "Super work! Let us see if we can move a little quicker!"
    "You are thriving great progress! Try speeding up a bit!"
    "Keep it up! Let us add a little more energy and go faster!"
    "You are unstoppable! See if you can move just a bit quicker!"
    "Amazing effort! Let us push the pace just a little more!"
    "Way to go! Can we pick up the speed just a tiny bit?"
    "Keep that momentum going! Let us move a little faster!"
    "You are doing so well! Let us speed things up just a little!"
)

# Loop through each utterance and generate audio files
for i in "${!utterances[@]}"; do
  # Get the current utterance
  utterance="${utterances[$i]}"
  
  # Generate the audio file (WAV)
  echo "$utterance" | sudo text2wave -eval "(voice_cmu_us_slt_cg)" -o "./faster/$i.wav"
  
  # Convert the WAV file to MP3 using ffmpeg, and set stereo (2 channels)
  ffmpeg -i "./faster/$i.wav" -ac 2 -q:a 0 "./faster/$i.mp3"
  
  # Optional: Print out which files are being processed
  echo "Generated ./faster/$i.wav and ./faster/$i.mp3"
done

echo "All audio files (WAV and MP3) have been generated!"