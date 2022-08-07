import os, time
from pygame import mixer

def playSound():
        # Initialize pygame mixer
    mixer.init()
        # Load the sounds
    sound = mixer.Sound('../sound/Cheerful R2D2.wav')
        # play sounds
    sound.play()
         # wait for sound to finish playing
    time.sleep(3)

if __name__ == '__main__':
    while(True):
        playSound() 
        time.sleep(10)