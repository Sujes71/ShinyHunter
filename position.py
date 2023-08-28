import pyautogui as pa
import keyboard
from time import sleep

while True:
    if keyboard.is_pressed('f2'):
        s = pa.screenshot()
        x, y = pa.position()
        print("COLOR: " + str(s.getpixel((x, y))))
        print("POSITION: " + str(pa.position()))
        sleep(1)
    if keyboard.is_pressed('escape'):
        break;