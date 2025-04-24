import paramiko
import os
import json
from calendarr.evento import Evento

class ConfigManager:
    CONFIG_FILE = "calendar_config.json"  # Esto se manejará de forma remota

    def __init__(self, user, password, host="150.214.198.59"):
        self.user = user
        self.password = password
        self.host = host
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def connect_to_server(self):
        """Conectar al servidor remoto usando SSH"""
        try:
            self.ssh_client.connect(self.host, username=self.user, password=self.password)
        except Exception as e:
            print(f"Error al conectar al servidor: {e}")

    def load_or_create_config(self):
        self.connect_to_server()

        # Ruta remota del archivo
        remote_config_file = f"/home/{self.user}/.config/neutricloud/{self.CONFIG_FILE}"

        try:
            sftp = self.ssh_client.open_sftp()

            # Comprobar si el directorio .config existe en el servidor remoto, si no, crearlo
            config_dir = os.path.dirname(remote_config_file)
            parent_dir = os.path.dirname(config_dir)  # Es la ruta a .config

            # Verificar si .config existe, si no, crearla
            try:
                sftp.stat(parent_dir)  # Intentar acceder a .config
            except FileNotFoundError:
                print(f"Directorio {parent_dir} no encontrado. Creando directorio...")
                sftp.mkdir(parent_dir)

            # Comprobar si el directorio neutricloud existe, si no, crearlo
            try:
                sftp.stat(config_dir)  # Intentar acceder al directorio neutricloud
            except FileNotFoundError:
                print(f"Directorio {config_dir} no encontrado. Creando directorio...")
                sftp.mkdir(config_dir)

            # Comprobar si el archivo de configuración existe
            try:
                sftp.stat(remote_config_file)  # Intentar acceder al archivo remoto
                with sftp.open(remote_config_file, "r") as f:
                    data = json.load(f)
                    self.config = data

                    # Convertir los diccionarios de vuelta a objetos Evento
                    for date, events in self.config["events"].items():
                        self.config["events"][date] = [Evento.from_dict(event) for event in events]

            except FileNotFoundError:
                # Si no existe el archivo, crear uno por defecto con un diccionario vacío de eventos
                print("Archivo de configuración no encontrado. Creando uno nuevo.")
                self.config = {"events": {}}

                # Guardar el archivo de configuración con un formato predeterminado
                with sftp.open(remote_config_file, "w") as f:
                    json.dump(self.config, f, indent=4)
                print(f"Archivo de configuración creado en: {remote_config_file}")
            return self.config

        except Exception as e:
            print(f"Error al cargar el archivo de configuración desde el servidor: {e}")

    def save_config(self, config):
        # Convertir todos los eventos a diccionarios
        events_dict = {}
        for date, events in config["events"].items():
            events_dict[date] = [event.to_dict() for event in events]

        # Guardar la configuración en el archivo JSON remoto
        try:
            sftp = self.ssh_client.open_sftp()
            remote_config_file = f"/home/{self.user}/.config/neutricloud/{self.CONFIG_FILE}"
            with sftp.open(remote_config_file, "w") as f:
                json.dump({"events": events_dict}, f, indent=4)
        except Exception as e:
            print(f"Error al guardar el archivo de configuración en el servidor: {e}")
