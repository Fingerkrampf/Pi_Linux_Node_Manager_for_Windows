#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Pi Linux Node Manager for Windows v1.2
Copyright (C) 2025 Fingerkrampf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: t.me/PiNetzwerkDeutschland

----------------------------------------------------------------

Pi Linux Node Manager für Windows v1.2
Copyright (C) 2025 Fingerkrampf

Dieses Programm ist freie Software: Sie können es unter den Bedingungen
der GNU General Public License, wie von der Free Software Foundation,
Version 3 der Lizenz oder (nach Ihrer Wahl) jeder neueren
veröffentlichten Version, weiterverteilen und/oder modifizieren.

Dieses Programm wird in der Hoffnung bereitgestellt, dass es nützlich sein wird,
aber OHNE JEDE GEWÄHRLEISTUNG; sogar ohne die implizite
Gewährleistung der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
Siehe die GNU General Public License für weitere Details.

Sie sollten eine Kopie der GNU General Public License zusammen mit diesem
Programm erhalten haben. Wenn nicht, siehe <https://www.gnu.org/licenses/>.

Kontakt: t.me/PiNetzwerkDeutschland
"""

import customtkinter as ctk
from tkinter import scrolledtext, messagebox, Menu
import paramiko
import json
import threading
import time
import os
import sys
import re

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

translations = {
    "de": {
        "title": "Pi Linux Node Manager für Windows v1.2 von Fingerkrampf @ t.me/PiNetzwerkDeutschland",
        "server_connection": "Serververbindung",
        "ip_address": "IP-Adresse",
        "username": "Benutzername",
        "password": "Passwort",
        "connect": "Verbinden",
        "disconnect": "Trennen",
        "connection_status": "Verbindungsstatus:",
        "not_connected": "Nicht verbunden",
        "connected_to": "Verbunden mit {}",
        "connecting": "Verbinde...",
        "auth_failed": "Authentifizierung fehlgeschlagen.",
        "connection_error": "Verbindungsfehler: {}",
        "node_management": "Node Verwaltung",
        "install_node": "Pi Node Installieren & Starten",
        "upgrade_node": "Bestehenden Node Upgraden",
        "node_version": "Installierte Version:",
        "unknown": "Unbekannt",
        "node_status_title": "NODE STATUS",
        "installation_log": "Aktions-Log",
        "install_confirm_title": "Installation Bestätigen",
        "install_confirm_msg": "Dies führt das neue Pi Node Installationsskript (via APT) auf Ihrem Server aus. Fortfahren?",
        "upgrade_confirm_title": "Upgrade Bestätigen",
        "upgrade_confirm_msg": "Dies versucht, einen bestehenden Node zu finden, seine Konfiguration zu sichern und ihn auf die neueste Version zu aktualisieren. Fortfahren?",
        "installation_started": "Installation gestartet...",
        "upgrade_started": "Upgrade gestartet...",
        "docker_check": "Prüfe und installiere Docker-Voraussetzungen...",
        "installation_complete": "Aktion abgeschlossen.",
        "pi_node_not_installed": "Pi Node scheint nicht installiert zu sein.",
        "os_unsupported": "FEHLER: Dieses Installationsskript ist nur für Debian-basierte Systeme (z.B. Ubuntu).",
        "settings": "Einstellungen",
        "language_toggle": "Sprache (DE/EN)",
        "appearance_toggle": "Darstellung (Hell/Dunkel)",
        "autoupdate_management": "Auto-Update",
        "enable_autoupdate": "Auto-Update Aktivieren",
        "disable_autoupdate": "Auto-Update Deaktivieren",
        "autoupdate_status": "Auto-Update Status:",
        "enabled": "Aktiviert",
        "disabled": "Deaktiviert",
        "checking": "Prüfe...",
        "enable_autoupdate_confirm": "Möchten Sie automatische Updates für den Pi Node aktivieren?",
        "disable_autoupdate_confirm": "Möchten Sie automatische Updates für den Pi Node deaktivieren?",
        "autoupdate_schedule": "Update Zeit (HH:MM):",
        "enable_autoupdate_confirm_schedule": "Möchten Sie tägliche automatische Updates für {}:{} Uhr aktivieren?",
        "invalid_time": "Ungültige Zeit",
        "invalid_time_msg": "Bitte geben Sie eine gültige Stunde (0-23) und Minute (0-59) ein.",
        "paste": "Einfügen",
        "server_actions": "Server Aktionen",
        "reboot_server": "Server Neustarten",
        "reboot_confirm_title": "Neustart Bestätigen",
        "reboot_confirm_msg": "Sind Sie sicher, dass Sie den gesamten Server neu starten möchten? Die Verbindung wird getrennt.",
        "system_status_title": "System Status",
        "cpu_load": "CPU Auslastung:",
        "ram_usage": "RAM Nutzung:",
        "disk_usage": "Speicherplatz (/):",
        "uptime": "Laufzeit:",
        "icon_load_error_title": "Icon Fehler",
        "icon_load_error_msg": "Konnte die Datei 'icon.ico' nicht laden. Stellen Sie sicher, dass die Datei im selben Ordner wie die Anwendung liegt und nicht beschädigt ist.",
        "backup_progress_info": "Dies kann bei großen Datenmengen eine Weile dauern. Der Fortschritt wird unten angezeigt:",
        "node_credentials_start": "Node Anmeldedaten ",
        "node_credentials_warning": "(NICHT TEILEN!)",
        "node_credentials_end": " (Klicken zum Kopieren)",
        "node_seed": "Node Seed:",
        "postgres_pw": "Postgres Passwort:",
        "copied": "Kopiert!"
    },
    "en": {
        "title": "Pi Linux Node Manager for Windows v1.2 by Fingerkrampf @ t.me/PiNetzwerkDeutschland",
        "server_connection": "Server Connection",
        "ip_address": "IP Address",
        "username": "Username",
        "password": "Password",
        "connect": "Connect",
        "disconnect": "Disconnect",
        "connection_status": "Connection Status:",
        "not_connected": "Not connected",
        "connected_to": "Connected to {}",
        "connecting": "Connecting...",
        "auth_failed": "Authentication failed.",
        "connection_error": "Connection error: {}",
        "node_management": "Node Management",
        "install_node": "Install & Start Pi Node",
        "upgrade_node": "Upgrade Pre-existing Node",
        "node_version": "Installed Version:",
        "unknown": "Unknown",
        "node_status_title": "NODE STATUS",
        "installation_log": "Action Log",
        "install_confirm_title": "Confirm Installation",
        "install_confirm_msg": "This will run the new Pi Node installation script (via APT) on your server. Continue?",
        "upgrade_confirm_title": "Confirm Upgrade",
        "upgrade_confirm_msg": "This will attempt to find a pre-existing node, back up its configuration, and upgrade it to the latest version. Continue?",
        "installation_started": "Installation started...",
        "upgrade_started": "Upgrade started...",
        "docker_check": "Checking and installing Docker prerequisites...",
        "installation_complete": "Action complete.",
        "pi_node_not_installed": "Pi Node does not seem to be installed.",
        "os_unsupported": "ERROR: This installation script is for Debian-based systems (like Ubuntu) only.",
        "settings": "Settings",
        "language_toggle": "Language (DE/EN)",
        "appearance_toggle": "Appearance (Light/Dark)",
        "autoupdate_management": "Auto-Update",
        "enable_autoupdate": "Enable Auto-Update",
        "disable_autoupdate": "Disable Auto-Update",
        "autoupdate_status": "Auto-Update Status:",
        "enabled": "Enabled",
        "disabled": "Disabled",
        "checking": "Checking...",
        "enable_autoupdate_confirm": "Do you want to enable automatic updates for the Pi Node?",
        "disable_autoupdate_confirm": "Do you want to disable automatic updates for the Pi Node?",
        "autoupdate_schedule": "Update Time (HH:MM):",
        "enable_autoupdate_confirm_schedule": "Enable daily automatic updates for {}:{}?",
        "invalid_time": "Invalid Time",
        "invalid_time_msg": "Please enter a valid hour (0-23) and minute (0-59).",
        "paste": "Paste",
        "server_actions": "Server Actions",
        "reboot_server": "Reboot Server",
        "reboot_confirm_title": "Confirm Reboot",
        "reboot_confirm_msg": "Are you sure you want to reboot the entire server? You will be disconnected.",
        "system_status_title": "System Status",
        "cpu_load": "CPU Load:",
        "ram_usage": "RAM Usage:",
        "disk_usage": "Disk Space (/):",
        "uptime": "Uptime:",
        "icon_load_error_title": "Icon Error",
        "icon_load_error_msg": "Could not load 'icon.ico'. Make sure the file is in the same folder as the application and is not corrupted.",
        "backup_progress_info": "This can take a while for large volumes. Progress will be shown below:",
        "node_credentials_start": "Node Credentials ",
        "node_credentials_warning": "(DO NOT SHARE!)",
        "node_credentials_end": " (Click to copy)",
        "node_seed": "Node Seed:",
        "postgres_pw": "Postgres Password:",
        "copied": "Copied!"
    }
}

class SSHManager:
    def __init__(self):
        self.ssh_client = None

    def connect(self, hostname, username, password):
        if self.ssh_client:
            self.disconnect()
        try:
            self.ssh_client = paramiko.SSHClient()
            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh_client.connect(hostname=hostname, username=username, password=password, timeout=10)
            return "success"
        except paramiko.AuthenticationException:
            self.ssh_client = None
            return "auth_failed"
        except Exception as e:
            self.ssh_client = None
            return str(e)

    def disconnect(self):
        if self.ssh_client:
            self.ssh_client.close()
            self.ssh_client = None

    def execute_command(self, command):
        if not self.ssh_client:
            return None, "Not connected"
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command)
            stdout_str = stdout.read().decode('utf-8').strip()
            stderr_str = stderr.read().decode('utf-8').strip()
            return stdout_str, stderr_str
        except Exception as e:
            return None, str(e)

    def execute_command_stream(self, command, callback):
        if not self.ssh_client:
            callback("Not connected")
            return
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(command, get_pty=True)
            for line in iter(stdout.readline, ""):
                callback(line.strip())
            for line in iter(stderr.readline, ""):
                callback(f"ERROR: {line.strip()}")
        except Exception as e:
            callback(f"FATAL ERROR: {str(e)}")


class PiNodeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.ssh_manager = SSHManager()
        self.status_thread = None
        self.stop_status_thread = threading.Event()
        self.config_file = "config.json"
        
        self.current_lang = ctk.StringVar(value="de")
        
        self.load_settings()
        
        self.setup_ui()
        self.current_lang.trace_add("write", self.update_language)
        self.update_language()
        
        self.load_connection_settings()
        
    def setup_ui(self):
        self.title("Pi Linux Node Manager for Windows v1.1")
        try:
            icon_path = resource_path('icon.ico')
            if not os.path.exists(icon_path):
                raise FileNotFoundError()
            self.iconbitmap(icon_path)
        except Exception as e:
            print(f"Could not load application icon: {e}")
        self.geometry("1100x950")
        self.grid_columnconfigure(0, weight=0, minsize=280)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        sidebar_frame = ctk.CTkFrame(self, width=280, corner_radius=0)
        sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
        sidebar_frame.grid_rowconfigure(5, weight=1)

        self.title_label = ctk.CTkLabel(sidebar_frame, text="Pi Linux Node Manager", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.conn_frame = ctk.CTkFrame(sidebar_frame, corner_radius=10)
        self.conn_frame.grid(row=1, column=0, padx=20, pady=10, sticky="ew")
        
        self.ip_entry = ctk.CTkEntry(self.conn_frame)
        self.ip_entry.pack(pady=(10, 5), padx=10, fill="x")
        self.user_entry = ctk.CTkEntry(self.conn_frame)
        self.user_entry.pack(pady=5, padx=10, fill="x")
        self.pw_entry = ctk.CTkEntry(self.conn_frame, show="*")
        self.pw_entry.pack(pady=5, padx=10, fill="x")

        self.ip_entry.bind("<Button-3>", lambda event: self._show_context_menu(event, self.ip_entry))
        self.user_entry.bind("<Button-3>", lambda event: self._show_context_menu(event, self.user_entry))
        self.pw_entry.bind("<Button-3>", lambda event: self._show_context_menu(event, self.pw_entry))

        self.connect_btn = ctk.CTkButton(self.conn_frame, command=self.toggle_connection)
        self.connect_btn.pack(pady=(10, 5), padx=10, fill="x")

        self.conn_status_label = ctk.CTkLabel(self.conn_frame, text="", text_color="gray")
        self.conn_status_label.pack(pady=(0, 10), padx=10)

        self.mgmt_frame = ctk.CTkFrame(sidebar_frame, corner_radius=10)
        self.mgmt_frame.grid(row=2, column=0, padx=20, pady=10, sticky="ew")
        
        self.install_btn = ctk.CTkButton(self.mgmt_frame, command=self.install_node)
        self.install_btn.pack(pady=(10, 5), padx=10, fill="x")
        self.upgrade_btn = ctk.CTkButton(self.mgmt_frame, command=self.upgrade_node)
        self.upgrade_btn.pack(pady=5, padx=10, fill="x")

        self.autoupdate_frame = ctk.CTkFrame(sidebar_frame, corner_radius=10)
        self.autoupdate_frame.grid(row=3, column=0, padx=20, pady=10, sticky="ew")
        
        self.autoupdate_status_label_desc = ctk.CTkLabel(self.autoupdate_frame, text="")
        self.autoupdate_status_label_desc.pack(pady=(10,0))
        self.autoupdate_status_label = ctk.CTkLabel(self.autoupdate_frame, text="---", font=ctk.CTkFont(weight="bold"))
        self.autoupdate_status_label.pack()

        self.autoupdate_schedule_frame = ctk.CTkFrame(self.autoupdate_frame, fg_color="transparent")
        self.autoupdate_schedule_frame.pack(pady=5, padx=10, fill="x")
        self.autoupdate_schedule_label = ctk.CTkLabel(self.autoupdate_schedule_frame, text="")
        self.autoupdate_schedule_label.pack(side="left", padx=(0,10))
        self.autoupdate_hour_entry = ctk.CTkEntry(self.autoupdate_schedule_frame, width=40)
        self.autoupdate_hour_entry.pack(side="left")
        self.autoupdate_hour_entry.insert(0, "02")
        ctk.CTkLabel(self.autoupdate_schedule_frame, text=":", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=5)
        self.autoupdate_minute_entry = ctk.CTkEntry(self.autoupdate_schedule_frame, width=40)
        self.autoupdate_minute_entry.pack(side="left")
        self.autoupdate_minute_entry.insert(0, "00")

        self.enable_autoupdate_btn = ctk.CTkButton(self.autoupdate_frame, command=self.enable_auto_update)
        self.enable_autoupdate_btn.pack(pady=(10, 5), padx=10, fill="x")
        self.disable_autoupdate_btn = ctk.CTkButton(self.autoupdate_frame, command=self.disable_auto_update)
        self.disable_autoupdate_btn.pack(pady=5, padx=10, fill="x")

        self.server_actions_frame = ctk.CTkFrame(sidebar_frame, corner_radius=10)
        self.server_actions_frame.grid(row=4, column=0, padx=20, pady=10, sticky="ew")
        self.server_actions_label = ctk.CTkLabel(self.server_actions_frame, text="", font=ctk.CTkFont(weight="bold"))
        self.server_actions_label.pack(pady=(10,5))
        self.reboot_btn = ctk.CTkButton(self.server_actions_frame, command=self.reboot_server, fg_color="#D32F2F", hover_color="#B71C1C")
        self.reboot_btn.pack(pady=(0,10), padx=10, fill="x")
        
        settings_frame = ctk.CTkFrame(sidebar_frame, corner_radius=10)
        settings_frame.grid(row=5, column=0, padx=20, pady=10, sticky="sew")
        settings_frame.grid_columnconfigure(1, weight=1)

        self.settings_label = ctk.CTkLabel(settings_frame, text="", font=ctk.CTkFont(weight="bold"))
        self.settings_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10,5), sticky="w")
        
        self.language_toggle_label = ctk.CTkLabel(settings_frame, text="")
        self.language_toggle_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.language_switch = ctk.CTkSwitch(settings_frame, text="", command=self.toggle_language, onvalue="en", offvalue="de")
        self.language_switch.grid(row=1, column=1, padx=10, pady=5, sticky="e")
        
        self.appearance_toggle_label = ctk.CTkLabel(settings_frame, text="")
        self.appearance_toggle_label.grid(row=2, column=0, padx=10, pady=(5,10), sticky="w")
        self.appearance_switch = ctk.CTkSwitch(settings_frame, text="", command=self.toggle_appearance_mode)
        self.appearance_switch.grid(row=2, column=1, padx=10, pady=(5,10), sticky="e")


        main_frame = ctk.CTkFrame(self, corner_radius=10)
        main_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")
        main_frame.grid_rowconfigure(4, weight=1) 
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)

        self.status_frame = ctk.CTkFrame(main_frame, corner_radius=10)
        self.status_frame.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")
        self.status_title_label = ctk.CTkLabel(self.status_frame, text="", font=ctk.CTkFont(size=12, weight="bold"))
        self.status_title_label.pack(padx=20, pady=(10,0))
        self.status_label = ctk.CTkLabel(self.status_frame, text="---", font=ctk.CTkFont(size=18, weight="bold"))
        self.status_label.pack(padx=20, pady=(0,10))
        
        version_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        version_frame.grid(row=1, column=0, padx=20, pady=(0,10), sticky="w")
        self.version_label_desc = ctk.CTkLabel(version_frame, text="")
        self.version_label_desc.pack(side="left")
        self.version_label = ctk.CTkLabel(version_frame, text="", font=ctk.CTkFont(weight="bold"))
        self.version_label.pack(side="left", padx=(5,0))
        
        self.credentials_frame = ctk.CTkFrame(main_frame, corner_radius=10)
        self.credentials_frame.grid(row=2, column=0, padx=20, pady=(0, 10), sticky="nsew")
        
        title_container_frame = ctk.CTkFrame(self.credentials_frame, fg_color="transparent")
        title_container_frame.pack(pady=(10,5), padx=10, anchor="w")

        self.credentials_start_label = ctk.CTkLabel(title_container_frame, text="", font=ctk.CTkFont(weight="bold"))
        self.credentials_start_label.pack(side="left")

        self.credentials_warning_label = ctk.CTkLabel(title_container_frame, text="", text_color="#FF5733") 
        self.credentials_warning_label.pack(side="left")

        self.credentials_end_label = ctk.CTkLabel(title_container_frame, text="", font=ctk.CTkFont(weight="bold"))
        self.credentials_end_label.pack(side="left")

        self.seed_desc_label = ctk.CTkLabel(self.credentials_frame, text="")
        self.seed_desc_label.pack(padx=10, pady=(5,0), anchor="w")
        self.seed_value_label = ctk.CTkLabel(self.credentials_frame, text="---", fg_color=("#e5e5e5", "#212121"), corner_radius=5, anchor="w", justify="left", wraplength=0)
        self.seed_value_label.pack(pady=(0, 5), padx=10, fill="x")
        self.seed_value_label.bind("<Button-1>", lambda e: self._copy_to_clipboard(self.seed_value_label))

        self.postgres_desc_label = ctk.CTkLabel(self.credentials_frame, text="")
        self.postgres_desc_label.pack(padx=10, pady=(5,0), anchor="w")
        self.postgres_value_label = ctk.CTkLabel(self.credentials_frame, text="---", fg_color=("#e5e5e5", "#212121"), corner_radius=5, anchor="w", justify="left", wraplength=0)
        self.postgres_value_label.pack(pady=(0, 10), padx=10, fill="x")
        self.postgres_value_label.bind("<Button-1>", lambda e: self._copy_to_clipboard(self.postgres_value_label))
        
        self.credentials_frame.grid_remove()
        
        self.system_status_frame = ctk.CTkFrame(main_frame, corner_radius=10)
        self.system_status_frame.grid(row=0, column=1, padx=(0, 20), pady=(20, 10), rowspan=3, sticky="nsew")
        self.system_status_frame.grid_columnconfigure(1, weight=1)

        self.system_status_title_label = ctk.CTkLabel(self.system_status_frame, text="", font=ctk.CTkFont(size=12, weight="bold"))
        self.system_status_title_label.grid(row=0, column=0, columnspan=2, padx=10, pady=(10, 5), sticky="w")

        self.cpu_desc_label = ctk.CTkLabel(self.system_status_frame, text="")
        self.cpu_desc_label.grid(row=1, column=0, padx=10, pady=2, sticky="w")
        self.cpu_val_label = ctk.CTkLabel(self.system_status_frame, text="---", font=ctk.CTkFont(weight="bold"))
        self.cpu_val_label.grid(row=1, column=1, padx=10, pady=2, sticky="e")

        self.ram_desc_label = ctk.CTkLabel(self.system_status_frame, text="")
        self.ram_desc_label.grid(row=2, column=0, padx=10, pady=2, sticky="w")
        self.ram_val_label = ctk.CTkLabel(self.system_status_frame, text="---", font=ctk.CTkFont(weight="bold"))
        self.ram_val_label.grid(row=2, column=1, padx=10, pady=2, sticky="e")

        self.disk_desc_label = ctk.CTkLabel(self.system_status_frame, text="")
        self.disk_desc_label.grid(row=3, column=0, padx=10, pady=2, sticky="w")
        self.disk_val_label = ctk.CTkLabel(self.system_status_frame, text="---", font=ctk.CTkFont(weight="bold"))
        self.disk_val_label.grid(row=3, column=1, padx=10, pady=2, sticky="e")

        self.uptime_desc_label = ctk.CTkLabel(self.system_status_frame, text="")
        self.uptime_desc_label.grid(row=4, column=0, padx=10, pady=(2,10), sticky="w")
        self.uptime_val_label = ctk.CTkLabel(self.system_status_frame, text="---", font=ctk.CTkFont(weight="bold"))
        self.uptime_val_label.grid(row=4, column=1, padx=10, pady=(2,10), sticky="e")
        
        self.log_label = ctk.CTkLabel(main_frame, text="", font=ctk.CTkFont(size=14, weight="bold"))
        self.log_label.grid(row=3, column=0, columnspan=2, padx=20, pady=(10, 5), sticky="w")
        self.log_text_frame = ctk.CTkFrame(main_frame, corner_radius=10)
        self.log_text_frame.grid(row=4, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")
        
        self.log_text = scrolledtext.ScrolledText(self.log_text_frame, height=15, state='disabled', wrap=ctk.WORD,
                                                  relief="flat", borderwidth=0)
        self.log_text.pack(fill="both", expand=True, padx=1, pady=1)

        self.update_ui_state(connected=False)
        self._update_log_colors()

    def _update_log_colors(self):
        mode = ctk.get_appearance_mode()
        if mode == "Dark":
            bg_color = "#2B2B2B"
            fg_color = "white"
            insert_color = "white"
        else: 
            bg_color = "#EBEBEB"
            fg_color = "black"
            insert_color = "black"
        self.log_text.configure(bg=bg_color, fg=fg_color, insertbackground=insert_color)

    def toggle_language(self):
        new_lang = self.language_switch.get()
        self.current_lang.set(new_lang)

    def toggle_appearance_mode(self):
        if self.appearance_switch.get() == 1: 
            ctk.set_appearance_mode("Dark")
        else: 
            ctk.set_appearance_mode("Light")
        self._update_log_colors() 

    def update_language(self, *args):
        lang = self.current_lang.get()
        t = translations[lang]

        self.title(t["title"])
        
        self.settings_label.configure(text=t["settings"])
        self.language_toggle_label.configure(text=t["language_toggle"])
        self.appearance_toggle_label.configure(text=t["appearance_toggle"])

        self.ip_entry.configure(placeholder_text=t["ip_address"])
        self.user_entry.configure(placeholder_text=t["username"])
        self.pw_entry.configure(placeholder_text=t["password"])
        self.connect_btn.configure(text=t["connect"] if not self.ssh_manager.ssh_client else t["disconnect"])
        if not self.ssh_manager.ssh_client:
            self.conn_status_label.configure(text=t["not_connected"])

        self.install_btn.configure(text=t["install_node"])
        self.upgrade_btn.configure(text=t["upgrade_node"])
        
        self.credentials_start_label.configure(text=t["node_credentials_start"])
        self.credentials_warning_label.configure(
            text=t["node_credentials_warning"],
            font=ctk.CTkFont(weight="bold") 
)
        self.credentials_end_label.configure(text=t["node_credentials_end"])

        self.seed_desc_label.configure(text=t["node_seed"])
        self.postgres_desc_label.configure(text=t["postgres_pw"])

        self.autoupdate_status_label_desc.configure(text=t["autoupdate_status"])
        self.autoupdate_schedule_label.configure(text=t["autoupdate_schedule"])
        self.enable_autoupdate_btn.configure(text=t["enable_autoupdate"])
        self.disable_autoupdate_btn.configure(text=t["disable_autoupdate"])

        self.server_actions_label.configure(text=t["server_actions"])
        self.reboot_btn.configure(text=t["reboot_server"])
        
        self.version_label_desc.configure(text=t["node_version"])
        self.status_title_label.configure(text=t["node_status_title"])
        if self.version_label.cget("text") == translations["de"]["unknown"] or self.version_label.cget("text") == translations["en"]["unknown"]:
             self.version_label.configure(text=t["unknown"])
        self.log_label.configure(text=t["installation_log"])
        
        self.system_status_title_label.configure(text=t["system_status_title"])
        self.cpu_desc_label.configure(text=t["cpu_load"])
        self.ram_desc_label.configure(text=t["ram_usage"])
        self.disk_desc_label.configure(text=t["disk_usage"])
        self.uptime_desc_label.configure(text=t["uptime"])

    def update_ui_state(self, connected):
        state = 'normal' if connected else 'disabled'
        self.install_btn.configure(state=state)
        self.upgrade_btn.configure(state='disabled')
        self.enable_autoupdate_btn.configure(state=state)
        self.disable_autoupdate_btn.configure(state=state)
        self.reboot_btn.configure(state=state)
        
        entry_state = 'disabled' if connected else 'normal'
        self.ip_entry.configure(state=entry_state)
        self.user_entry.configure(state=entry_state)
        self.pw_entry.configure(state=entry_state)

        if not connected:
            self.autoupdate_status_label.configure(text="---", text_color="gray")
            self.enable_autoupdate_btn.configure(state='disabled')
            self.disable_autoupdate_btn.configure(state='disabled')
            self.autoupdate_hour_entry.configure(state='disabled')
            self.autoupdate_minute_entry.configure(state='disabled')
            self.credentials_frame.grid_remove()
            
    def _copy_to_clipboard(self, widget):
        t = translations[self.current_lang.get()]
        original_text = widget.cget("text")
        if original_text and original_text != "---" and original_text != t["copied"]:
            self.clipboard_clear()
            self.clipboard_append(original_text)
            
            original_color = widget.cget("text_color")
            widget.configure(text=t["copied"], text_color="#4CAF50")
            
            def restore_text():
                widget.configure(text=original_text, text_color=original_color)
            
            widget.after(1500, restore_text)

    def load_settings(self):
        try:
            with open(self.config_file, 'r') as f:
                settings = json.load(f)
                
                saved_mode = settings.get("appearance_mode", "Dark") 
                ctk.set_appearance_mode(saved_mode)

        except (FileNotFoundError, json.JSONDecodeError):
            ctk.set_appearance_mode("Dark")

    def load_connection_settings(self):
        try:
            with open(self.config_file, 'r') as f:
                settings = json.load(f)
                
                self.ip_entry.insert(0, settings.get("ip", ""))
                self.user_entry.insert(0, settings.get("user", ""))
                self.autoupdate_hour_entry.delete(0, ctk.END)
                self.autoupdate_hour_entry.insert(0, settings.get("autoupdate_hour", "02"))
                self.autoupdate_minute_entry.delete(0, ctk.END)
                self.autoupdate_minute_entry.insert(0, settings.get("autoupdate_minute", "00"))

                saved_lang = settings.get("lang", "de")
                self.current_lang.set(saved_lang)
                if saved_lang == "en":
                    self.language_switch.select()
                else:
                    self.language_switch.deselect()

                saved_mode = settings.get("appearance_mode", "Dark")
                if saved_mode == "Dark":
                    self.appearance_switch.select()
                else:
                    self.appearance_switch.deselect()

        except (FileNotFoundError, json.JSONDecodeError):
            self.language_switch.deselect()
            self.appearance_switch.select()

    def save_settings(self):
        settings = {
            "ip": self.ip_entry.get(),
            "user": self.user_entry.get(),
            "lang": self.current_lang.get(),
            "appearance_mode": ctk.get_appearance_mode(), 
            "autoupdate_hour": self.autoupdate_hour_entry.get(),
            "autoupdate_minute": self.autoupdate_minute_entry.get()
        }
        with open(self.config_file, 'w') as f:
            json.dump(settings, f, indent=4)

    def toggle_connection(self):
        if self.ssh_manager.ssh_client:
            self.disconnect()
        else:
            threading.Thread(target=self.connect, daemon=True).start()
    
    def connect(self):
        t = translations[self.current_lang.get()]
        self.conn_status_label.configure(text=t["connecting"], text_color="orange")
        self.update_ui_state(connected=False)
        self.connect_btn.configure(state='disabled')

        ip = self.ip_entry.get()
        user = self.user_entry.get()
        pw = self.pw_entry.get()

        if not all([ip, user, pw]):
            messagebox.showwarning("Input Missing", "Please enter IP, username, and password.")
            self.conn_status_label.configure(text=t["not_connected"], text_color="gray")
            self.connect_btn.configure(state='normal')
            return

        result = self.ssh_manager.connect(ip, user, pw)

        if result == "success":
            self.conn_status_label.configure(text=t["connected_to"].format(ip), text_color="green")
            self.connect_btn.configure(text=t["disconnect"])
            self.save_settings()
            self.update_ui_state(connected=True)
            self.fetch_node_info()
            self.start_status_updates()
            threading.Thread(target=self.fetch_and_display_credentials, daemon=True).start()
        elif result == "auth_failed":
            self.conn_status_label.configure(text=t["auth_failed"], text_color="red")
        else:
            self.conn_status_label.configure(text=t["connection_error"].format(result), text_color="red")
        
        self.connect_btn.configure(state='normal')

    def disconnect(self):
        t = translations[self.current_lang.get()]
        self.stop_status_thread.set()
        self.ssh_manager.disconnect()
        self.conn_status_label.configure(text=t["not_connected"], text_color="gray")
        self.connect_btn.configure(text=t["connect"])
        self.update_ui_state(connected=False)
        self.version_label.configure(text=t["unknown"])
        self.status_label.configure(text="---", text_color="gray")
        theme_colors = ctk.ThemeManager.theme
        self.status_frame.configure(fg_color=theme_colors["CTkFrame"]["fg_color"])
        self.cpu_val_label.configure(text="---")
        self.ram_val_label.configure(text="---")
        self.disk_val_label.configure(text="---")
        self.uptime_val_label.configure(text="---")
        self.credentials_frame.grid_remove()
        self.seed_value_label.configure(text="---")
        self.postgres_value_label.configure(text="---")

    def fetch_and_display_credentials(self):
        config_paths = [
            'pi-node/docker_volumes/mainnet/stellar/core/etc/stellar-core.cfg',
            'pi-node-docker-production/docker_volumes/mainnet/stellar/core/etc/stellar-core.cfg'
        ]
        
        stdout = None
        
        for path in config_paths:
            command = f'cat ~/{path}'
            stdout_test, stderr_test = self.ssh_manager.execute_command(command)
            if stdout_test and "No such file" not in stderr_test:
                stdout = stdout_test
                break
            
        seed = "Not Found"
        password = "Not Found"

        if stdout:
            lines = stdout.splitlines()
            for line in lines:
                if "NODE_SEED" in line:
                    try:
                        seed = line.split('"')[1]
                    except IndexError:
                        pass
                if "DATABASE" in line:
                    try:
                        db_url = line.split('"')[1]
                        
                        password_match = re.search(r'password=([^&\s]+)', db_url)
                        if password_match:
                            password = password_match.group(1)
                        else:
                            user_pass_match = re.search(r'postgres://.*?:(.*?)\@', db_url)
                            if user_pass_match:
                                password = user_pass_match.group(1)
                                
                    except (IndexError, AttributeError):
                        pass
        
        def update_gui():
            self.seed_value_label.configure(text=seed)
            self.postgres_value_label.configure(text=password)
            if seed != "Not Found" or password != "Not Found":
                self.credentials_frame.grid()
            else:
                self.credentials_frame.grid_remove()

        self.after(0, update_gui)

    def fetch_node_info(self):
        t = translations[self.current_lang.get()]
        stdout, stderr = self.ssh_manager.execute_command("pi-node --version")
        if stdout and not stderr:
            self.version_label.configure(text=stdout)
        else:
            self.version_label.configure(text=t["unknown"])
        self.update_status()
        self.update_autoupdate_status()
        self.update_system_stats()

    def start_status_updates(self):
        self.stop_status_thread.clear()
        self.status_thread = threading.Thread(target=self.status_update_loop, daemon=True)
        self.status_thread.start()

    def status_update_loop(self):
        while not self.stop_status_thread.is_set():
            self.update_status()
            self.update_autoupdate_status()
            self.update_system_stats()
            time.sleep(10)

    def update_status(self):
        if not self.ssh_manager.ssh_client:
            return
        t = translations[self.current_lang.get()]
        stdout, stderr = self.ssh_manager.execute_command("pi-node status")
        
        status_text = "---"
        color = "gray"
        
        theme_colors = ctk.ThemeManager.theme
        default_frame_color = theme_colors["CTkFrame"]["fg_color"]
        frame_color = default_frame_color

        install_button_state = 'normal'
        upgrade_button_state = 'disabled'

        if stderr and "command not found" in stderr.lower():
            status_text = t["pi_node_not_installed"]
            color = "#F44336"
            frame_color = ("#FADBD8", "#522a2a") 
            install_button_state = 'normal'
        elif stdout:
            status_text = stdout
            status_lower = status_text.lower()
            
            if "synced" in status_lower:
                color = "#4CAF50"
                frame_color = ("#D5F5E3", "#2a5238")
                install_button_state = 'disabled'
                upgrade_button_state = 'normal'
            elif "catching-up" in status_lower:
                color = "#FFA500"
                frame_color = ("#FDEBD0", "#523a2a")
                install_button_state = 'disabled'
                upgrade_button_state = 'normal'
            elif "running" in status_lower:
                color = "#4CAF50"
                frame_color = ("#D5F5E3", "#2a5238")
                install_button_state = 'disabled'
                upgrade_button_state = 'normal'
            elif "stopped" in status_lower:
                color = "#FFC107"
                frame_color = ("#FEF9E7", "#52442a")
                install_button_state = 'normal'
                upgrade_button_state = 'normal'
            else:
                color = ("black", "white")
                install_button_state = 'normal'
        else:
            status_text = stderr if stderr else "No output"
            color = "#F44336"
            frame_color = ("#FADBD8", "#522a2a")
            install_button_state = 'normal'

        self.status_label.configure(text=status_text, text_color=color)
        self.status_frame.configure(fg_color=frame_color)
        self.install_btn.configure(state=install_button_state)
        self.upgrade_btn.configure(state=upgrade_button_state)

    def update_system_stats(self):
        if not self.ssh_manager.ssh_client:
            return

        command = (
            "echo '---CPU---' && top -bn1 | grep '%Cpu(s)' | awk '{print $2+$4\"%\"}' && "
            "echo '---RAM---' && free -m | grep Mem | awk '{print $3\"MB / \"$2\"MB\"}' && "
            "echo '---DISK---' && df -h / | tail -n 1 | awk '{print $3\" / \"$2\" (\"$5\")\"}' && "
            "echo '---UPTIME---' && uptime -p"
        )
        
        stdout, stderr = self.ssh_manager.execute_command(command)

        stats = {'cpu': '---', 'ram': '---', 'disk': '---', 'uptime': '---'}

        if stdout and not stderr:
            try:
                lines = stdout.splitlines()
                for i, line in enumerate(lines):
                    if line == '---CPU---':
                        stats['cpu'] = lines[i+1].strip()
                    elif line == '---RAM---':
                        stats['ram'] = lines[i+1].strip()
                    elif line == '---DISK---':
                        stats['disk'] = lines[i+1].strip()
                    elif line == '---UPTIME---':
                        stats['uptime'] = lines[i+1].strip().replace("up ", "")
            except (IndexError, ValueError) as e:
                print(f"Error parsing system stats: {e}")

        def update_ui():
            self.cpu_val_label.configure(text=stats['cpu'])
            self.ram_val_label.configure(text=stats['ram'])
            self.disk_val_label.configure(text=stats['disk'])
            self.uptime_val_label.configure(text=stats['uptime'])

        self.after(0, update_ui)

    def update_autoupdate_status(self):
        if not self.ssh_manager.ssh_client:
            return

        t = translations[self.current_lang.get()]
        stdout, stderr = self.ssh_manager.execute_command("crontab -l 2>/dev/null | grep 'pi-node'")

        def update_ui():
            if stdout and "pi-node" in stdout:
                self.autoupdate_status_label.configure(text=t["enabled"], text_color="#4CAF50")
                self.enable_autoupdate_btn.configure(state='disabled')
                self.disable_autoupdate_btn.configure(state='normal')

                try:
                    cron_parts = stdout.split()
                    minute, hour = cron_parts[0], cron_parts[1]
                    if minute.isdigit() and hour.isdigit():
                        self.autoupdate_hour_entry.configure(state='normal')
                        self.autoupdate_minute_entry.configure(state='normal')
                        
                        self.autoupdate_minute_entry.delete(0, ctk.END)
                        self.autoupdate_minute_entry.insert(0, f"{int(minute):02d}")
                        self.autoupdate_hour_entry.delete(0, ctk.END)
                        self.autoupdate_hour_entry.insert(0, f"{int(hour):02d}")
                        
                        self.autoupdate_hour_entry.configure(state='disabled')
                        self.autoupdate_minute_entry.configure(state='disabled')
                except (IndexError, ValueError):
                    self.autoupdate_hour_entry.configure(state='disabled')
                    self.autoupdate_minute_entry.configure(state='disabled')
            else:
                self.autoupdate_status_label.configure(text=t["disabled"], text_color="#F44336")
                self.enable_autoupdate_btn.configure(state='normal')
                self.disable_autoupdate_btn.configure(state='disabled')
                self.autoupdate_hour_entry.configure(state='normal')
                self.autoupdate_minute_entry.configure(state='normal')

        self.after(0, update_ui)

    def enable_auto_update(self):
        t = translations[self.current_lang.get()]
        hour = self.autoupdate_hour_entry.get()
        minute = self.autoupdate_minute_entry.get()

        try:
            hour_val = int(hour)
            minute_val = int(minute)
            if not (0 <= hour_val <= 23 and 0 <= minute_val <= 59):
                raise ValueError()
        except ValueError:
            messagebox.showerror(t["invalid_time"], t["invalid_time_msg"])
            return

        schedule_cron = f'"{minute_val} {hour_val} * * *"'
        command = f"pi-node enableAutoUpdate --schedule {schedule_cron}"
        confirm_msg = t["enable_autoupdate_confirm_schedule"].format(f"{hour_val:02d}", f"{minute_val:02d}")

        if messagebox.askyesno(t["enable_autoupdate"], confirm_msg):
            self.add_log_message(f"--- Enabling Auto-Update with schedule {schedule_cron}... ---")
            threading.Thread(target=self._run_auto_update_command, args=(command,), daemon=True).start()

    def disable_auto_update(self):
        t = translations[self.current_lang.get()]
        if messagebox.askyesno(t["disable_autoupdate"], t["disable_autoupdate_confirm"]):
            self.add_log_message("--- Disabling Auto-Update... ---")
            threading.Thread(target=self._run_auto_update_command, args=("pi-node disableAutoUpdate",), daemon=True).start()

    def _run_auto_update_command(self, command):
        self.ssh_manager.execute_command_stream(command, self.add_log_message)
        self.after(100, self.update_autoupdate_status)
        self.after(100, lambda: self.add_log_message("--- Action complete ---"))
        self.after(100, lambda: threading.Thread(target=self.fetch_and_display_credentials, daemon=True).start())
        self.after(100, lambda: self.add_log_message("--- Action complete ---"))

    def _paste_to_entry(self, entry_widget):
        try:
            entry_widget.delete(0, ctk.END)
            entry_widget.insert(0, self.clipboard_get())
        except Exception as e:
            print(f"Could not paste from clipboard: {e}")

    def _show_context_menu(self, event, entry_widget):
        context_menu = Menu(self, tearoff=0)
        t = translations[self.current_lang.get()]
        context_menu.add_command(label=t.get("paste", "Paste"), command=lambda: self._paste_to_entry(entry_widget))
        context_menu.tk_popup(event.x_root, event.y_root)

    def _clear_log_and_disable_buttons(self):
        self.log_text.config(state='normal')
        self.log_text.delete('1.0', ctk.END)
        self.log_text.config(state='disabled')
        self.install_btn.configure(state='disabled')
        self.upgrade_btn.configure(state='disabled')

    def install_node(self):
        t = translations[self.current_lang.get()]
        if messagebox.askyesno(t["install_confirm_title"], t["install_confirm_msg"]):
            self._clear_log_and_disable_buttons()
            self.add_log_message(f"--- {t['installation_started']} ---")
            threading.Thread(target=self._run_installation, daemon=True).start()

    def upgrade_node(self):
        t = translations[self.current_lang.get()]
        if messagebox.askyesno(t["upgrade_confirm_title"], t["upgrade_confirm_msg"]):
            self._clear_log_and_disable_buttons()
            self.add_log_message(f"--- {t['upgrade_started']} ---")
            threading.Thread(target=self._run_upgrade, daemon=True).start()

    def reboot_server(self):
        t = translations[self.current_lang.get()]
        if messagebox.askyesno(t["reboot_confirm_title"], t["reboot_confirm_msg"]):
            self.add_log_message("--- Rebooting server... Connection will be lost. ---")
            threading.Thread(target=self.ssh_manager.execute_command, args=("sudo reboot",)).start()
            self.after(2000, self.disconnect)
            
    def _run_simple_command(self, command, log_message):
        self._clear_log_and_disable_buttons()
        self.add_log_message(log_message)
        
        def command_thread():
            self.ssh_manager.execute_command_stream(command, self.add_log_message)
            self.after(100, self.finish_action)
            
        threading.Thread(target=command_thread, daemon=True).start()

    def _get_prereq_script(self):
        t = translations[self.current_lang.get()]
        return f"""
        echo "--- {t['docker_check']} ---"
        if ! command -v docker &> /dev/null; then
            echo "Docker not found. Installing via official script..."
            curl -fsSL https://get.docker.com -o get-docker.sh
            sudo sh get-docker.sh
            sudo usermod -aG docker $USER
            echo "Docker installed successfully."
        else
            echo "Docker is already installed."
        fi
        echo "Ensuring Docker Compose v2, cron, and rsync are available..."
        sudo apt-get update
        sudo apt-get install -y docker-compose-plugin cron rsync
        docker compose version
        """

    def _run_installation(self):
        t = translations[self.current_lang.get()]
        prereq_script = self._get_prereq_script()
        install_script = f"""
        set -e
        echo "--- Checking operating system ---"
        if [ ! -f /etc/debian_version ]; then
            echo "{t['os_unsupported']}"
            exit 1
        fi
        echo "Debian-based system detected. Proceeding..."
        {prereq_script}
        echo "--- Step 1: Installing Pi-Node prerequisites ---"
        sudo apt-get install -y ca-certificates curl gnupg
        echo "--- Step 2: Adding GPG key ---"
        sudo install -m 0755 -d /etc/apt/keyrings
        curl -fsSL https://apt.minepi.com/repository.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/pinetwork-archive-keyring.gpg
        sudo chmod a+r /etc/apt/keyrings/pinetwork-archive-keyring.gpg
        echo "--- Step 3: Adding APT source ---"
        echo 'deb [arch=amd64 signed-by=/etc/apt/keyrings/pinetwork-archive-keyring.gpg] https://apt.minepi.com stable main' | sudo tee /etc/apt/sources.list.d/pinetwork.list > /dev/null
        echo "--- Step 4: Updating package index ---"
        sudo apt-get update
        echo "--- Step 5: Installing pi-node package ---"
        sudo apt-get install -y pi-node
        echo "--- Step 6: Verifying installation ---"
        pi-node --version
        echo "--- Step 7: Initializing pi-node ---"
        pi-node initialize --auto-confirm --start-node
        echo "--- Installation and initialization complete! ---"
        """
        self.ssh_manager.execute_command_stream(install_script, self.add_log_message)
        self.after(100, self.finish_action)

    def _run_upgrade(self):
        t = translations[self.current_lang.get()]
        prereq_script = self._get_prereq_script()
        upgrade_script = f"""
        set -e
        echo "--- Starting Upgrade Process ---"
        
        echo "--- Ensuring pi-node CLI and prerequisites are installed ---"
        {prereq_script}
        echo "--- Updating APT and installing latest pi-node package ---"
        sudo apt-get update
        sudo apt-get install -y pi-node

        echo "--- Searching for existing Pi Node installation directory ---"
        PROJECT_DIR=""
        if [ -d "$HOME/pi-node" ] && [ -f "$HOME/pi-node/docker-compose.yml" ]; then
            PROJECT_DIR="$HOME/pi-node"
        elif [ -d "$HOME/pi-node-docker-production" ]; then
            PROJECT_DIR="$HOME/pi-node-docker-production"
        else
            echo "ERROR: Could not find an existing pi-node or pi-node-docker-production directory."
            exit 1
        fi
        echo "Found existing project directory at: $PROJECT_DIR"
        
        echo "--- Step 1: Finding stellar-core.cfg to determine configuration ---"
        cd "$PROJECT_DIR"
        > ./mainnet.env

        CONFIG_FILE_PATH=$(sudo find "$PROJECT_DIR" -name stellar-core.cfg | head -n 1)

        if [ -z "$CONFIG_FILE_PATH" ]; then
            echo "ERROR: Could not find 'stellar-core.cfg' within '$PROJECT_DIR'."
            echo "Please ensure your node's data volumes are present."
            exit 1
        fi
        echo "Found config file at: $CONFIG_FILE_PATH"
        
        DOCKER_VOLUMES_PATH_ABS=$(dirname "$(dirname "$(dirname "$CONFIG_FILE_PATH")")")
        echo "Derived main Docker volume path: $DOCKER_VOLUMES_PATH_ABS"
        
        echo "Reading configuration from $CONFIG_FILE_PATH..."
        
        NODE_SEED=$(grep 'NODE_SEED' "$CONFIG_FILE_PATH" | awk -F'"' '{{print $2}}')
        
        DB_URL=$(grep 'DATABASE' "$CONFIG_FILE_PATH" | awk -F'"' '{{print $2}}')

        POSTGRES_PASSWORD=$(echo "$DB_URL" | grep -o "password=[^&' ]*" | cut -d= -f2 | tr -d "'")

        if [ -z "$POSTGRES_PASSWORD" ]; then
            echo "Could not find 'password=' parameter. Trying user:password@host format..."
            POSTGRES_PASSWORD=$(echo "$DB_URL" | awk -F'[:@]' '{{print $3}}')
        fi

        if [ -n "$NODE_SEED" ]; then
            echo "NODE_SEED=$NODE_SEED" >> ./mainnet.env
        fi

        if [ -n "$POSTGRES_PASSWORD" ]; then
            echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD" >> ./mainnet.env
        fi
        
        if [ -f ./mainnet.env ]; then
            set -a
            source ./mainnet.env
            set +a
        fi

        if [ -z "$NODE_SEED" ] || [ -z "$POSTGRES_PASSWORD" ]; then
            echo "ERROR: Failed to automatically find all required values from config file."
            [ -z "$NODE_SEED" ] && echo " > NODE_SEED could not be found in $CONFIG_FILE_PATH."
            [ -z "$POSTGRES_PASSWORD" ] && echo " > POSTGRES_PASSWORD could not be found in $CONFIG_FILE_PATH."
            exit 1
        fi

        echo "Successfully found all configuration values."
        
        echo "--- Step 2: Stopping existing node and backing up volumes ---"
        if [ -f "docker-compose.yml" ]; then
            docker compose down
        else
            echo "Warning: docker-compose.yml not found, cannot stop node. Assuming it's already stopped."
        fi
        
        if [ -d "$DOCKER_VOLUMES_PATH_ABS" ]; then
            BACKUP_PATH="${{DOCKER_VOLUMES_PATH_ABS}}.backup"
            echo "Creating backup at: $BACKUP_PATH"
            echo "{t['backup_progress_info']}"
            sudo rsync -a --progress "$DOCKER_VOLUMES_PATH_ABS/" "$BACKUP_PATH/"
        else
            echo "Warning: Docker volumes path not found at $DOCKER_VOLUMES_PATH_ABS. Skipping backup."
        fi

        echo "--- Step 3: Initializing node with the CLI (re-using existing config) ---"
        pi-node initialize --pi-folder "$HOME/pi-node" --docker-volumes "$DOCKER_VOLUMES_PATH_ABS" --node-private-key "$NODE_SEED" --postgres-password "$POSTGRES_PASSWORD" --start-node --force --setup-auto-updates --skip-files-preview --auto-confirm

        echo "--- Step 4: Verifying status ---"
        pi-node status
        echo "--- Upgrade process complete! ---"
        """
        self.ssh_manager.execute_command_stream(upgrade_script, self.add_log_message)
        self.after(100, self.finish_action)

    def finish_action(self):
        t = translations[self.current_lang.get()]
        self.add_log_message(f"--- {t['installation_complete']} ---")
        self.fetch_node_info()
        threading.Thread(target=self.fetch_and_display_credentials, daemon=True).start()

    def add_log_message(self, message):
        def append():
            self.log_text.config(state='normal')
            self.log_text.insert(ctk.END, message + '\n')
            self.log_text.see(ctk.END)
            self.log_text.config(state='disabled')
        self.after(0, append)

    def on_closing(self):
        self.save_settings()
        self.stop_status_thread.set()
        if self.ssh_manager.ssh_client:
            self.ssh_manager.disconnect()
        self.destroy()

if __name__ == "__main__":
    app = PiNodeGUI()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()