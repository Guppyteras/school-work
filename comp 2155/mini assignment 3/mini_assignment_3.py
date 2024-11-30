import paramiko
import datetime

class SSHClient:
    def __init__(self, hostname, port, username, password):
        """Constructor to initialize the SSH client."""
        self.__hostname = hostname
        self.__port = port
        self.__username = username
        self.__password = password
        self.__client = None
        self.__shell = None
        self.connect()

    def __del__(self):
        """Destructor to close the SSH connection."""
        self.close_connection()

    def connect(self):
        """Connect to an SSH Client using a Paramiko client."""
        self.__client = paramiko.SSHClient()
        self.__client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.__client.connect(self.__hostname, port=self.__port, username=self.__username, password=self.__password)
        print("Connected to the SSH server.")

    def open_shell(self):
        """Evoking a shell from an SSH Client connection."""
        self.__shell = self.__client.invoke_shell()
        print("Shell opened.")

    def send_command_via_shell(self, command):
        """Send a command using the Shell."""
        self.__shell.send(command + '\n')
        output = self.__shell.recv(1024).decode('utf-8')
        return output

    def send_command_via_exec(self, command):
        """Send a command-line command using exec_command method."""
        stdin, stdout, stderr = self.__client.exec_command(command)
        output = stdout.read().decode('utf-8')
        return output

    def save_output(self, command, output):
        """Save either the shell or exec_command output."""
        now = datetime.datetime.now()
        filename = f"command_{now.strftime('%d_%B_%Y-%H%M')}.txt"
        with open(filename, 'w') as f:
            f.write(f"Command: {command}\n")
            f.write("Output:\n")
            f.write(output)
        print(f"Output saved to {filename}.")

    def close_connection(self):
        """Closing the connection."""
        if self.__shell:
            self.__shell.close()
        if self.__client:
            self.__client.close()
        print("Connection closed.")


if __name__ == "__main__":
    
    ssh_client = SSHClient(hostname='10.0.0.250', port=22, username='admin', password='admin')
    
    try:
        ssh_client.open_shell()
        
        # Sending a command via shell
        shell_output = ssh_client.send_command_via_shell('ls')
        ssh_client.save_output('ls', shell_output)
        
        # Sending a command via exec_command
        exec_output = ssh_client.send_command_via_exec('pwd')
        ssh_client.save_output('pwd', exec_output)
    finally:
        ssh_client.close_connection()