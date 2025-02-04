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
    Extract all files with specified extensions from the specified screen region.

    Parameters:
        region (tuple): (x, y, width, height) - Region to search for file names.
        extensions (list): List of file extensions to search for (default: [".qmdl2", ".qmdl"]).

    Returns:
        list: List of file names with the given extensions.
    """
    screenshot = pyautogui.screenshot(region=region)
    grayscale_screenshot = ImageOps.grayscale(screenshot)
    detected_text = pytesseract.image_to_string(grayscale_screenshot)
    print(f"Detected text:\n{detected_text}")

    # Create a regex pattern to match any of the specified extensions
    extensions_pattern = "|".join([re.escape(ext) for ext in extensions])
    files = re.findall(rf'\S+({extensions_pattern})', detected_text)
    return files


# Main script
time.sleep(5)  # Allow time to switch to the file explorer

# Step 1: Locate and click "Open Option"
location_open_option = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_option1.png')
if location_open_option:
    print(f"Object 'Open Option' found at: {location_open_option}")
    pyautogui.click(location_open_option)
else:
    print("Object 'Open Option' not found.")

time.sleep(5)

# Define the region where filenames are displayed
region_to_search = (100, 200, 800, 600)  # Adjust based on your screen resolution

# Initialize a set to track processed files
processed_files = set()
new_file = None  # Initialize the new file as None

# Define the example file name to prioritize
example_file = "20241022_150702_0000.qmdl"

# Scroll and dynamically pick new files
for attempt in range(10):  # Scroll up to 10 times
    print(f"Scroll attempt {attempt + 1}...")

    # Extract files with the specified extensions
    files = extract_files_with_extensions(region=region_to_search, extensions=[".qmdl2", ".qmdl"])

    # Check if the example file is present
    if example_file in files and example_file not in processed_files:
        new_file = example_file
        processed_files.add(new_file)
        print(f"Example file selected: {new_file}")

        # Simulate typing the file name into the "File name" input field
        pyautogui.click(350, 600)  # Adjust coordinates for the "File name" input field
        pyautogui.typewrite(new_file)
        pyautogui.press("enter")

        # Exit after selecting the example file
        break

    # If the example file is not found, pick the first unprocessed file
    new_file = next((file for file in files if file not in processed_files), None)

    if new_file:
        processed_files.add(new_file)  # Mark this file as processed
        print(f"New file selected: {new_file}")

        # Simulate typing the file name into the "File name" input field
        pyautogui.click(350, 600)  # Adjust coordinates for the "File name" input field
        pyautogui.typewrite(new_file)
        pyautogui.press("enter")

        # Exit after selecting a new file
        break
    else:
        print("No new files found. Scrolling...")
        pyautogui.scroll(-100)  # Scroll down
        time.sleep(1)  # Wait for the UI to update after scrolling

# If no files were found after scrolling
# Step 2: Locate and click the "Open" button
time.sleep(5)
open_button_location = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/open_button.png', confidence=0.8)
if open_button_location:
    print(f"'Open' button found at: {open_button_location}")
    pyautogui.click(open_button_location)
else:
    print("Could not find the 'Open' button.")

time.sleep(5)

# Step 3: Locate and click "Save to Text"
location_save_to_text = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/save_to_text.png')
if location_save_to_text:
    print(f"Object 'Save to Text' found at: {location_save_to_text}")
    pyautogui.click(location_save_to_text)
else:
    print("Object 'Save to Text' not found.")

time.sleep(15)

# Step 4: Locate and click "Click on Save"
location_click_on_save = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/click_on_save.png')
if location_click_on_save:
    print(f"Object 'Click on Save' found at: {location_click_on_save}")
    pyautogui.click(location_click_on_save)
else:
    print("Object 'Click on Save' not found.")

# Step 5: Check if the file already exists and click "Yes Button" if necessary
time.sleep(5)
location_yes_button = pyautogui.locateOnScreen('C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/yes_button.png')
if location_yes_button:
    print(f"Object 'Yes Button' found at: {location_yes_button}")
    pyautogui.click(location_yes_button)
else:
    print("Object 'Yes Button' not found.")
