#!/bin/bash

# Variables
SOURCE_DIR="/home/haswell/karim"  # Directory on Haswell where .txt files are generated
WINDOWS_USER="Khach"      # Your Windows username
WINDOWS_IP="192.168.1.11"              # Replace with the IP address of your Windows machine
WINDOWS_DESTINATION="C:/Users/Khach/Downloads/transformed_logs"  # Replace with the target directory on your Windows machine
QCAT_PATH="/opt/qcom/QCAT7/bin/QCAT"  # Path to QCAT binary
LOG_DIR="/path/to/qmdl/files"         # Directory where QCAT should read input files
TRANSFORMED_DIR="/home/haswell/karim"  

# Ensure necessary directories exist
mkdir -p "$SOURCE_DIR" "$TRANSFORMED_DIR"

# Step 1: Start QCAT
echo "Starting QCAT..."
$QCAT_PATH &
QCAT_PID=$!  # Get QCAT process ID
echo "QCAT started with PID $QCAT_PID."

# Function to copy new text files
copy_files() {
  echo "Checking for new .txt files in $SOURCE_DIR..."
  for file in "$SOURCE_DIR"/*.txt; do
    # Check if file exists and is new
    if [[ -f "$file" ]]; then
      echo "Found file: $file"
      echo "Transferring $file to Windows machine..."
      scp "$file" "$WINDOWS_USER@$WINDOWS_IP:\"$WINDOWS_DESTINATION\""
      if [[ $? -eq 0 ]]; then
        echo "File $file successfully transferred to $WINDOWS_IP:$WINDOWS_DESTINATION"
      else
        echo "Error: Failed to transfer $file"
      fi
    fi
  done
}

# Main loop to monitor and copy new files
while true; do
  copy_files
  sleep 10  # Check every 10 seconds for new files
done

# Cleanup (only reached if the loop ends for some reason)
kill $QCAT_PID
echo "QCAT process stopped."
scp /home/haswell/karim/20241113_101853_0000.txt Khach@192.168.1.11:"C:/Users/Khach/Downloads/transformed_logs"
