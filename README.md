# Pi_Linux_Node_Manager_for_Windows
A user-friendly graphical interface (GUI) for managing a Pi Network Node running on a Linux server, directly from your Windows computer.  This tool simplifies common tasks like installation, upgrades, status monitoring, and auto-updates, eliminating the need for manual SSH commands. 

✨ Features

    🌐 Easy Connection Management: Auto-Save your server's IP address and username for quick connections.

    🇩🇪 / 🇬🇧 Multi-Language Support: Switch between English and German on the fly.

    📊 Live Node Status: Automatically fetches and displays your node's status (e.g., Synced!, Catching-up, Stopped) with color-coded feedback.

    🚀 One-Click Installation: Executes a complete installation script for new nodes on Debian-based systems (like Ubuntu), including Docker and all prerequisites.

    ⬆️ One-Click Upgrade: Safely upgrades your pre-existing node by backing up configurations and using the new pi-node command-line interface (CLI).

    ⚙️ Auto-Update Control: Easily enable, disable, or schedule daily automatic updates for your Pi Node via cron jobs.

    🖥️ Server Reboot: A convenient button to restart your server directly from the application.

    📜 Detailed Action Log: See the real-time output of server commands directly within the tool.

🔧 How It Works

The application uses the Paramiko library in Python to establish a secure SSH connection to your Linux server. Once connected, it executes predefined shell scripts to perform the various management tasks.

    Installation: The script follows the official Pi Network procedure by adding the apt repository, installing the pi-node package, and then initializing it.

    Upgrade: The script intelligently locates your existing node directory, extracts crucial configuration details (like your NODE_SEED), backs up the data, and re-initializes the node with the latest version.

    Status Checks: It periodically runs pi-node status and pi-node --version to keep the UI updated with the latest information.

📋 Prerequisites

On your Windows PC:

    Windows 7 or later.

    If running from source: Python 3.8+

On your Linux Server:

    A Debian-based operating system (e.g., Ubuntu 20.04+, Debian 10+).

    An active SSH server.

    A user account with sudo privileges.

🚀 Getting Started

There are two ways to use this application.

Option A: Download the Executable (Recommended)

    Go to the Releases section of this GitHub repository.

    Download the latest .exe file (e.g., Pi_Linux_Node_Manager_for_Windows.exe).

    Run the executable. No installation is required.

Option B: Run from Python Source

If you have Python installed and prefer to run the script directly:

    Clone the repository:
    Bash

git clone https://github.com/Fingerkrampf/Pi_Linux_Node_Manager_for_Windows.git
cd Pi_Linux_Node_Manager_for_Windows

Install the required Python libraries:
Bash

pip install customtkinter paramiko

Run the script:
Bash

    python Pi_Linux_Node_Manager_for_Windows.py

⚙️ Configuration

The application will automatically create a config.json file in the same directory. This file stores your last used IP address, username, language preference, and auto-update time settings so you don't have to enter them every time.

⚠️ Disclaimer

This program is free software and is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY. Functions like "Install Node", "Upgrade Node", and "Reboot Server" make significant changes to your server.

Always back up your important data before performing major operations. The author is not responsible for any data loss or server issues that may arise from using this tool. Use at your own risk.

📄 License

This project is licensed under the GNU General Public License v3.0. See the LICENSE file for more details.

👤 Author & Contact

    Author: Fingerkrampf

    Contact & Support: Join the German Pi Network community on Telegram: t.me/PiNetzwerkDeutschland
