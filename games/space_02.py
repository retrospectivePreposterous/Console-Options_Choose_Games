import numpy as np
import keyboard
import time
import winsound
import cursor
cursor.hide()
from colorama import init, Fore, Style
init()

rows = 10
cols = 20
lap = 0.1
frequency = 500  
duration = 200 
def beep ():
    winsound.Beep(frequency, duration)
beep()

def cls():
    print("\033[" + str(rows) + "A", end="")


def print_screen ():
    cls()
    screen = np.zeros((rows,cols)).astype(int)
    screen[heroe[0], heroe[1]] = 1
    if missile != False:
        screen[missile[0], missile[1]] = 2
    for row in screen:
        for item in row:
            if item == 0:
                print("·", end="")
            elif item == 1:
                print(Fore.RED + ">", end="")
                print(Style.RESET_ALL, end="")
            elif item == 2:
                print(Fore.YELLOW + ")", end="")
                print(Style.RESET_ALL, end="")
        print()
        
# Init
heroe = [3,1]
missile = False
print_screen ()

while 1 > 0:
    time.sleep(lap)
    if missile != False:
        missile = [missile[0],missile[1]+1]
        if missile[1] >= cols:
            missile = False
    cls()
    print_screen ()
    if keyboard.is_pressed('w'):
        heroe[0] -= 1

    if keyboard.is_pressed('s'):
        heroe[0] += 1

    if keyboard.is_pressed('space'):
        if missile == False:
            beep()
            missile = [heroe[0],2]
        

        


        
        
