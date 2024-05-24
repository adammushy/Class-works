import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(10)


position1=pt.locateOnScreen("bots/emoji.png",confidence=.6)

x = position1[0]
y = position1[1]


#get-message

def get_message():
    global x, y
    
    position = pt.locateOnScreen("bots/moji.png",confidence=.6)
    
    x = position[0]
    y = position[1]
    
    pt.moveTo(x,y, duration=.05)
    pt.moveTo(x+40,y+50, duration=.05)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(12,15)
    pt.click()    
    
    whatsapp_message=pyperclip.paste()
    
    pt.click()
    print("Message received:" + whatsapp_message)
    
    return whatsapp_message
    
get_message()
    