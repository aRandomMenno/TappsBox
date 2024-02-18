
# Automatically opens boxes in tapps evolution games, using this program

> A program that will automatically open boxes in tapps evolution simulator games.

## What you need

- A computer with a program to mirror your screen to your computer. I use [scrcpy](https://github.com/Genymobile/scrcpy) for this.
  - using this method might require USB-debugging to be **enabled**.
- Python 3.11 or higher [(download Python)](https://www.python.org/downloads/) with the following library's:
  - pyautogui
  - keyboard
  - opencv-python

### **OR**

- A computer with an android emulator.
  - e.g. bluestacks.
- Python 3.11 or higher [9download Python)](https://www.python.org/downloads/) with the following library's:
  - pyautogui
  - keyboard
  - opencv-python

## Running the program

1. download code as zip
2. extract it to a folder
3. if you don't have Python, install it and the dependencies
4. open your emulator or copy your phone screen
5. if you would like you can run `safeguard.py` which will make your mouse go to the bottom right of the screen when pressing the `escape` key, triggering PyAutoGUI's failsafe to stop all scripts with pyautogui
6. run the file `bot.py`

### TODO

1. Make it so program automatically gives to the alien. But I have not figured out how.
