# VLC Video Player

This is a simple Python script that utilizes VLC to play a video in a loop in fullscreen mode.

## Requirements

- Python 3.x
- VLC Media Player
- The `python-vlc` library (you can install it with `pip install python-vlc`)

## Installation of Dependencies

Before running the program, make sure you have the following dependencies installed:

### Python 3.x

If you don't have Python installed, you can download it from the official website: [Python.org](https://www.python.org/).

### python-vlc

You can install python-vlc using pip, the Python package manager. Run the following command in your terminal:

pip install python-vlc

## Configuration

- Ensure VLC Media Player is installed on your system.
- Specify the directory path of the video in the `video_directory` variable.

## Usage

1. Run the Python script.
2. Wait for 5 seconds for the media player to initialize.
3. The specified video will start playing in a loop in fullscreen mode.
4. Each time the video playback completes, "Finished" will be printed in the console.
5. The script will continue playing the video in an infinite loop.

## Notes

- Ensure the path of the video specified in `video_directory` is valid.
- You can adjust the waiting time between loops by modifying the value of `sleep` in the loop.
