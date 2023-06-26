# Music Player
## Modules
- Python
- multiprocessing
- playsound

This Python code uses playsound module to play a song.
~~~bash
import playsound

# Once playsound is ran it finishes program before moving on
playsound.playsound("Music.mp3")
~~~

And uses a multiprocesser to split the thread and terminate the thread once pressing a key.
~~~bash
from playsound import playsound
from multiprocessing import Process
if __name__ == "__main__":
     M1 = Process(target=playsound, args=("Music.mp3",))

     M1.start()
     input(">>>")
     M1.terminate()
~~~
