from time import sleep
import vlc
playing = set([1,2,3,4])  
video_directory = "/home/pi/Downloads/vis3.mp4"
# creating Instance class object
vlc_instance = vlc.Instance()
  
player = vlc_instance.media_player_new()
player.set_fullscreen(True)
  
sleep(5)

while True:
    player.set_mrl(video_directory)
    player.play()
    sleep(1)
    while player.get_state() in playing:
        sleep(1)
        continue        
    print("Finished")
    sleep(5)
    continue