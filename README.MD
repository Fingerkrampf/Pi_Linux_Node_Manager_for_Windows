![Screenshot](screenshot/Screenshot%202025-08-30%20113859.png)


<details>
<summary><strong>English Version</strong> (Click to expand)</summary>
<br>

# Pi Linux Node Manager for Windows

A user-friendly graphical user interface (GUI) for managing a Pi Network Node running on a Linux server, directly from your Windows computer.

This tool simplifies common tasks like installation, upgrades, status monitoring, and auto-updates, eliminating the need for manual SSH command entry.

*(The user interface of the Pi Linux Node Manager shows connection details, node status, and the action log.)*

---

## ✨ Features

* **🌐 Easy Connection Management**: Auto-saves your server's IP address and username for quick connections.
* **🇩🇪 / 🇬🇧 Multilingual Support**: Switch between German and English at any time.
* **📊 Live Node Status**: Automatically fetches and displays your node's status (e.g., `Synced!`, `Catching-up`, `Stopped`) with color-coded feedback.
* **🚀 One-Click Installation**: Executes a full installation script for new nodes on Debian-based systems (like Ubuntu), including Docker and all prerequisites.
* **⬆️ One-Click Upgrade**: Safely updates your existing node by backing up configurations and using the new `pi-node` command-line interface (CLI).
* **⚙️ Auto-Update Control**: Easily enable, disable, or schedule daily automatic updates for your Pi Node via cron jobs.
* **🖥️ Server Reboot**: A convenient button to restart your server directly from the application.

---

## 🔧 How It Works

The application uses the **Paramiko** library in Python to establish a secure SSH connection to your Linux server. Once connected, it executes predefined shell scripts to perform the various management tasks.

* **Installation**: The script follows the official Pi Network procedure by adding the `apt` repository, installing the `pi-node` package, and then initializing it.
* **Upgrade**: The script intelligently finds your existing node directory, extracts important configuration details (like your `NODE_SEED`), backs up the data, and re-initializes the node with the latest version.
* **Status Checks**: It regularly runs `pi-node status` and `pi-node --version` to keep the UI updated with the latest information.

---

## 📋 Prerequisites

### On your Windows PC:

* Windows 7 or newer.
* If running from source: Python 3.8+

### On your Linux Server:

* A **Debian-based** operating system (e.g., Ubuntu 20.04+, Debian 13+).
* An active SSH server.
* A user account with `sudo` privileges.

---

## 🚀 Getting Started

There are two ways to use this application.

### Option A: Download the Executable (Recommended)

