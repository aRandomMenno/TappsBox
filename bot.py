
import pyautogui as pag
import time

class bot:
    def __init__(self):
        self.boxPos = None
        self.boxEvoPos = None
        self.TakeBtnBoxEvoGUIPos = None
        self.berryPosLeft = None
        self.berryPosRight = None
        self.searchRegion = [290, 320, 675, 850]
        self.berryCounter = 0

    def boxSearch(self):
        try:
            self.boxPos = pag.locateOnScreen(image=r"./img/box.png", region=self.searchRegion, grayscale=True, confidence=0.5)
        except pag.ImageNotFoundException:
            self.boxPos = None

    def boxEvoSearch(self):
        try:
            self.boxEvoPos = pag.locateOnScreen(image=r"./img/boxEvo.png", region=self.searchRegion, grayscale=True, confidence=0.5)
        except pag.ImageNotFoundException:
            self.boxEvoPos = None

    def TakeBtnEvoBoxGUISearch(self):
        try:
            self.TakeBtnBoxEvoGUIPos = pag.locateOnScreen(image=r"./img/boxEvoGUITakeBtn.png", region=self.searchRegion, grayscale=True, confidence=0.5)
        except pag.ImageNotFoundException:
            self.TakeBtnBoxEvoGUIPos = None

    def berrySearch(self):
        if self.berryCounter >= 240:
            try:
                self.berryPosLeft = pag.locateOnScreen(image=r"./img/berryLeft.png", region=self.searchRegion, grayscale=True, confidence=0.6)
            except pag.ImageNotFoundException:
                self.berryCounter -= 100
            try:
                self.berryPosRight = pag.locateOnScreen(image=r"./img/berryRight.png", region=self.searchRegion, grayscale=True, confidence=0.6)
            except pag.ImageNotFoundException:
                self.berryCounter -= 100
        else:
            pass
            
    def run(self):
        self.boxSearch()
        self.boxEvoSearch()
        self.TakeBtnEvoBoxGUISearch()
        self.berrySearch()
        
        if self.TakeBtnBoxEvoGUIPos != None:
            pag.moveTo(self.TakeBtnBoxEvoGUIPos)
            pag.leftClick(duration=0.07)

        if self.boxPos != None:
            pag.moveTo(self.boxPos)
            pag.leftClick(duration=0.07)
            
        if self.boxEvoPos != None:
            pag.moveTo(self.boxEvoPos)
            pag.leftClick(duration=0.07)
            
        if self.berryPosLeft != None:
            pag.moveTo(self.berryPos)
            pag.leftClick(duration=0.07)
            self.berryPos = None
            self.berryCounter = 0

        if self.berryPosRight != None:
            pag.moveTo(self.berryPos)
            pag.leftClick(duration=0.07)
            self.berryPos = None
            self.berryCounter = 0
            
        self.berryCounter += 1

bot = bot()
time.sleep(2) # $ Time to switch to the good tab!

if __name__ == '__main__':
    run = True
    while run:
        bot.run()
