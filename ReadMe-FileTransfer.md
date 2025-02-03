# Netmiko SCP Automation Script

This Python script uses [Netmiko](https://github.com/ktbyers/netmiko) to connect to one or more remote Linux devices, execute commands to create a file, and then copy that file to a remote server via SCP.

## Overview

For each device listed, the script:

1. **Connects to the Device:**  
   Uses Netmiko's `ConnectHandler` to establish an SSH connection to a Linux device.

2. **Executes Commands:**
   - **Command 0:**  
     Changes the directory to `/home/ubuntu/QCAT` and creates an empty file named `Log-20250101.qmdl`.
   - **Command 1:**  
     Uses SCP to transfer the created file from the device to a remote server (`5.34.196.245`) into `/home/ubuntu/QMDL/`.

3. **Handles Errors:**  
   Catches connection and authentication issues with Netmiko's exception classes (`NetmikoTimeoutException` and `NetmikoAuthenticationException`).

## Download File

You can download the script file in several ways:

### Direct Download

Click the link below to download the raw Python script file directly:

- [Download script.py](https://github.com/yourusername/yourrepository/raw/main/script.py)

*(Replace the URL above with the actual link to your file in your repository.)*

### Clone the Repository

Alternatively, you can clone the entire repository:

```bash
git clone https://github.com/yourusername/yourrepository.git
cd yourrepository
