import pyautogui

def getLiveScreen():
    myScreenshot = pyautogui.screenshot()
    myFileLocation = 'C:\\Users\\thanh\\OneDrive\\Pictures\\screenshot.png'
    myScreenshot.save(myFileLocation)
    return myFileLocation
