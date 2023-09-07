import pyautogui as pag
import keyboard as kb
import time
import asyncio
cycles = 0

async def box():
  global cycles
  box = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\box.png", confidence=0.4)
  evo_box = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\evo-box.png", confidence=0.55)
  take_evo_box = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\take-btn.png", confidence=0.55)
  cycles += 1
  if box is not None:
    print("INFO: Normal box.")
    pag.moveTo(box)
    pag.leftClick()
  elif evo_box is not None:
    print("INFO: Evolution box.")
    pag.moveTo(evo_box)
    pag.leftClick()
  elif take_evo_box is not None:
    print("INFO: 'take it' btn.")
    pag.moveTo(take_evo_box)
    pag.leftClick()

async def berry():
  blueBerry = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\berry-blue.png", confidence=0.45)
  redBerry = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\berry-red.png", confidence=0.45)
  yellowBerry = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\berry-yellow.png", confidence=0.45)
  if blueBerry is not None:
    print("INFO: Blue berry.")
    pag.moveTo(blueBerry)
    pag.leftClick()
  elif redBerry is not None:
    print("INFO: Red berry.")
    pag.moveTo(redBerry)
    pag.leftClick()
  elif yellowBerry is not None:
    print("INFO: Yellow berry.")
    pag.moveTo(yellowBerry)
    pag.leftClick()

time.sleep(2)
print("START: Succesfully started 'bot'.")

while kb.is_pressed('q') == False:
  asyncio.run(box())
  if cycles >= 5:
    asyncio.run(berry())
    cycles = 0