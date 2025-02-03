import netmiko
from netmiko import ConnectHandler, exceptions

devices = """188.121.96.126""".strip().splitlines()

device_type = 'linux'
username = 'ubuntu'
password = 'eurecom@2025'

netmiko_exceptions = (exceptions.NetmikoTimeoutException,
                      exceptions.NetmikoAuthenticationException)

for device in devices:
    try:
        print('~' * 79)
        print('Connecting to device:', device)
        connection = ConnectHandler(ip=device,
                                    device_type=device_type,
                                    username=username,
                                    password=password)
        
        command0 = (
            "cd /home/ubuntu/QCAT && "
            "touch /home/ubuntu/QCAT/Log-20250101.qmdl && "
        )
        command1 = (
            "scp /home/ubuntu/QCAT/Log-20250101.qmdl ubuntu@5.34.196.245:/home/ubuntu/QMDL/Log-20250101.qmdl"
        )
        
        # Use send_command_timing() to avoid prompt detection issues
        output0 = connection.send_command_timing(command0, delay_factor=2)
        print("Command output:")
        print(output0)
        output = connection.send_command_timing(command1, delay_factor=2)
        print("Command output:")
        print(output)
        
        connection.disconnect()
    except netmiko_exceptions as e:
        print('Failed to connect to device', device, ":", e)

