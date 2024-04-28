import paramiko
import smtplib
from email.mime.text import MIMEText
from dotenv import dotenv_values


def check_service_status(hostname, username, password, service):
    with paramiko.SSHClient() as ssh_client:
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh_client.connect(hostname=hostname, username=username, password=password)

            # Command to check service status
            command = f"systemctl is-active {service}"

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


def send_alert_email(sender_email, receiver_email, password, service_name):
    subject = f"Service Alert: {service_name} is not running"
    body = f"The {service_name} service is not running on the server."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, password)
        server.send_message(msg)


def main():
    # Load environment variables from .env file
    config = dotenv_values('.env')

    # Configuration
    hostname = config.get('HOSTNAME')
    username = config.get('USERNAME')
    password = config.get('PASSWORD')
    services_to_check = ['apache2', 'nginx', 'mysql']
    sender_email = config.get('SENDER_EMAIL')
    receiver_email = config.get('RECEIVER_EMAIL')
    email_password = config.get('EMAIL_PASSWORD')

    # Check service status for each service
    for service in services_to_check:
        status = check_service_status(hostname, username, password, service)
        print(status)
        if "Not running" in status:
            send_alert_email(sender_email, receiver_email, email_password, service)


if __name__ == "__main__":
    main()
