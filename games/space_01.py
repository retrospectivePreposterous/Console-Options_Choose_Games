import numpy as np
import keyboard
import time
import cursor
cursor.hide()
from colorama import init, Fore, Style
init()

rows = 10
cols = 20
lap = 0.2

def cls():
    print("\033[" + str(rows) + "A", end="")


def print_screen ():
    cls()
    screen = np.zeros((rows,cols)).astype(int)
    screen[heroe[0], heroe[1]] = 1
    
    for row in screen:
        for item in row:
            if item == 0:
                print("·", end="")
            elif item == 1:
                print(Fore.RED + ">", end="")
                print(Style.RESET_ALL, end="")
        print()
        
# Init
heroe = [3,1]

print_screen ()

while 1 > 0:
    time.sleep(lap)

    if keyboard.is_pressed('w'):
        cls()
        heroe[0] -= 1
        print_screen ()
        
    if keyboard.is_pressed('s'):
        cls()
        heroe[0] += 1
        print_screen ()
        


        
        
