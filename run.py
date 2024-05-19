import pandas as pd
import pygetwindow as gw
import threading
import pyautogui
import time
def click_on_img(path,region=None,confidence=0.8,click=True):
    try:
        icon_location = pyautogui.locateOnScreen(path, grayscale=True, confidence=confidence,region=region)
        icon_center = pyautogui.center(icon_location)
        if click:
            pyautogui.click(icon_center)
        else:
            pyautogui.moveTo(icon_center)
        return True
    except pyautogui.ImageNotFoundException:
        return False
    
if __name__ == "__main__":
    print("Program started...")
    while True:
        click_on_img("img/sound_icon.png",confidence=0.95,click=True)
    main()