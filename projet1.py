import pyautogui
import time
# Capture a screenshot to locate an object
time.sleep(5)

location_open_option  = pyautogui.locateOnScreen('c:/Users/radhi/Documents/project/open_option1.png')
if location_open_option:
    print(f"Object found at: {location_open_option}")
    # Click at the found location
    pyautogui.click(location_open_option)

else:
    print("Object not found.")

time.sleep(5)

location_open_file = pyautogui.locateOnScreen('c:/Users/radhi/Documents/project/open_file.png')

if location_open_file:
    print(f"Object found at: {location_open_file}")
    # Click at the found location
    pyautogui.click(location_open_file)

else:
    print("Object not found.")

time.sleep(5)

location_open_button = pyautogui.locateOnScreen('c:/Users/radhi/Documents/project/open_button.png')

if location_open_button:
    print(f"Object found at: {location_open_button}")
    # Click at the found location
    pyautogui.click(location_open_button)

else:
    print("Object not found.")
time.sleep(50)

location_save_to_text = pyautogui.locateOnScreen('c:/Users/radhi/Documents/project/save_to_text.png')



if location_save_to_text:
    print(f"Object found at: {location_save_to_text}")
    # Click at the found location
    pyautogui.click(location_save_to_text)

else:

    print("Object not found.")

time.sleep(5)
location_click_on_save = pyautogui.locateOnScreen('c:/Users/radhi/Documents/project/click_on_save.png')



if location_click_on_save:
    print(f"Object found at: {location_click_on_save}")
    # Click at the found location
    pyautogui.click(location_click_on_save)

else:
    print("Object not found.")