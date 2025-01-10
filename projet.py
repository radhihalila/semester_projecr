import pyautogui
import time

# Wait before starting to give time to prepare the environment
time.sleep(5)

# Step 1: Locate and click "Open Option"
location_open_option = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_option1.png')
if location_open_option:
    print(f"Object 'Open Option' found at: {location_open_option}")
    pyautogui.click(location_open_option)
else:
    print("Object 'Open Option' not found.")

time.sleep(15)

# Step 2: Locate and click "Open File"
location_open_file = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_file.png')
if location_open_file:
    print(f"Object 'Open File' found at: {location_open_file}")
    pyautogui.click(location_open_file)
else:
    print("Object 'Open File' not found.")

time.sleep(5)

# Pause for Manual File Selection
#print("Pause for manual file selection. Press Enter in the console to continue...")
#input("Press Enter to continue...")  # Wait for the user to select the file manually

# Step 3: Locate and click "Open Button"
location_open_button = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_button.png')
if location_open_button:
    print(f"Object 'Open Button' found at: {location_open_button}")
    pyautogui.click(location_open_button)
else:
    print("Object 'Open Button' not found.")

time.sleep(5)

# Step 4: Locate and click "Save to Text"
location_save_to_text = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/save_to_text.png')
if location_save_to_text:
    print(f"Object 'Save to Text' found at: {location_save_to_text}")
    pyautogui.click(location_save_to_text)
else:
    print("Object 'Save to Text' not found.")

time.sleep(5)

# Step 5: Locate and click "Click on Save"
location_click_on_save = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/click_on_save.png')
if location_click_on_save:
    print(f"Object 'Click on Save' found at: {location_click_on_save}")
    pyautogui.click(location_click_on_save)
else:
    print("Object 'Click on Save' not found.")

# Step 6: Check if the file already exists and click "Yes Button" if necessary
time.sleep(5)
location_yes_button = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/yes_button.png')
if location_yes_button:
    print(f"Object 'Yes Button' found at: {location_yes_button}")
    pyautogui.click(location_yes_button)
else:
    print("Object 'Yes Button' not found.")