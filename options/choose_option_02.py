import keyboard
import time
import winsound
import cursor
cursor.hide()
from colorama import init, Fore, Style
init()

lap = 1  # Seconds to wait after pressing
frequency = 500  
duration = 200 
def beep ():
    winsound.Beep(frequency, duration)
beep ()

print("Use left and right to choose, and Space to enter option:\n")
print("What kind of food do you prefer?")

loop = True 
option = [0,0]
while loop == True:
    
    if option == [0,0]:
        print("=> Pizza          Fruit")
        print("   Meat           Fish")
        print("\033[3A")
    elif option == [0,1]:
        print("   Pizza       => Fruit")
        print("   Meat           Fish")
        print("\033[3A")
    elif option == [1,0]:
        print("   Pizza          Fruit")
        print("=> Meat           Fish")
        print("\033[3A")
    elif option == [1,1]:
        print("   Pizza          Fruit")
        print("   Meat        => Fish")
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
        print("\n\n")
        beep ()
        loop = False
        

if option == [0,0]:
    print("It seems you are a Pizza guy!")
elif option == [0,1]:
    print("So Fruit, uh?") 
elif option == [1,0]:
    print("Meat is also my favourite") 
elif option == [1,1]:
    print("Fish, nah") 
time.sleep(lap) 


loop = True
while loop == True:
    
    print("press Space to exist", end = "\r")  
       
    if keyboard.is_pressed('space'):
        print("")
        beep ()
        loop = False