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

bgr = cv2.imread('lab.png') #Por defecto opencv lee en BGR
wb = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

def print_screen ():
    screen = wb
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
        
print_screen()


input()