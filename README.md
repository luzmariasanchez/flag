# VLC Video Player

This is a simple Python script that utilizes VLC to play a video in a loop in fullscreen mode.

## Requirements

- Python 3.x
- VLC Media Player
- The `python-vlc` library (you can install it with `pip install python-vlc`)

## Setup

- Ensure VLC Media Player is installed on your system.
- Specify the directory path of the video in the `video_directory` variable.
- Adjust the `playing` set with the numbers of the videos you want to play.

## Usage

1. Run the Python script.
2. Wait for 5 seconds for the media player to initialize.
3. The specified video will start playing in a loop in fullscreen mode.
4. Each time the video playback completes, "Finished" will be printed in the console.
5. The script will continue playing the video in an infinite loop.

## Notes

- Ensure the path of the video specified in `video_directory` is valid.
- You can adjust the waiting time between loops by modifying the value of `sleep` in the loop.
