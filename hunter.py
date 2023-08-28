import pyautogui as pg
import time
import keyboard
import threading

def within_threshold(color1, color2, threshold):
    return all(abs(color1[i] - color2[i]) <= threshold for i in range(3))

def checkNettle():
    global stop_threads, end
    stop_threads = False
    end = False
    target_colors = [(144, 72, 48)]
    threshold = 2
    color_found = False
    
    x_range = range(986, 1583)
    y_range = range(239, 497)
    
    while True:
        if stop_threads:
            pass
        elif end:
            print("Finalized!")
            break
        else:
            s = pg.screenshot()
            for x in x_range:
                for y in y_range:
                    pixel_color = s.getpixel((x, y))
                    if any(within_threshold(pixel_color, target_color, threshold) for target_color in target_colors) and not color_found:
                        print("Color found!")
                        color_found = True
                        break
                if color_found:
                    color_found = False
                    break
        time.sleep(1)

def finalize():
    global stop_threads
    global end
    while True:
        if keyboard.is_pressed("f2"):
            stop_threads = True
        if keyboard.is_pressed("f1"):
            stop_threads = False
        if keyboard.is_pressed("esc"):
            end = True
            stop_threads = False
            break

x = threading.Thread(target=checkNettle)
y = threading.Thread(target=finalize)

time.sleep(3)

x.start()
y.start()
