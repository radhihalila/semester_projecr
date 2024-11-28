import pyautogui
import time

# Function to scroll and locate an object dynamically
def scroll_and_locate(button_image, region=None, max_attempts=10, scroll_amount=-100):
    """
    Scroll the screen dynamically and try to locate the object.

    Parameters:
        button_image (str): Path to the button image to locate.
        region (tuple): Optional. The region to perform the search (x, y, width, height).
        max_attempts (int): Number of times to scroll before giving up.
        scroll_amount (int): Amount to scroll. Negative values scroll down, positive values scroll up.

    Returns:
        Location of the object if found, otherwise None.
    """
    for attempt in range(max_attempts):
        location = pyautogui.locateOnScreen(button_image, region=region)
        if location:
            return location
        pyautogui.scroll(scroll_amount)
        time.sleep(0.5)  # Allow time for screen to update after scrolling
    return None


# Start of the script
time.sleep(5)  # Give some time to switch to the file explorer

# Step 1: Locate and click "Open Option"
location_open_option = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_option1.png')
if location_open_option:
    print(f"Object 'Open Option' found at: {location_open_option}")
    pyautogui.click(location_open_option)
else:
    print("Object 'Open Option' not found.")

time.sleep(5)

# Step 2: Locate and click "Open File" dynamically by scrolling
location_open_file = scroll_and_locate('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_file.png')
if location_open_file:
    print(f"Object 'Open File' found at: {location_open_file}")
    pyautogui.click(location_open_file)
else:
    print("Object 'Open File' not found after scrolling.")

time.sleep(5)

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
