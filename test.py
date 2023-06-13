from playsound import playsound
import multiprocessing
from time import sleep


# song = "Music\Rock\Favorite\Creeps.mp3"


def play():
    playsound("Music\Rock\Favorite\Creeps.mp3")
if __name__ == "__main__":
    M1 = multiprocessing.Process(target=play)

    M1.start()
    sleep(0.1)
    input(">>>")

    M1.terminate()
