# Pi Linux Node Manager für Windows

Eine benutzerfreundliche grafische Oberfläche (GUI) zur Verwaltung eines Pi Network Nodes, der auf einem Linux-Server läuft, direkt von Ihrem Windows-Computer aus.

Dieses Tool vereinfacht gängige Aufgaben wie die Installation, Upgrades, Statusüberwachung und Auto-Updates und macht die manuelle Eingabe von SSH-Befehlen überflüssig.

![Bild des Pi Linux Node Managers](https://raw.githubusercontent.com/Fingerkrampf/Pi_Linux_Node_Manager_for_Windows/main/assets/pi-node-manager-screenshot.png)
*(Die Benutzeroberfläche des Pi Linux Node Managers zeigt Verbindungsdetails, den Node-Status und das Aktionsprotokoll.)*

---

## ✨ Funktionen

* **🌐 Einfache Verbindungsverwaltung**: Speichern Sie die IP-Adresse und den Benutzernamen Ihres Servers für schnelle Verbindungen.
* **🇩🇪 / 🇬🇧 Mehrsprachige Unterstützung**: Wechseln Sie jederzeit zwischen Deutsch und Englisch.
* **📊 Live-Node-Status**: Ruft den Status Ihres Nodes (z. B. `Synced!`, `Catching-up`, `Stopped`) automatisch ab und zeigt ihn mit farbcodiertem Feedback an.
* **🚀 Ein-Klick-Installation**: Führt ein vollständiges Installationsskript für neue Nodes auf Debian-basierten Systemen (wie Ubuntu) aus, einschließlich Docker und aller Voraussetzungen.
* **⬆️ Ein-Klick-Upgrade**: Aktualisiert Ihren bereits bestehenden Node sicher, indem Konfigurationen gesichert und die neue `pi-node` Befehlszeilenschnittstelle (CLI) verwendet wird.
* **⚙️ Auto-Update-Steuerung**: Aktivieren, deaktivieren oder planen Sie ganz einfach tägliche automatische Updates für Ihren Pi Node über Cron-Jobs.
* **🖥️ Server-Neustart**: Eine praktische Schaltfläche, um Ihren Server direkt aus der Anwendung neu zu starten.
* **📜 Detailliertes Aktionsprotokoll**: Sehen Sie die Echtzeitausgabe von Serverbefehlen direkt in der App, ideal zur Fehlerbehebung.

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

* Ein **Debian-basiertes** Betriebssystem (z. B. Ubuntu 20.04+, Debian 10+).
* Ein aktiver SSH-Server.
* Ein Benutzerkonto mit `sudo`-Rechten.

---

## 🚀 Erste Schritte

Es gibt zwei Möglichkeiten, diese Anwendung zu nutzen.

### Option A: Die ausführbare Datei herunterladen (Empfohlen)

1.  Gehen Sie zum Abschnitt **[Releases](https://github.com/Fingerkrampf/Pi_Linux_Node_Manager_for_Windows/releases)** dieses GitHub-Repositorys.
2.  Laden Sie die neueste `.exe`-Datei herunter (z. B. `Pi_Linux_Node_Manager_for_Windows_v1.0.exe`).
3.  Führen Sie die Datei aus. Es ist keine Installation erforderlich.

### Option B: Aus dem Python-Quellcode ausführen

Wenn Sie Python installiert haben und das Skript lieber direkt ausführen möchten:

1.  **Klonen Sie das Repository:**
    Öffnen Sie eine Kommandozeile oder ein Terminal und führen Sie den folgenden Git-Befehl aus, um den Quellcode herunterzuladen.
    ```sh
    git clone [https://github.com/Fingerkrampf/Pi_Linux_Node_Manager_for_Windows.git](https://github.com/Fingerkrampf/Pi_Linux_Node_Manager_for_Windows.git)
    cd Pi_Linux_Node_Manager_for_Windows
    ```

2.  **Installieren Sie die Abhängigkeiten:**
    Die Anwendung benötigt zwei Hauptbibliotheken: `customtkinter` für die Benutzeroberfläche und `paramiko` für die SSH-Verbindung. Installieren Sie diese mit pip.
    ```sh
    pip install customtkinter paramiko
    ```

3.  **Führen Sie das Skript aus:**
    Sobald die Abhängigkeiten installiert sind, können Sie die Anwendung starten, indem Sie das Python-Skript ausführen.
    ```sh
    python Pi_Linux_Node_Manager_for_Windows.py
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
