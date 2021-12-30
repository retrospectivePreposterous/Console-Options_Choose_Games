import keyboard
import time
import winsound
import cursor
cursor.hide()

lap = 1  # Seconds to wait after pressing
frequency = 500  
duration = 200 
def beep ():
    winsound.Beep(frequency, duration)
beep ()

print("Use left and right to choose, and Space to enter option:\n")
print("What kind of food do you prefer?")

loop = True 
option = 1
while loop == True:
    
    if option == 1:
        print("=> Pizza          Fruit", end = "\r")
    elif option == 2:
        print("   Pizza       => Fruit", end = "\r")
        
    if keyboard.is_pressed('left'):
        option = 1
        beep ()
    if keyboard.is_pressed('right'):
        option = 2
        beep ()
    if keyboard.is_pressed('space'):
        print("\n")
        beep ()
        loop = False
        

if option == 1:
    print("It seems you are a Pizza guy!")
elif option == 2:
    print("So Fruit, uh?") 
time.sleep(lap) 


loop = True
while loop == True:
    
    print("press Space to exist", end = "\r")  
       
    if keyboard.is_pressed('space'):
        print("")
        beep ()
        loop = False