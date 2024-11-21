import cv2
import pyautogui
import time
import os
import subprocess

def locate_and_click(image_path, confidence=0.5, timeout=10):
    """
    Locate an on-screen image and click it.
    """
    start_time = time.time()
    while True:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            return True
        if time.time() - start_time > timeout:
            print(f"Error: Unable to find '{image_path}' within the timeout.")
            return False
        time.sleep(0.5)

print('Starting the automation process...')

# Step 1: Launch QCAT
#qcat_path = "/opt/qcom/QCAT7/bin/QCAT"  # Update with the correct QCAT command or executable path
#subprocess.Popen(['sudo', qcat_path], shell=True)
#print("Launching QCAT...")
time.sleep(15)  # Allow time for QCAT to open

# Step 2: Click 'File > Open'

if not locate_and_click('open_option.png'):
    exit()

# Step 3: Wait for the "Open File" dialog and select a file
print("Looking for the open file dialog...")
if locate_and_click('open_file.png',0.8):  # Adjust with a screenshot of the open file dialog
    time.sleep(2)  # Allow time for the file dialog to appear

    # Click on the first file in the dialog
    print("Selecting a file in the open dialog...")


        # Click the "Open" button in the dialog
    if locate_and_click('open_button.png'):  # Screenshot of the "Open" button
          print("Clicked the Open button.")
          time.sleep(3)  # Allow time for the file to load
    else:
         print("Error: 'Open' button not found.")
         exit()

else:
    print("Error: Open File dialog not found.")
    exit()

# Step 4: Handle QShrink4 Popup
print("Checking for QShrink4 popup...")
if locate_and_click('qshrink.png', confidence=0.5):  # Screenshot of the "No" button
    print("Handled QShrink4 popup by clicking 'No'.")
else:
    print("No QShrink4 popup detected.")

# Step 5: Navigate to "karim" Entry in the Left-Hand Tree View
print("Looking for 'karim' entry...")
if locate_and_click('karim_enter.png', confidence=0.9):  # Screenshot of the "karim" entry
    print("Navigated to 'karim'.")
else:
    print("Error: Unable to find 'karim' in the tree view.")
    exit()

# Step 6: Export the File
print("Looking for the save/export button...")
if locate_and_click('click_on_save.png', confidence=0.9):  # Screenshot of the Save/Export button
    print("Export button clicked.")
    pyautogui.typewrite("/home/haswell/karim/20241018_172553_0000.txt")  # Enter output file path
    pyautogui.press('enter')
    time.sleep(3)  # Allow time for the export to complete

    # Verify if the export was successful
    output_file = "/home/haswell/karim/20241018_172553_0000.txt"
    if os.path.exists(output_file):
        print(f"File transformed successfully! Output saved at '{output_file}'.")
    else:
        print("Error: Export failed. Output file not found.")
else:
    print("Error: Save/Export button not found.")