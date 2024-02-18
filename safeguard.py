import pyautogui as pag
import keyboard

def move_mouse(_):
    pag.moveTo(10000, 10000)

keyboard.on_press_key('esc', move_mouse)

while True:
    pass