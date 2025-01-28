import pyautogui
import pytesseract
from PIL import ImageOps
import time
import re

# Configure Tesseract OCR
pytesseract.pytesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Function to extract files with `.qmdl2` and `.qmdl` extensions in a region
def extract_files_with_extensions(region, extensions=[".qmdl2", ".qmdl"]):
    """
    Extract valid file names with specified extensions from a screen region.

    Parameters:
        region (tuple): (x, y, width, height) - Region to capture for OCR.
        extensions (list): List of file extensions to validate.

    Returns:
        list: Valid filenames matching the extensions.
    """
    # Capture the screen region
    screenshot = pyautogui.screenshot(region=region)
    grayscale_screenshot = ImageOps.grayscale(screenshot)
    detected_text = pytesseract.image_to_string(grayscale_screenshot)
    print(f"Detected text:\n{detected_text}")

    # Validate filenames based on extensions
    extensions_pattern = "|".join([re.escape(ext) for ext in extensions])
    files = re.findall(rf'\S+({extensions_pattern})', detected_text)
    print(f"Valid files found: {files}")

    return files


# Function to click the "Open" button
def click_open_button(open_button_image):
    """
    Locate and click the "Open" button if it's active.

    Parameters:
        open_button_image (str): Path to the "Open" button screenshot.

    Returns:
        bool: True if the button is clicked, False otherwise.
    """
    open_button_location = pyautogui.locateOnScreen(open_button_image, confidence=0.8)
    if open_button_location:
        print(f"'Open' button found at: {open_button_location}")
        pyautogui.click(open_button_location)
        return True
    else:
        print("'Open' button not found or inactive.")
        return False


# Main Script
time.sleep(5)  # Allow time to switch to the file explorer

# Step 1: Locate and click "Open Option 1"
location_open_option = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_option1.png')
if location_open_option:
    print(f"Object 'Open Option 1' found at: {location_open_option}")
    pyautogui.click(location_open_option)
else:
    print("Object 'Open Option 1' not found.")

time.sleep(5)

# Step 2: Locate and click "Open File"
location_open_file = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_file.png', confidence=0.6)
if location_open_file:
    print(f"Object 'Open File' found at: {location_open_file}")
    pyautogui.click(location_open_file)
else:
    print("Object 'Open File' not found.")

time.sleep(5)

# Define the region where filenames are displayed (adjust height to focus on one file at a time)
region_to_search = (100, 200, 800, 50)  # Narrow height for single-row detection

# Path to the "Open" button screenshot
open_button_image = 'C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_button.png'

# Track processed files to avoid duplicates
processed_files = set()

# Scroll and dynamically pick new files
for attempt in range(10):  # Scroll up to 10 times
    print(f"Scroll attempt {attempt + 1}...")

    # Extract and validate files
    files = extract_files_with_extensions(region=region_to_search, extensions=[".qmdl2", ".qmdl"])

    # Skip already processed files
    new_files = [file for file in files if file not in processed_files]

    if new_files:
        # Use the first unprocessed valid file
        selected_file = new_files[0]
        processed_files.add(selected_file)
        print(f"Selected file: {selected_file}")

        # Simulate pasting the file name into the "File Name" input field
        pyautogui.click(350, 600)  # Adjust these coordinates for your "File Name" input field
        pyautogui.hotkey('ctrl', 'a')  # Select all text
        pyautogui.typewrite(selected_file)  # Paste the file name

        # Click the "Open" button if active
        if click_open_button(open_button_image):
            break
    else:
        print("No valid files detected. Scrolling...")
        pyautogui.scroll(-100)  # Scroll down
        time.sleep(1)

# Step 3: Locate and click "Save to Text"
time.sleep(15)
location_save_to_text = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/save_to_text.png', confidence=0.8)
if location_save_to_text:
    print(f"Object 'Save to Text' found at: {location_save_to_text}")
    pyautogui.click(location_save_to_text)
else:
    print("Object 'Save to Text' not found.")

time.sleep(5)

# Step 4: Locate and click "Click on Save"
location_click_on_save = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/click_on_save.png', confidence=0.8)
if location_click_on_save:
    print(f"Object 'Click on Save' found at: {location_click_on_save}")
    pyautogui.click(location_click_on_save)
else:
    print("Object 'Click on Save' not found.")

# Step 5: Check if the file already exists and click "Yes Button" if necessary
time.sleep(5)
location_yes_button = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/yes_button.png', confidence=0.8)
if location_yes_button:
    print(f"Object 'Yes Button' found at: {location_yes_button}")
    pyautogui.click(location_yes_button)
else:
    print("Object 'Yes Button' not found. Proceeding without overwrite confirmation.")
