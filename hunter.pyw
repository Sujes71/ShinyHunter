import pyautogui as pg
import time
import threading
import os, sys

def within_threshold(color1, color2, threshold):
    return all(abs(color1[i] - color2[i]) <= threshold for i in range(3))

def asign_shiny_to_find(name):
    rgb_list = []
    with open('C:\\Users\\destr\\Documents\\ProjectsVSC\\shiny\\colors.txt', "r") as archivo:
        lineas = archivo.readlines()
        for linea in lineas:
            if name == linea.split(":")[0].strip():
                rgb_values = linea.split(":")[1].strip()
                rgb_values = rgb_values.replace("(", "").replace(")", "")
                rgb_values = rgb_values.split(",")
                rgb_values = [int(value) for value in rgb_values]
                rgb_list.append(rgb_values)
    return rgb_list
    

def checkNettle():
    global end
    end = False
    target_colors = asign_shiny_to_find(sys.argv[1])
    threshold = 2
    color_found = False
    
    x_range = range(986, 1583)
    y_range = range(239, 497)
    
    while True:
        if end:
            print("Finalized!")
            break
        else:
            s = pg.screenshot()
            for x in x_range:
                for y in y_range:
                    pixel_color = s.getpixel((x, y))
                    if any(within_threshold(pixel_color, target_color, threshold) for target_color in target_colors) and not color_found:
                        print("Color found!")
                        os.startfile('C:\\Users\\destr\\Documents\\ProjectsVSC\\shiny\\ring.mp3')
                        end = True
                        color_found = True
                        break
                if color_found:
                    color_found = False
                    break
        time.sleep(1)

x = threading.Thread(target=checkNettle)

x.start()
