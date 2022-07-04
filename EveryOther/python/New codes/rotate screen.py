import time
#import win32api
import rotatescreen
import keyboard


screen = rotatescreen.get_primary_display()
for i in range(14):
    
    time.sleep(1)
    screen.rotate_to(i*90 % 360)
    
    