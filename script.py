from imagesearch import *
from pynput.mouse import Controller, Button
import time

mouse = Controller()

while True:
    time.sleep(1)
    pos = imagesearch("./dou.png")

    if pos[0] != -1:
        mouse.position = (636, 562) #Aca ajustar las coordenadas del boton "¡aceptar!" en caso de que haga click en cualquier lugar, esos valores son para una pantalla con resolucion 1366x 768
        mouse.click(Button.left, 1)
        pyautogui.moveTo(pos[0], pos[1])
        #break 
        
        
#Descomentar el break si queres que solo acepte la primer partida encontrada
