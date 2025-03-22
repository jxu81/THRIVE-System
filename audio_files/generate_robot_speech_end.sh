#!/bin/bash

# Create the 'end' directory if it doesn't exist
mkdir -p ./end

# Array of utterances with text-to-speech compatible formatting
utterances=(
    "Fantastic! Wow! Good game. Let us play another one."
    "Fantastic! Wow! That was a great game! Let us play another one!"
    "Awesome job! That was so much fun! Ready for another round?"
    "You did amazing! What a great game! Let us go again!"
    "Wow! That was fantastic! How about another game?"
    "Great work! You rocked that game! Let us play again!"
    "Super effort! That was fun! Want to play one more?"
    "Amazing! You are so good at this! Let us do another game!"
    "That was incredible! Let us go for another round!"
    "Woohoo! You did awesome! Let us play again!"
    "Nice job! What a fun game! How about another one?"
)

# Loop through each utterance and generate audio files
for i in "${!utterances[@]}"; do
  # Get the current utterance
  utterance="${utterances[$i]}"
  
  # Generate the audio file (WAV)
  echo "$utterance" | sudo text2wave -eval "(voice_cmu_us_slt_cg)" -o "./end/$i.wav"
  
  # Convert the WAV file to MP3 using ffmpeg, and set stereo (2 channels)
  ffmpeg -i "./end/$i.wav" -ac 2 -q:a 0 "./end/$i.mp3"
  
  # Optional: Print out which files are being processed
  echo "Generated ./end/$i.wav and ./end/$i.mp3"
done

echo "All audio files (WAV and MP3) have been generated!"
