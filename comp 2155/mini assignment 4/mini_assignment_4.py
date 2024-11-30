from netmiko import ConnectHandler

# Task 1: Create three text files with router configuration
for i in range(1, 4):
    file_name = f"router_{i}.txt"
    with open(file_name, "w") as file:
        file.write(f"Host of router: 192.168.1.{i}\n")  
        file.write("Username to connect to router: R1\n")  
        file.write("Password to connect to router: cisco\n")  
        file.write("Port of router: 22\n")  
print("Router configuration files created.")

# Task 2: Create a text file for OSPF configuration
with open("ospf_routing_protocol.txt", "w") as ospf_file:
    ospf_file.write("router ospf 1\n")
    ospf_file.write("network 0.0.0.0 0.0.0.0 area 0\n")
    ospf_file.write("distance 110\n")  
    ospf_file.write("default-information originate\n")  
print("OSPF routing protocol file created.")

# Task 3: Connect to routers using Netmiko and apply OSPF configuration
# Router details
routers = [
    {
        "device_type": "VG3X0",  
        "host": f"192.168.1.{i}",  
        "username": "R1",  
        "password": "cisco",  
        "port": 22,  
        "secret": "cisco"  
    }
    for i in range(1, 4)
]

# Read OSPF commands from the file
with open("ospf_routing_protocol.txt", "r") as ospf_file:
    ospf_commands = ospf_file.readlines()

# Apply OSPF configuration to each router
for router in routers:
    try:
        print(f"Connecting to {router['host']}...")
        connection = ConnectHandler(**router)
        connection.enable()  # Enter privileged mode
        output = connection.send_config_set(ospf_commands)
        print(f"OSPF configuration applied to {router['host']}:\n{output}")
        connection.disconnect()
    except Exception as e:
        print(f"Failed to connect to {router['host']}: {e}")

print("Configuration complete.")
