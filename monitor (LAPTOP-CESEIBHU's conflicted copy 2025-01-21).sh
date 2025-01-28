#!/bin/bash

# Variables
SOURCE_DIR="/home/haswell/karim"  # Directory on Haswell where .txt files are generated
TARGET_USER="Khach"              # Windows username
TARGET_IP="172.21.19.65"         # Windows machine IP address
TARGET_DIR="C:/Users/Khach/Downloads/transformed_logs"  # Destination directory on Windows

# Monitor for new .txt files
echo "Monitoring directory for new text files: $SOURCE_DIR"
while true; do
  # Check for new .txt files
  NEW_FILE=$(ls -Art "$SOURCE_DIR"/*.txt 2>/dev/null | tail -n 1)

  if [[ -n "$NEW_FILE" ]]; then
    BASENAME=$(basename "$NEW_FILE")
    echo "New text file detected: $BASENAME"

    # Step 1: Transfer the file to the target machine
    echo "Transferring $BASENAME to the target machine..."
    scp "$NEW_FILE" "$TARGET_USER@$TARGET_IP:\"$TARGET_DIR\""

    if [[ $? -eq 0 ]]; then
      echo "File $BASENAME successfully transferred to $TARGET_IP:$TARGET_DIR"
    else
      echo "Error: Failed to transfer $BASENAME to the target machine."
    fi
  fi

  # Wait before checking again
  sleep 10
done
