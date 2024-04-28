# ServTrack

## Overview

ServTrack is a lightweight tool designed to ensure the smooth operation of critical services on a Linux system. It simplifies the process of monitoring service statuses, providing timely alerts if any services deviate from the expected state.

## Key Features

- **Automated Service Status Checks:** Effortlessly verifies the operational status of designated services.
- **Alerting Mechanism:** Instantly notifies users of any service anomalies or unexpected disruptions.
- **Flexible Configuration:** Customize which services to monitor and define acceptable operational thresholds.

## Requirements

- Linux-based operating system
- Python 3.x installed
- Install the required libraries using pip

## Installation

1. Clone or download the repository to your local environment.
2. Ensure Python 3.x is installed.
3. Install the Paramiko library by executing `pip install paramiko` in your terminal.

## Usage

1. Configure the `services_to_check` list in the `ServTrack.py` script to specify the services for monitoring.
2. If checking services on remote machines, input the relevant SSH connection details (hostname, username, password) in the `.env` file.
3. Run the `ServTrack.py` script.
4. Review the output to observe the status of the specified services.
5. If any services are not operating as expected, promptly address the issues to maintain system integrity.

## Configuration

### `.env` File

Adjust the `.env` file in the project directory to set the necessary environment variables for the script:

```dotenv
HOSTNAME=your_server_ip
USERNAME=your_username
PASSWORD=your_password
SENDER_EMAIL=your_email@gmail.com
RECEIVER_EMAIL=receiver_email@gmail.com
EMAIL_PASSWORD=your_email_password
```