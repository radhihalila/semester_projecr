#!/bin/bash

# Variables
QCAT_PATH="/opt/qcom/QCAT7/bin/QCAT"
LOG_DIR="/opt/qcom/QCAT7/logs"
TRANSFORMED_DIR="/opt/qcom/QCAT7/transformed_logs"
LOCAL_MACHINE_USER="Khach"
LOCAL_MACHINE_IP="192.168.1.11"
LOCAL_DESTINATION_PATH="C:/Users/Khach/Downloads/transformed_logs"
TRANSFORMER_SCRIPT="C:/Users/Khach/transformer_script.py"

# Ensure the transformed logs directory exists
mkdir -p "$TRANSFORMED_DIR"

# Step 1: Start QLog
echo "Starting QLog..."
$QCAT_PATH &
QLOG_PID=$!
echo "QLog started with PID $QLOG_PID."

# Step 2: Monitor for new QMDL files
echo "Monitoring directory for new QMDL files: $LOG_DIR"
while true; do
  # Check for the latest QMDL file
  NEW_FILE=$(ls -Art "$LOG_DIR"/*.qmdl 2>/dev/null | tail -n 1)
  
  if [[ -n "$NEW_FILE" ]]; then
    echo "New QMDL file detected: $NEW_FILE"

    # Step 3: Transform QMDL to text using QCAT
    TRANSFORMED_FILE="$TRANSFORMED_DIR/$(basename "$NEW_FILE" .qmdl).txt"
    echo "Transforming $NEW_FILE to $TRANSFORMED_FILE..."
    $QCAT_PATH --input "$NEW_FILE" --output "$TRANSFORMED_FILE"  # Adjust QCAT's CLI options if needed
    
    if [[ -f "$TRANSFORMED_FILE" ]]; then
      echo "Transformation successful: $TRANSFORMED_FILE"
      
      # Step 4: Send the transformed file to the local Windows machine
      echo "Transferring $TRANSFORMED_FILE to Windows machine..."
      scp "$TRANSFORMED_FILE" "$LOCAL_MACHINE_USER@$LOCAL_MACHINE_IP:\"$LOCAL_DESTINATION_PATH\""
      
      if [[ $? -eq 0 ]]; then
        echo "File transferred successfully to $LOCAL_MACHINE_IP:$LOCAL_DESTINATION_PATH"
        
        # Step 5: Execute the transformer script on Windows via SSH
        echo "Executing transformer script on Windows machine..."
        ssh "$LOCAL_MACHINE_USER@$LOCAL_MACHINE_IP" "python \"$TRANSFORMER_SCRIPT\" \"$LOCAL_DESTINATION_PATH/$(basename "$TRANSFORMED_FILE")\""
        
        if [[ $? -eq 0 ]]; then
          echo "Transformer script executed successfully."
        else
          echo "Error: Failed to execute transformer script on Windows machine."
        fi
      else
        echo "Error: File transfer to Windows machine failed."
      fi
    else
      echo "Error: Transformation failed for $NEW_FILE."
    fi

    # Exit after processing one file (or remove this line to keep monitoring continuously)
    break
  fi

  # Wait before checking again
  sleep 2
done

# Clean up
kill $QLOG_PID
echo "QLog process stopped."
