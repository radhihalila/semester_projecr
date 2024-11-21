import pyautogui
import time
image_path = "c:/Users/radhi/Documents/project/save_to_text.png"
time.sleep(5)
location = pyautogui.locateOnScreen(image_path, confidence=0.8)

if location:
    print(f"Image found at: {location}")
else:
    print("Image not found.")
