from time import sleep
from pyautogui import *

FAILSAFE = False # To leave the mouse move free in the screen :)
# Positions
start_btn = position(34, 878)
search_filed = position(110, 828)

# Actions

click(start_btn)
if True:
    
    click(search_filed)
    if True:  
        typewrite("cmd")
        sleep(2)
        
        typewrite(["enter"])
        sleep(1)
        
        typewrite("ipconfig -all")
        typewrite(["enter"])
        if True:
            typewrite("exit")
            click(start_btn)
            click(search_filed)
            sleep(2)
            
            
            # Editing is important here according to your computer's lang
            typewrite("bloc-notes") # for a french windows
            #typewrite("Notepad") # for a english windows
            sleep(1)
            
            typewrite(["enter"])
            typewrite("This is operation made by Zakaria Farhati")
