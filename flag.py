from time import sleep
import vlc

playing = set([1, 2, 3, 4])
video_directory = "/home/pi/flag/media/Untitled [FLAG].mp4"
# creating Instance class object
vlc_instance = vlc.Instance()

player = vlc_instance.media_player_new()
player.set_fullscreen(True)

sleep(5)

while True:
    player.set_mrl(video_directory)
    player.play()
    sleep(1)
    print("Finished")
    sleep(5)
