import os
from PySide6.QtWidgets import QDialog, QFileDialog
from meetings.publish_ui import Ui_publish  # El archivo generado por pyuic6
import utils.utils as utils
import paramiko
import datetime


class PublishDialog(QDialog, Ui_publish):
    def __init__(self, parent=None):
        super(PublishDialog, self).__init__(parent)
        self.setupUi(self)

        # Agregar elementos al QComboBox de categorías
        self.addCategoriesToComboBox()

        # Conectar los botones a las funciones correspondientes
        self.search_path.clicked.connect(self.searchItem)
        self.cancel.clicked.connect(self.reject)  # Cerrar el diálogo sin hacer nada
        self.confirm.clicked.connect(self.confirmPublish)

    def addCategoriesToComboBox(self):
        """Agrega categorías al QComboBox."""
        categories = ["LAB", "SIMULATIONS", "ANALYSIS / RECONSTRUCTION", "SBND COMMISSIONING", "OTHERS"]  # Lista de categorías
        self.categoryComboBox.addItems(categories)  # Agregar las categorías al combo box

    def searchItem(self):
        """Abre un cuadro de diálogo para seleccionar un archivo en el sistema."""
        file_path, _ = QFileDialog.getOpenFileName(self, "Seleccionar archivo", "", "Todos los archivos (*.*)")
        if file_path:
            self.upload_path.setText(file_path)  # Establecer el pathing del archivo en el QLineEdit

    def confirmPublish(self):
        """Confirma la publicación con los datos introducidos en los campos."""
        category = self.categoryComboBox.currentText()  # Obtener la categoría seleccionada
        title = self.title.text()  # Obtener el título
        pathing = self.upload_path.text()  # Obtener el pathing del archivo

        # Validar que todos los campos estén completos
        if not category or not title or not pathing:
            utils.update_label_data(self.parent(), f"Todos los campos deben estar llenos.")
            return

        if not os.path.exists(pathing):
            utils.update_label_data(self.parent(), f"El archivo no existe.")
            return

        # Lógica de la publicación (puedes personalizarla según tus necesidades)
        self.publishItem(category, title, pathing)

        # Cerrar el diálogo después de confirmar
        self.accept()

    def publishItem(self, category, title, pathing):
        """Sube el archivo y lo asocia con el meeting más cercano."""
        remote_meetings_dir = "/var/www/wiki/data/pages/start/group_meetings"
        remote_media_dir = "/var/www/wiki/data/media/start/group_meetings"

        # Obtener el nombre del archivo subido
        remote_filename = os.path.basename(pathing)
        remote_media_path = f"{remote_media_dir}/{remote_filename}"

        parent = self.parent()
        if not all(hasattr(parent, attr) for attr in ["host", "user", "password"]):
            utils.update_label_data(parent, "❌ Error: Credenciales no disponibles.")
            return

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(parent.host, username=parent.user, password=parent.password)

            sftp = ssh.open_sftp()

            # Subir el archivo al servidor
            sftp.put(pathing, remote_media_path)
            
            # Intentar verificar si el archivo de reuniones ya existe
            '''try:
                sftp.stat(remote_media_path)  # Esto solo devuelve información del archivo si existe
                utils.update_label_data(self.parent(), "El archivo ya existe")
                sftp.close()
                ssh.close()
                return  # Salir si el archivo ya existe
            except IOError:
                # Si el archivo no existe (captura IOError), simplemente continúa
                pass'''

            # Obtener lista de archivos en el directorio de meetings
            files = sftp.listdir(remote_meetings_dir)
            txt_files = sorted(
                [f for f in files if f.endswith(".txt")],
                key=lambda f: sftp.stat(f"{remote_meetings_dir}/{f}").st_mtime,
                reverse=True  # Ordenar por fecha de modificación (más reciente primero)
            )

            if not txt_files:
                utils.update_label_data(parent, "❌ No hay meetings en el servidor.")
                return

            latest_meeting_file = txt_files[0]  # El archivo de meeting más reciente
            meeting_date_str = latest_meeting_file.replace(".txt", "")  # 2025_04_04
            meeting_date = datetime.datetime.strptime(meeting_date_str, "%Y_%m_%d").date()
            today_date = datetime.date.today()

            if meeting_date < today_date:
                utils.update_label_data(parent, "⚠️ No hay meeting pendiente.")
                return

            # Descargar el archivo de meeting para modificarlo
            local_meeting_path = f"group_meeting_temp.txt"
            remote_meeting_path = f"{remote_meetings_dir}/{latest_meeting_file}"
            sftp.get(remote_meeting_path, local_meeting_path)

            # Leer el contenido y modificarlo
            with open(local_meeting_path, "r", encoding="utf-8") as f:
                lines = f.readlines()

            insert_line = f"  * {parent.user} {{{{ :start:group_meetings:{remote_filename} | {title} }}}}\n"
            updated_lines = []
            category_found = False

            for line in lines:
                updated_lines.append(line)
                if line.strip() == f"=== {category} ===":
                    updated_lines.append(insert_line)
                    category_found = True

            if not category_found:
                utils.update_label_data(parent, f"⚠️ No se encontró la categoría {category} en el archivo de meeting.")

            # Guardar los cambios en el archivo local
            with open(local_meeting_path, "w", encoding="utf-8") as f:
                f.writelines(updated_lines)

            # Subir el archivo modificado al servidor
            sftp.put(local_meeting_path, remote_meeting_path)

            utils.update_label_data(parent, f"✅ Archivo '{remote_filename}' subido y registrado en el meeting {meeting_date_str}.")

            # Cerrar conexiones
            sftp.close()
            ssh.close()

        except Exception as e:
            utils.update_label_data(parent, f"❌ Error al procesar el archivo: {e}")
