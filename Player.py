from playsound import playsound
import multiprocessing
from time import sleep

def play():
    playsound("Music.mp3")
if __name__ == "__main__":
    M1 = multiprocessing.Process(target=play)

    M1.start()
    sleep(0.1)
    input("Press key to End Music...")
    M1.terminate()
