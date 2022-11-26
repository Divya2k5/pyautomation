import pyautogui 
import time
limit=input("enter limit:")
msg=input("enter message:")
i=0
time.sleep(10)
while i<int(limit):
    pyautogui.typewrite(msg)
    pyautogui.press("enter")
    
    i+=1






