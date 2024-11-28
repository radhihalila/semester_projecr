import pyautogui
import pytesseract
from PIL import ImageOps
import time
import re

# Configure Tesseract path (change to the correct path where Tesseract is installed)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Function to process text in a specific region
def extract_files_with_extension(region, extension=".qmdl2"):
    """
    Extract all files with a given extension from the specified screen region.

    Parameters:
        region (tuple): (x, y, width, height) - Region to search for file names.
        extension (str): File extension to search for (default: ".qmdl2").

    Returns:
        list: List of file names with the given extension.
    """
    screenshot = pyautogui.screenshot(region=region)
    grayscale_screenshot = ImageOps.grayscale(screenshot)
    detected_text = pytesseract.image_to_string(grayscale_screenshot)
    print(f"Detected text:\n{detected_text}")

    # Extract filenames with the specified extension
    files = re.findall(rf'\S+{re.escape(extension)}', detected_text)
    return files


# Main script
time.sleep(5)  # Allow time to switch to the file explorer

# Define the region where filenames are displayed (adjust as needed based on your screen resolution)
region_to_search = (100, 200, 800, 600)  # (x, y, width, height)

# Step 1: Locate and click "Open Option"
location_open_option = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_option1.png')
if location_open_option:
    print(f"Object 'Open Option' found at: {location_open_option}")
    pyautogui.click(location_open_option)
else:
    print("Object 'Open Option' not found.")

time.sleep(5)

# Step 2: Scroll and dynamically pick a new file
processed_files = set()  # To track files already processed
for attempt in range(10):  # Scroll up to 10 times
    files = extract_files_with_extension(region=region_to_search, extension=".qmdl2")
    new_file = next((file for file in files if file not in processed_files), None)

    if new_file:
        processed_files.add(new_file)
        print(f"New file found: {new_file}")
        
        # Simulate typing the file name into the file input field
        pyautogui.click(350, 600)  # Adjust coordinates for the "File name" input field
        pyautogui.typewrite(new_file)
        pyautogui.press("enter")
        break
    else:
        print("No new files found. Scrolling...")
        pyautogui.scroll(-100)  # Scroll down
        time.sleep(0.5)

time.sleep(5)

# Step 3: Locate and click "Open Button"
location_open_button = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_button.png', confidence=0.8)
if location_open_button:
    print(f"Object 'Open Button' found at: {location_open_button}")
    pyautogui.click(location_open_button)
else:
    print("Object 'Open Button' not found.")

time.sleep(15)

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
