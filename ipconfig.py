from time import sleep
from pyautogui import *

FAILSAFE = False
# Positions
start_btn = position(34, 878)
search_filed = position(110, 828)

# Actions
#click(position(34, 878))
click(start_btn)
if True:
    #click(position(110, 828))
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
            
            typewrite("bloc-notes")
            sleep(1)
            
            typewrite(["enter"])
            typewrite("This is operation made by Zakaria Farhati")
