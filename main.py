import paramiko


def check_service_status(hostname, username, password, service):
    # SSH client setup
    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            # Connect to the SSH server
            ssh_client.connect(hostname=hostname, username=username, password=password)

            # Command to check service status
            command = f"systemctl is-active {service}"

            # Execute the command
            stdin, stdout, stderr = ssh_client.exec_command(command)

            # Check the exit status of the command
            exit_status = stdout.channel.recv_exit_status()

            # Determine service status based on exit status
            if exit_status == 0:
                return f"{service}: Running"
            else:
                return f"{service}: Not running"

        except paramiko.AuthenticationException:
            return "Authentication failed. Please check your credentials."
        except paramiko.SSHException as e:
            return f"SSH error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"


def main():
    # Configuration
    hostname = "your_server_ip"
    username = "your_username"
    password = "your_password"
    services_to_check = ['apache2', 'nginx', 'mysql']

    # Check service status for each service
    for service in services_to_check:
        status = check_service_status(hostname, username, password, service)
        print(status)


if __name__ == "__main__":
    main()
