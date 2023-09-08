
#? Importing necessary libraries
import pyautogui as pag
import keyboard as kb
import time
import asyncio

#* Initializing the cycles variable
cycles = 0

#* Defining the box function
async def box():
  #* Making cycles a global variable so it can be accessed outside the function
  global cycles
  
  #* Locating the box, evo_box, and take_evo_box images on the screen
  box = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\box.png", confidence=0.4)
  evo_box = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\evo-box.png", confidence=0.5)
  take_evo_box = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\take-btn.png", confidence=0.5)
  
  #* Incrementing cycles by 1
  cycles += 1
  
  #* Checking if box, evo_box, or take_evo_box is found on the screen and performing actions accordingly
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

#* Defining the berry function
async def berry():
  #* Locating the blueBerry, redBerry, and yellowBerry images on the screen
  blueBerry = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\berry-blue.png", confidence=0.5)
  redBerry = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\berry-red.png", confidence=0.5)
  yellowBerry = pag.locateOnScreen("C:\\Users\\menno\\OneDrive\\Coding\\Python\\Auto-Box\\img\\berry-yellow.png", confidence=0.5)
  
  #* Checking if blueBerry, redBerry, or yellowBerry is found on the screen and performing actions accordingly
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

#* Waiting for 3 seconds before starting the bot
print("START: Starting in 3 seconds.")
time.sleep(3)
print("START: Succesfully started 'bot'.")

#* Making sure you can stop the bot from running by pressing / holding the 'q' for a bit
while kb.is_pressed('q') == False:
    asyncio.run(box())
    #* Running the berry function every 5 cycles
    if cycles >= 5:
      asyncio.run(berry())
      #* Resetting cycles to 0
      cycles = 0
