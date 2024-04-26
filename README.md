# Linux Services Sanity Checker

## Overview

The Linux Services Sanity Checker is a tool designed to ensure the proper functioning of essential services on a Linux system. It automates the process of checking the status of specified services and alerts the user if any of the services are not running as expected.

## Features

- **Service Status Check:** Automatically checks the status of specified services on the Linux system.
- **Alerting Mechanism:** Alerts the user if any of the services are not running or are in an unexpected state.
- **Customizable Configuration:** Allows users to specify which services to monitor and set thresholds for acceptable states.

## Requirements

- Linux-based operating system
- Python 3.x installed
- Paramiko library (`pip install paramiko`) for SSH connections (if checking services on remote machines)

## Installation

1. Clone or download the repository to your local machine.
2. Ensure Python 3.x is installed on your system.
3. Install the Paramiko library by running `pip install paramiko` in your terminal.

## Usage

1. Configure the `services_to_check` list in the `sanity_checker.py` script to specify which services you want to monitor.
2. If checking services on remote machines, provide the appropriate SSH connection details (hostname, username, password) in the script.
3. Run the `sanity_checker.py` script.
4. View the output to see the status of the specified services.
5. If any services are not running as expected, take appropriate action to troubleshoot and resolve the issue.

## Example

```bash
python sanity_checker.py
```

## Configuration

### `services_to_check` List

Edit the `services_to_check` list in the `sanity_checker.py` script to specify which services you want to monitor. Each item in the list should be a string representing the name of a service.

```python
services_to_check = ['apache2', 'nginx', 'mysql']
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need for a simple tool to monitor essential services on Linux systems.

---

Feel free to customize this README according to your specific implementation and preferences!
