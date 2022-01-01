import numpy as np
import cv2
import keyboard
import time
import winsound
import cursor
cursor.hide()
from colorama import init, Fore, Style
init()

# Imprescindible para que en consola lea las imagenes en el mismo directorio
import os
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# Lectura laberinto
bgr = cv2.imread('lab.png') #Por defecto opencv lee en BGR
screen = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# Variables
collected = 0
keys = len(np.where(screen == 150)[0])
fq = 500  
dt = 200 
special_fq = 800  
special_dt = 200 

rows = np.shape(screen)[0]
def cls():
    print("\033[" + str(rows+1) + "A", end="") # +1 is the line of Keys and Scores

def beep ():
    winsound.Beep(fq, dt)
def special_beep ():
    winsound.Beep(special_fq, special_dt)
beep()

def print_screen ():
    cls()
    for row in screen:
        for item in row:
            if item == 0:
                print("███", end="")
            elif item == 255:
                print(Fore.RED + " · ", end="")
                print(Style.RESET_ALL, end="")

            elif item == 76:
                print(Fore.YELLOW + " ● ", end="")
                print(Style.RESET_ALL, end="")
                
            elif item == 150:
                print(Fore.CYAN + " ▲ ", end="")
                print(Style.RESET_ALL, end="")
            
            elif item == 29:
                print(Fore.GREEN + " ■ ", end="")
                print(Style.RESET_ALL, end="")
        print()      
    print(Fore.YELLOW + "LLAVES: " + str(collected) + " / " + str(keys))
    print(Style.RESET_ALL, end="")
print_screen()



row,col = np.where(screen == 76)
heroe = [row,col]

loop = True 
while loop == True:
        
    if keyboard.is_pressed('left'):   
        if screen[heroe[0],heroe[1]-1] != 0:
            if screen[heroe[0],heroe[1]-1] == 150:
                collected += 1
                special_beep ()
            if screen[heroe[0],heroe[1]-1] != 29:
                screen[heroe[0],heroe[1]] = 255
                heroe = [heroe[0],heroe[1]-1]
                screen[heroe[0],heroe[1]] = 76
                print_screen()
                beep ()
            else:
                if collected == keys:
                    loop = False
    if keyboard.is_pressed('right'):
        if screen[heroe[0],heroe[1]+1] != 0:
            if screen[heroe[0],heroe[1]+1] == 150:
                collected += 1
                special_beep ()
            if screen[heroe[0],heroe[1]+1] != 29:
                screen[heroe[0],heroe[1]] = 255
                heroe = [heroe[0],heroe[1]+1]
                screen[heroe[0],heroe[1]] = 76
                print_screen()
                beep ()
            else:
                if collected == keys:
                    loop = False
    if keyboard.is_pressed('up'):
        if screen[heroe[0]-1,heroe[1]] != 0:
            if screen[heroe[0]-1,heroe[1]] == 150:
                collected += 1
                special_beep ()
            if screen[heroe[0]-1,heroe[1]] != 29:
                screen[heroe[0],heroe[1]] = 255
                heroe = [heroe[0]-1,heroe[1]]
                screen[heroe[0],heroe[1]] = 76
                print_screen()
                beep ()
            else:
                if collected == keys:
                    loop = False
    if keyboard.is_pressed('down'):
        if screen[heroe[0]+1,heroe[1]] != 0:
            if screen[heroe[0]+1,heroe[1]] == 150:
                collected += 1
                special_beep ()
            if screen[heroe[0]+1,heroe[1]] != 29:
                screen[heroe[0],heroe[1]] = 255
                heroe = [heroe[0]+1,heroe[1]]
                screen[heroe[0],heroe[1]] = 76
                print_screen()
                beep ()
            else:
                if collected == keys:
                    loop = False


