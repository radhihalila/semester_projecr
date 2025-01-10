import pyautogui
import time

# Path to the image you want to locate
image_path = 'open_file.png'  

try:
    # Attempt to locate the image on the screen
    location = pyautogui.locateOnScreen(image_path, confidence=0.8)
    if location:
        # If found, print the location and move the mouse to it
        print("Object found at: {}".format(location))
        x, y = pyautogui.center(location)
        pyautogui.moveTo(x, y, duration=0.5)  
        pyautogui.click()
        print("Clicked on the target at ({}, {})".format(x, y))
    else:
        print("Target not found on the screen.")
except Exception as e:
    print("An error occurred: {}".format(e))
