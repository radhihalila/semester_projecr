import pyautogui
import time
# Capture a screenshot to locate an object
time.sleep(5)

location_open_option  = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_option1.png')
if location_open_option:
    print(f"Object found at: {location_open_option}")
    # Click at the found location
    pyautogui.click(location_open_option)

else:
    print("Object not found.")

time.sleep(5)

location_open_file = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_file.png')

if location_open_file:
    print(f"Object found at: {location_open_file}")
    # Click at the found location
    pyautogui.click(location_open_file)

else:
    print("Object not found.")

time.sleep(5)

location_open_button = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_button.png')
print('im here')
if location_open_button:
    print(f"Object found at: {location_open_button}")
    # Click at the found location
    pyautogui.click(location_open_button)

else:
    print("Object not found.")
time.sleep(50)

location_save_to_text = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/save_to_text.png')



if location_save_to_text:
    print(f"Object found at: {location_save_to_text}")
    # Click at the found location
    pyautogui.click(location_save_to_text)

else:

    print("Object not found.")

time.sleep(5)
location_click_on_save = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/click_on_save.png')



if location_click_on_save:
    print(f"Object found at: {location_click_on_save}")
    # Click at the found location
    pyautogui.click(location_click_on_save)

else:
    print("Object not found.")

#in the case where the file already exist    
time.sleep(5)
location_yes_button = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/yes_button.png')



if location_click_on_save:
    print(f"Object found at: {location_yes_button}")
    # Click at the found location
    pyautogui.click(location_yes_button)

else:
    print("Object not found.")    