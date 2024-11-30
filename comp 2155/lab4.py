import paramiko

def ssh_connect(host, port, username, password, commands):
    # Initialize the SSH client
    client = paramiko.SSHClient()
    
    # Automatically add the server's SSH key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
        # Connect to the server
        client.connect(host, port=port, username=username, password=password)

        # Execute commands
        for command in commands:
            stdin, stdout, stderr = client.exec_command(command)
            print(f"Executing: {command}")
            print(f"Output: {stdout.read().decode()}")
            print(f"Errors: {stderr.read().decode()}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the connection
        client.close()


if __name__ == "__main__":
    host = "10.0.0.250"  
    port = 22  # Default SSH port
    username = "caporuscio.amedeo@gmail.com"  
    password = "Ak47reflex_"  

    
    commands = [
        "show version",  # Cisco router command
        "uname -a"       # Ubuntu command
    ]

    ssh_connect(host, port, username, password, commands)