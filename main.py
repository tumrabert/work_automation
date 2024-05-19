import pandas as pd
import pygetwindow as gw
import threading
import pyautogui
import time

def return_date(path='icloud_template.csv'):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(path)
    # Convert the DataFrame to a list of lists excluding the header
    data = df.values.tolist()
    return data

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
        
def process_window(window):
    # Print thread ID and window title
    print("Thread ID:", threading.get_ident(), "Processed:", window.title)
    window.activate()
    window.maximize()
    print(f"Title: {window.title}, Position: ({window.left+10}, {window.bottom}), Size: ({window.width}, {window.height})")
    # Perform actions on the window here
    reg=(window.left+10, window.top+10, window.width, window.height)
    print(reg)
    if click_on_img("./img/your_txt.png",reg,confidence=0.95,click=True)==False:
            print("Your device not found")
    else:
            print("Your device found")
            pyautogui.move(0, 50, duration=0.1)
            pyautogui.click()
            time.sleep(0.1)    

    if click_on_img("img/sound_icon.png",reg,confidence=0.95,click=True)==False:
            print("Sound icon not found")
            #continue
    time.sleep(0.5)         
    window.minimize()

def main():
    chrome_windows = gw.getWindowsWithTitle('Screen')
    # Sort windows by title
    chrome_windows_sorted = sorted(chrome_windows, key=lambda x: x.title)
    # Start Threads
    # Sequentially process windows using a loop
    while True:
        for window in chrome_windows_sorted:
            process_window(window)
        print("Finished processing all windows. Restarting...")


if __name__ == "__main__":
    print("Program started...")
    main()