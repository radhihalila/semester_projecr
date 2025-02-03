# Automation Execution and File Transfer using SCP

This project demonstrates an automation process that connects to a remote Linux device using Netmiko, executes a series of commands to create a file, and then transfers that file to another server using SCP.

## Technical Details

- **Programming Language:** Python 3  
- **Library Used:** [Netmiko](https://github.com/ktbyers/netmiko)  
- **Device Type:** Linux  
- **Key Modules:**  
  - `ConnectHandler` for establishing SSH connections.
  - `exceptions` to handle connection and authentication issues.
- **Error Handling:**  
  The script handles `NetmikoTimeoutException` and `NetmikoAuthenticationException` to ensure robust connections.

## Automation Process

1. **Device Connection:**  
   The script reads a list of device IP addresses and connects to each using SSH.

2. **Command Execution:**  
   - **First Command:**  
     Navigates to a specific directory (`/home/ubuntu/QCAT`) and creates a file (`Log-20250101.qmdl`).
   - **Second Command:**  
     Uses SCP to transfer the newly created file to a remote server at IP `5.34.196.245`, placing it in `/home/ubuntu/QMDL/`.

3. **Feedback and Error Handling:**  
   - The script prints the output of each executed command.
   - In the event of a connection or authentication error, the script logs the error and continues with the next device.

## Environment Setup

Before running the script, ensure the following:

1. **Python Installation:**  
   Make sure Python 3.6+ is installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Install Netmiko:**  
   Install the Netmiko library using pip:
   ```bash
   pip install netmiko
