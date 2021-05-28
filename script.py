from imagesearch import *
from pynput.mouse import Controller, Button
import time

mouse = Controller()

while True:
    time.sleep(1)
    pos = imagesearch("./dou.png")

    if pos[0] != -1:
        mouse.position = (pos[0], pos[1])
        mouse.click(Button.left, 1)
        #break 
        
        
#Descomentar el break si queres que solo acepte la primer partida encontrada
