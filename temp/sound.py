import os, time
from pygame import mixer

def playSound():
        # Initialize pygame mixer
    mixer.init()
        # Load the sounds
    sound = mixer.Sound('../sound/R2 beeping 2.mp3')
        # play sounds
    sound.play()
         # wait for sound to finish playing
    time.sleep(3)

if __name__ == '__main__':
    while(True):
        playSound() 
        time.sleep(10)