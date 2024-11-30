from netmiko import ConnectHandler

# Define the device parameters
device = {
    'device_type': 'VG3X0',  
    'host': '192.168.1.1',        
    'username': 'R1', 
    'password': 'cisco',   
    'secret': 'cisco',  
}

# Create a list of commands to run
commands = [
    'username november privilege 15 secret HelloWorld!',
]

# Establish a connection to the device
try:
    connection = ConnectHandler(**device)

    # Enter enable mode if required
    connection.enable()

    # Send the commands
    output = connection.send_config_set(commands)

    # Print the output
    print(output)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Disconnect from the device
    connection.disconnect()