1.  Go to the **[Releases](https://github.com/Fingerkrampf/Pi_Linux_Node_Manager_for_Windows/releases)** section of this GitHub repository.
2.  Download the latest `.exe` file (e.g., `Pi_Linux_Node_Manager_for_Windows.exe`).
3.  Run the file. No installation is required.

### Option B: Run from Python Source Code

If you have Python installed and prefer to run the script directly:

1.  **Clone the Repository:**
    Open a command prompt or terminal and run the following Git command to download the source code.
    ```sh
    git clone https://github.com/Fingerkrampf/Pi_Linux_Node_Manager_for_Windows.git
    cd Pi_Linux_Node_Manager_for_Windows
    ```

2.  **Install Dependencies:**
    The application requires two main libraries: `customtkinter` for the UI and `paramiko` for the SSH connection. Install them using pip.
    ```sh
    pip install customtkinter paramiko json threading time os sys
    ```

3.  **Run the Script:**
    Once the dependencies are installed, you can start the application by running the Python script.
    ```sh
    python Pi_Linux_Node_Manager_for_Window_v101.py
    ```

---

## ⚙️ Configuration

The application automatically creates a `config.json` file in the same directory. This file stores your last-used IP address, username, language preference, and auto-update time, so you don't have to re-enter them on every launch.

---

## ⚠️ Disclaimer

This program is free software and is distributed in the hope that it will be useful, but **WITHOUT ANY WARRANTY**. Features like "Install Node," "Update Node," and "Reboot Server" make significant changes to your server.

**Always create a backup of your important data before performing major operations.** The author is not responsible for any data loss or server issues that may arise from using this tool. Use at your own risk.

---

## 📄 License

This project is licensed under the **GNU General Public License v3.0**. See the `LICENSE` file for more details.

---

## 👤 Author & Contact

* **Author:** Fingerkrampf
* **Contact & Support:** Join the German Pi Network community on Telegram: [t.me/PiNetzwerkDeutschland](https://t.me/PiNetzwerkDeutschland)
</details>

<details>
<summary><strong>Deutsche Version</strong> (Klicken zum Ausklappen)</summary>
<br>

# Pi Linux Node Manager für Windows

Eine benutzerfreundliche grafische Oberfläche (GUI) zur Verwaltung eines Pi Network Nodes, der auf einem Linux-Server läuft, direkt von Ihrem Windows-Computer aus.

Dieses Tool vereinfacht gängige Aufgaben wie die Installation, Upgrades, Statusüberwachung und Auto-Updates und macht die manuelle Eingabe von SSH-Befehlen überflüssig.

*(Die Benutzeroberfläche des Pi Linux Node Managers zeigt Verbindungsdetails, den Node-Status und das Aktionsprotokoll.)*

---

## ✨ Funktionen

* **🌐 Einfache Verbindungsverwaltung**: Auto-Speichert die IP-Adresse und den Benutzernamen Ihres Servers für schnelle Verbindungen.
* **🇩🇪 / 🇬🇧 Mehrsprachige Unterstützung**: Wechseln Sie jederzeit zwischen Deutsch und Englisch.
* **📊 Live-Node-Status**: Ruft den Status Ihres Nodes (z. B. `Synced!`, `Catching-up`, `Stopped`) automatisch ab und zeigt ihn mit farbcodiertem Feedback an.
* **🚀 Ein-Klick-Installation**: Führt ein vollständiges Installationsskript für neue Nodes auf Debian-basierten Systemen (wie Ubuntu) aus, einschließlich Docker und aller Voraussetzungen.
* **⬆️ Ein-Klick-Upgrade**: Aktualisiert Ihren bereits bestehenden Node sicher, indem Konfigurationen gesichert und die neue `pi-node` Befehlszeilenschnittstelle (CLI) verwendet wird.
* **⚙️ Auto-Update-Steuerung**: Aktivieren, deaktivieren oder planen Sie ganz einfach tägliche automatische Updates für Ihren Pi Node über Cron-Jobs.
* **🖥️ Server-Neustart**: Eine praktische Schaltfläche, um Ihren Server direkt aus der Anwendung neu zu starten.

---

## 🔧 Wie es funktioniert

Die Anwendung verwendet die **Paramiko**-Bibliothek in Python, um eine sichere SSH-Verbindung zu Ihrem Linux-Server herzustellen. Nach der Verbindung führt sie vordefinierte Shell-Skripte aus, um die verschiedenen Verwaltungsaufgaben durchzuführen.

* **Installation**: Das Skript folgt dem offiziellen Pi-Netzwerk-Verfahren, indem es das `apt`-Repository hinzufügt, das `pi-node`-Paket installiert und es anschließend initialisiert.
* **Upgrade**: Das Skript findet intelligent Ihr vorhandenes Node-Verzeichnis, extrahiert wichtige Konfigurationsdetails (wie Ihren `NODE_SEED`), sichert die Daten und initialisiert den Node mit der neuesten Version neu.
* **Statusprüfungen**: Es führt regelmäßig `pi-node status` und `pi-node --version` aus, um die Benutzeroberfläche mit den neuesten Informationen zu versorgen.

---

## 📋 Voraussetzungen

### Auf Ihrem Windows-PC:

* Windows 7 oder neuer.
* Falls Sie aus dem Quellcode ausführen: Python 3.8+

### Auf Ihrem Linux-Server:

* Ein **Debian-basiertes** Betriebssystem (z. B. Ubuntu 20.04+, Debian 13+).
* Ein aktiver SSH-Server.
* Ein Benutzerkonto mit `sudo`-Rechten.

---

## 🚀 Erste Schritte

Es gibt zwei Möglichkeiten, diese Anwendung zu nutzen.

### Option A: Die ausführbare Datei herunterladen (Empfohlen)

1.  Gehen Sie zum Abschnitt **[Releases](https://github.com/Fingerkrampf/Pi_Linux_Node_Manager_for_Windows/releases)** dieses GitHub-Repositorys.
2.  Laden Sie die neueste `.exe`-Datei herunter (z. B. `Pi_Linux_Node_Manager_for_Windows.exe`).
3.  Führen Sie die Datei aus. Es ist keine Installation erforderlich.

### Option B: Aus dem Python-Quellcode ausführen

Wenn Sie Python installiert haben und das Skript lieber direkt ausführen möchten:

1.  **Klonen Sie das Repository:**
    Öffnen Sie eine Kommandozeile oder ein Terminal und führen Sie den folgenden Git-Befehl aus, um den Quellcode herunterzuladen.
    ```sh
    git clone https://github.com/Fingerkrampf/Pi_Linux_Node_Manager_for_Windows.git
    cd Pi_Linux_Node_Manager_for_Windows
    ```

2.  **Installieren Sie die Abhängigkeiten:**
    Die Anwendung benötigt zwei Hauptbibliotheken: `customtkinter` für die Benutzeroberfläche und `paramiko` für die SSH-Verbindung. Installieren Sie diese mit pip.
    ```sh
    pip install customtkinter paramiko json threading time os sys
    ```

3.  **Führen Sie das Skript aus:**
    Sobald die Abhängigkeiten installiert sind, können Sie die Anwendung starten, indem Sie das Python-Skript ausführen.
    ```sh
    python Pi_Linux_Node_Manager_for_Window_v101.py
    ```

---

## ⚙️ Konfiguration

Die Anwendung erstellt automatisch eine `config.json`-Datei im selben Verzeichnis. Diese Datei speichert Ihre zuletzt verwendete IP-Adresse, Ihren Benutzernamen, Ihre Spracheinstellung und die Zeit für das Auto-Update, sodass Sie diese nicht bei jedem Start erneut eingeben müssen.

---

## ⚠️ Haftungsausschluss

Dieses Programm ist freie Software und wird in der Hoffnung verbreitet, dass es nützlich sein wird, aber **OHNE JEGLICHE GEWÄHRLEISTUNG**. Funktionen wie "Node Installieren", "Node Updaten" und "Server Neustarten" nehmen erhebliche Änderungen an Ihrem Server vor.

**Erstellen Sie immer eine Sicherung Ihrer wichtigen Daten, bevor Sie größere Operationen durchführen.** Der Autor ist nicht für Datenverluste oder Serverprobleme verantwortlich, die durch die Nutzung dieses Tools entstehen könnten. Die Verwendung erfolgt auf eigenes Risiko.

---

## 📄 Lizenz

Dieses Projekt ist unter der **GNU General Public License v3.0** lizenziert. Weitere Details finden Sie in der `LICENSE`-Datei.

---

## 👤 Autor & Kontakt

* **Autor:** Fingerkrampf
* **Kontakt & Support:** Treten Sie der deutschen Pi-Netzwerk-Community auf Telegram bei: [t.me/PiNetzwerkDeutschland](https://t.me/PiNetzwerkDeutschland)
</details>
