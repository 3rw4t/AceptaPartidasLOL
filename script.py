from pynput.mouse import Controller, Button
import time
import win32gui
mouse = Controller()
w=win32gui
condition = True
while condition:

    if w.GetWindowText(w.GetForegroundWindow()) == "League of Legends":
        time.sleep(3)
        mouse.position = (636, 562)
        mouse.click(Button.left, 1)
        condition = False
