
#! Importing necessary libraries
import pyautogui as pag
import keyboard as kb
import time
import asyncio

cycles = 0

#! Defining the box function
async def box():
  
  global cycles
  box = pag.locateOnScreen(r"C:\Users\menno\OneDrive\Coding\Python\Auto-Box\img\box.png", confidence=0.5)
  evo_box = pag.locateOnScreen(r"C:\Users\menno\OneDrive\Coding\Python\Auto-Box\img\evo-box.png", confidence=0.6)
  take_evo_box = pag.locateOnScreen(r"C:\Users\menno\OneDrive\Coding\Python\Auto-Box\img\take-btn.png", confidence=0.6)
  cycles += 1

  #! checking if any boxes are found or we need to take the evobox reward.
  if take_evo_box is not None:
    pag.moveTo(take_evo_box)
    pag.leftClick()
  elif box is not None:
    pag.moveTo(box)
    pag.leftClick()
  elif evo_box is not None:
    pag.moveTo(evo_box)
    pag.leftClick()

#! Defining the berry function
async def berry():
  blueBerry = pag.locateOnScreen(r"C:\Users\menno\OneDrive\Coding\Python\Auto-Box\img\berry-blue.png", confidence=0.5)
  redBerry = pag.locateOnScreen(r"C:\Users\menno\OneDrive\Coding\Python\Auto-Box\img\berry-red.png", confidence=0.5)
  yellowBerry = pag.locateOnScreen(r"C:\Users\menno\OneDrive\Coding\Python\Auto-Box\img\berry-yellow.png", confidence=0.5)
  
  #! Check for berries.
  if blueBerry is not None:
    pag.moveTo(blueBerry)
    pag.leftClick()
  elif redBerry is not None:
    pag.moveTo(redBerry)
    pag.leftClick()
  elif yellowBerry is not None:
    pag.moveTo(yellowBerry)
    pag.leftClick()

#! Waiting for 3 seconds before starting the bot
print("INFO: Starting in 3 seconds.")
time.sleep(3)
print("INFO: Succesfully started script.")

#! Making sure you can stop the script from running by pressing / holding the 'q' AND 's' at the same time.
while kb.is_pressed('q') == False:
  #! Making sure you can pause the script by pressing / holding the 'q' for a bit
    while kb.is_pressed('s') == False:
      asyncio.run(box())
      if cycles >= 5:
        asyncio.run(berry())
        cycles = 0

print("INFO: Stopped the script succesfully.")