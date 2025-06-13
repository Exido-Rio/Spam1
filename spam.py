import pyautogui as spam
import time
import requests
import os
 
limit = input("Enter number of msg")
msg = input("Mesagge you want to send")

i = 0

time.sleep(5)

while i<int(limit):
    spam.typewrite(msg)
    spam.press("Enter")
    time.sleep(2)
    i+=1
