import pyautogui as pag
import keyboard as kb
import asyncio

cycles = 0

async def box():
  global cycles
  box = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\box.png", confidence=0.4)
  evo_box = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\evo-box.png", confidence=0.5)
  take_evo_box = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\take-btn.png", confidence=0.65)
  cycles += 1
  if box is not None:
    print("INFO: found normal box.")
    pag.moveTo(box)
    pag.leftClick()
  elif evo_box is not None:
    print("INFO: found evolution box.")
    pag.moveTo(evo_box)
    pag.leftClick()
  elif take_evo_box is not None:
    print("INFO: found 'take it'.")
    pag.moveTo(take_evo_box)
    pag.leftClick()

async def berry():
  blueBerry = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\berry-blue.png", confidence=0.5)
  redBerry = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\berry-red.png", confidence=0.5)
  yellowBerry = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\berry-yellow.png", confidence=0.5)
  if blueBerry is not None:
    print("INFO: found blue berry.")
    pag.moveTo(blueBerry)
    pag.leftClick()
  elif redBerry is not None:
    print("INFO: found red berry.")
    pag.moveTo(redBerry)
    pag.leftClick()
  elif yellowBerry is not None:
    print("INFO: found yellow berry.")
    pag.moveTo(yellowBerry)
    pag.leftClick()

while kb.is_pressed('q') == False:
  asyncio.run(box())
  if cycles >= 50:
    asyncio.run(berry())
    cycles = 0