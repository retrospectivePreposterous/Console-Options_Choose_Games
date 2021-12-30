import keyboard
import time
import winsound
import cursor
cursor.hide()
from colorama import init, Fore, Back, Style
init()

lap = 1  # Seconds to wait after pressing
frequency = 500  
duration = 200 
space = 15

def beep ():
    winsound.Beep(frequency, duration)
beep ()

def choose (opt_list):
    loop = True 
    option = [0,0]
    print(Back.CYAN, end="")
    while loop == True:
        
        if option == [0,0]:
            print(Back.CYAN, end="")
            print("   " + opt_list[0] + (space-len(opt_list[0]))*" ", end="") 
            print(Style.RESET_ALL, end="")
            print("   " + opt_list[1] + (space-len(opt_list[1]))*" ")
            print("   " + opt_list[2] + (space-len(opt_list[2]))*" ", end="")
            print("   " + opt_list[3] + (space-len(opt_list[3]))*" ")
            print("\033[3A")
        elif option == [0,1]:
            print("   " + opt_list[0] + (space-len(opt_list[0]))*" ", end="") 
            print(Back.CYAN, end="")
            print("   " + opt_list[1] + (space-len(opt_list[1]))*" ")
            print(Style.RESET_ALL, end="")
            print("   " + opt_list[2] + (space-len(opt_list[2]))*" ", end="")
            print("   " + opt_list[3] + (space-len(opt_list[3]))*" ")
            print("\033[3A")
        elif option == [1,0]:
            print("   " + opt_list[0] + (space-len(opt_list[0]))*" ", end="") 
            print("   " + opt_list[1] + (space-len(opt_list[1]))*" ")
            print(Back.CYAN, end="")
            print("   " + opt_list[2] + (space-len(opt_list[2]))*" ", end="")
            print(Style.RESET_ALL, end="")
            print("   " + opt_list[3] + (space-len(opt_list[3]))*" ")
            print("\033[3A")
        elif option == [1,1]:
            print("   " + opt_list[0] + (space-len(opt_list[0]))*" ", end="") 
            print("   " + opt_list[1] + (space-len(opt_list[1]))*" ")
            print("   " + opt_list[2] + (space-len(opt_list[2]))*" ", end="")
            print(Back.CYAN, end="")
            print("   " + opt_list[3] + (space-len(opt_list[3]))*" ")
            print(Style.RESET_ALL, end="")
            print("\033[3A")
            
        if keyboard.is_pressed('left'):
            option = [option[0],0]
            beep ()
        if keyboard.is_pressed('right'):
            option = [option[0],1]
            beep ()
        if keyboard.is_pressed('up'):
            option = [0,option[1]]
            beep ()
        if keyboard.is_pressed('down'):
            option = [1,option[1]]
            beep ()
        if keyboard.is_pressed('space'):
            print(Style.RESET_ALL, end="")
            print("\n\n")
            beep ()
            loop = False
            
    return (option)

##############################################################################

print("Use left and right to choose, and Space to enter option:\n")
print("What kind of food do you prefer?")

option = choose(["PIZZA", "fruit",
                 "meat",  "fish"])
        
if option == [0,0]:
    print("It seems you are a Pizza guy!")
elif option == [0,1]:
    print("So Fruit, uh?") 
elif option == [1,0]:
    print("Meat is also my favourite") 
elif option == [1,1]:
    print("Fish, nah") 
print()
time.sleep(lap) 

print("And how do you move?")

option = choose(["Car", "Motorbike",
                 "Plane",  "by foot"])
        
if option == [0,0]:
    print("Polluting, fine")
elif option == [0,1]:
    print("lonely guy I see") 
elif option == [1,0]:
    print("Planes should be banned") 
elif option == [1,1]:
    print("Feetfeetfeet") 
time.sleep(lap) 


loop = True
while loop == True:
    
    print("press Space to exist", end = "\r")  
       
    if keyboard.is_pressed('space'):
        print("")
        beep ()
        loop = False