import pyautogui
import pytesseract
from PIL import Image
import time
import re

# Configure Tesseract path (change to the correct path where Tesseract is installed)
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Function to find and click any file with a given extension
def find_and_click_file_with_extension(extensions, reference_image, padding=(0, 0, 800, 600)):
    """
    Locate a file with a specific extension within a region defined dynamically by a reference image.

    Parameters:
        extensions (list): List of file extensions to search for (e.g., ['.qmdl', '.qmdl2']).
        reference_image (str): Path to the image to use as a region reference.
        padding (tuple): (x_offset, y_offset, width, height) to define the region around the reference.

    Returns:
        bool: True if a file is found and clicked, otherwise False.
    """
    # Locate the reference image
    reference_location = pyautogui.locateOnScreen(reference_image)
    if not reference_location:
        print("Reference image not found.")
        return False

    print(f"Reference image found at: {reference_location}")

    # Define the region based on the reference image and padding
    x, y, width, height = reference_location
    x_offset, y_offset, region_width, region_height = padding
    region = (x + x_offset, y + y_offset, region_width, region_height)
    print(f"Search region: {region}")

    # Take a screenshot of the defined region
    screenshot = pyautogui.screenshot(region=region)

    # Perform OCR to extract text
    detected_text = pytesseract.image_to_string(screenshot)
    print(f"Detected text:\n{detected_text}")

    # Search for any file with the given extensions
    for extension in extensions:
        match = re.search(rf'\S+{re.escape(extension)}', detected_text)  # Match file name with the extension
        if match:
            print(f"File found: {match.group()}")

            # Locate the file visually on the screen and click
            # Adjust the location based on region offset
            location = pyautogui.locateOnScreen(screenshot)
            if location:
                pyautogui.click(location)
                print(f"Clicked on: {match.group()}")
                return True

    return False


# Main script
time.sleep(5)  # Delay to switch to the file explorer

# Define the file extensions to search for
file_extensions = ['.qmdl', '.qmdl2']

# Provide the reference image to define the region
reference_image_path = 'C:/Users/Khach/Dropbox/PC/Documents/semester_projecr/file_region.png'  # Replace with your image

# Define padding around the reference image (x_offset, y_offset, width, height)
padding_around_reference = (0, 100, 800, 600)  # Adjust as needed for your screen

# Attempt to find and click a file with the specified extensions
if find_and_click_file_with_extension(file_extensions, reference_image_path, padding_around_reference):
    print("File with the specified extension clicked successfully!")
else:
    print("No file with the specified extension was found.")
