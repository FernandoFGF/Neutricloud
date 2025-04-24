# inventory_functions.py
import paramiko
from PySide6.QtWidgets import QApplication, QMessageBox, QInputDialog
import os

def copy_to_clipboard(self):
    """
    Copia solo los nombres de los archivos y carpetas seleccionados al portapapeles.
    """
    indexes = self.ui.explorer.selectedIndexes()

    if not indexes:
        self.update_label_data("No se ha seleccionado ningún archivo o directorio.")
        return

    file_names = set()  # Usamos un set para evitar duplicados

    for index in indexes:
        if not index.isValid():
            continue

        # Solo procesamos la primera columna de la fila (columna 0)
        if index.column() == 0:  # Columna 0 es donde está el nombre del archivo o directorio
            # Obtener solo el nombre del archivo/carpeta (columna 0)
            item_name = self.model.itemFromIndex(index).text()

            # Obtener el tipo del ítem (si es necesario, para agregar extensión)
            item_type = self.model.itemFromIndex(index.siblingAtColumn(3)).text()  # Obtener tipo del ítem

            # Si no es un directorio, agregar la extensión si es necesario
            file_extension = f".{item_type}" if item_type and item_type != "Directory" else ""

            # Construir la ruta completa
            file_path = f"{self.current_directory}/{item_name}{file_extension}"

            # Añadir la ruta al set (evita duplicados)
            file_names.add(file_path)

    if file_names:
        clipboard = QApplication.clipboard()

        clipboard.setText("\n".join(file_names))

        # Mostrar lo copiado en label_data
        self.update_label_data(f"Copiado al portapapeles:{file_names}")
    else:
        self.update_label_data("No se encontraron archivos válidos para copiar.")

def paste_from_clipboard(self):
    """
    Copia archivos desde el portapapeles a la ubicación seleccionada en el servidor remoto.
    Si el archivo ya existe, no permite la sobrescritura y muestra un mensaje.
    """
    clipboard = QApplication.clipboard()
    mime_data = clipboard.mimeData()
    copied_paths = mime_data.text().split("\n")  # Separamos por salto de línea

    if not copied_paths:
        self.update_label_data("No hay archivos copiados en el portapapeles.")
        return

    index = self.ui.explorer.selectedIndexes()
    
    if not index:
        remote_target_directory = self.current_directory
    elif index[3].data() != "Directory":
        remote_target_directory = self.current_directory
    else:
        target_directory = index[0].data()  # Obtener la ruta del directorio seleccionado
        remote_target_directory = f"/home/{self.user}/{target_directory}"

    # Iniciar conexión SSH con paramiko
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, username=self.user, password=self.password)

        for file_path in copied_paths:
            if not file_path:
                continue

            # Obtener el nombre del archivo
            file_name = file_path.split('/')[-1]
            remote_file_path = f"{remote_target_directory}/{file_name}"

            dir = item_type(file_name, self)

            # Verificamos si es una ruta local (Windows) o remota (servidor)
            if file_path.startswith('/home/'):
                # Ruta remota: usar cp
                copy_remote_file(self, file_path, remote_target_directory, ssh, dir)
            else:
                # Ruta local: usar scp
                transfer_local_file(self, file_path, remote_target_directory, ssh)
        
        self.load_remote_files()
        ssh.close()

    except Exception as e:
        self.update_label_data(f"Error de conexión SSH: {str(e)}")




def copy_remote_file(self, remote_file_path, remote_target_directory, ssh, item_type):
    """
    Copia un archivo desde el servidor remoto a otro directorio en el servidor.
    """
    file_name = remote_file_path.split("/")[-1]
    # Construimos manualmente la ruta de destino asegurándonos de que la barra inclinada está bien colocada.
    remote_target_path = f"{remote_target_directory}/{file_name}"

    if item_type == "Directory":
        # Si es un directorio, usamos el parámetro -r
        cp_command = f"cp -r {remote_file_path} {remote_target_path}"
    else:
        # Si es un archivo, no necesitamos el parámetro -r
        cp_command = f"cp {remote_file_path} {remote_target_path}"
    
    #cp_command = f"cp {remote_file_path} {remote_target_path}"
    
    stdin, stdout, stderr = ssh.exec_command(cp_command)
    error = stderr.read().decode()

    if error:
        self.update_label_data(f"Error al copiar: {error}")
    else:
        self.update_label_data(f"Archivo copiado a {remote_target_directory}")


def transfer_local_file(self, local_file_path, remote_target_directory, ssh):
    """
    Transfiere un archivo desde la máquina local al servidor remoto usando SCP.
    """
    try:
        # Si la ruta tiene 'file://', eliminar esa parte para obtener la ruta local correcta
        if local_file_path.startswith('file:///'):
            local_file_path = local_file_path[8:]  # Eliminar 'file:///' al inicio

        # En Windows, las rutas deben tener una barra invertida (backslash), así que la convertimos
        local_file_path = local_file_path.replace('/', '\\')
        
        # Usar SCP para transferir el archivo
        scp = paramiko.SFTPClient.from_transport(ssh.get_transport())
        # Crear la ruta remota con barras inclinadas, usando os.path.join pero reemplazando las barras invertidas en Windows
        remote_file_path = remote_target_directory + '/' + os.path.basename(local_file_path)
        scp.put(local_file_path, remote_file_path)
        self.load_remote_files()
        scp.close()

        self.update_label_data(f"Archivo local copiado a {remote_target_directory}")
    
    except Exception as e:
        "Error al transferir el archivo"

def delete_item(self):
    """
    Elimina los archivos o directorios seleccionados de forma remota en el servidor.
    """
    # Obtener los índices seleccionados en la primera columna
    indexes = [index for index in self.ui.explorer.selectedIndexes() if index.column() == 0]

    if not indexes:
        return

    # Mostrar un cuadro de confirmación antes de eliminar
    reply = QMessageBox.question(
        self, 'Confirmar eliminación', '¿Estás seguro de que deseas eliminar los archivos seleccionados?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

    if reply == QMessageBox.Yes:
        # Iniciar conexión SSH con paramiko
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.user, password=self.password)

            for index in indexes:
                if not index.isValid():
                    continue

                # Solo procesamos la primera columna de la fila (columna 0)
                if index.column() == 0:  # Columna 0 es donde está el nombre del archivo o directorio
                    # Obtener solo el nombre del archivo/carpeta (columna 0)
                    item_name = self.model.itemFromIndex(index).text()

                    # Obtener el tipo del ítem (si es necesario, para agregar extensión)
                    item_type = self.model.itemFromIndex(index.siblingAtColumn(3)).text()  # Obtener tipo del ítem

                    # Si no es un directorio, agregar la extensión si es necesario
                    file_extension = f".{item_type}" if item_type and item_type != "Directory" else ""

                    # Construir la ruta completa
                    file_path = f"{self.current_directory}/{item_name}{file_extension}"

                    # Ejecutamos el comando de eliminación remota
                    if item_type == "Directory":
                        # Si es un directorio, usamos 'rm -r' para eliminarlo
                        rm_command = f"rm -r {file_path}"
                    else:
                        # Si es un archivo, usamos 'rm' para eliminarlo
                        rm_command = f"rm {file_path}"

                    stdin, stdout, stderr = ssh.exec_command(rm_command)
                    error = stderr.read().decode()

                    if error:
                        self.update_label_data(f"Error al eliminar {file_path}: {error}")
                    else:
                        self.update_label_data(f"{file_path} eliminado.")
            self.load_remote_files()
            ssh.close()

        except Exception as e:
            self.update_label_data(f"Error de conexión SSH: {str(e)}")
        

def rename_item(self):
    """
    Renombra el archivo o directorio seleccionado en el servidor remoto.
    """
    # Obtener solo los índices de la primera columna para evitar repeticiones
    indexes = [index for index in self.ui.explorer.selectedIndexes() if index.column() == 0]

    if not indexes:
        self.update_label_data("No se ha seleccionado ningún archivo o directorio para renombrar.")
        return

    # Obtener el nombre del archivo o directorio seleccionado
    item_name = self.model.itemFromIndex(indexes[0]).text()

    # Obtener el tipo del ítem desde la columna 4 (tipo de ítem)
    item_type = self.model.itemFromIndex(indexes[0].siblingAtColumn(3)).text()  # Obtener tipo del ítem (ej. 'Directory', 'txt', etc.)

    # Mostrar un cuadro de diálogo para que el usuario ingrese el nuevo nombre
    new_name, ok = QInputDialog.getText(self, 'Renombrar archivo o directorio', 'Ingresa el nuevo nombre:', text=item_name)

    if ok and new_name:
        # Si es un directorio, no necesitas extensión. Si es un archivo, debes conservar la extensión.
        if item_type == "Directory":
            new_item_name = new_name  # Para directorios, no agregamos extensión.
            file_extension = ""  # No agregamos extensión para directorios.
        else:
            file_extension = f".{item_type}"  # Para archivos, añadimos la extensión.
            new_item_name = f"{new_name}{file_extension}"  # Para archivos, agregamos extensión al nuevo nombre.

        # Obtener la ruta completa del archivo o directorio
        file_path = f"{self.current_directory}/{item_name}{file_extension}"  # Agregar extensión al archivo de origen
        new_file_path = f"{self.current_directory}/{new_item_name}"

        # Comprobar si ya existe un archivo o directorio con el mismo nombre en el índice (columna 0)
        for row in range(self.ui.explorer.model().rowCount()):
            index = self.ui.explorer.model().index(row, 0)
            existing_item_name = self.model.itemFromIndex(index).text()
            existing_item_type = self.model.itemFromIndex(index.siblingAtColumn(3)).text()  # Tipo de ítem (archivo o directorio)

            # Si el nombre coincide y el tipo es diferente (archivo vs directorio), mostrar advertencia
            if existing_item_name == new_item_name and existing_item_type != item_type:
                QMessageBox.warning(self, 'Error', f"Ya existe un {existing_item_type} con el mismo nombre.")
                return

        # Iniciar conexión SSH con paramiko
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.user, password=self.password)

            # Comando para renombrar usando 'mv' (cambiar nombre)
            mv_command = f"mv {file_path} {new_file_path}"
            
            # Ejecutamos el comando para renombrar el archivo o directorio
            stdin, stdout, stderr = ssh.exec_command(mv_command)
            error = stderr.read().decode()

            if error:
                self.update_label_data(f"Error al renombrar {file_path} a {new_file_path}: {error}")
            else:
                self.update_label_data(f"{file_path} renombrado a {new_file_path}")
            self.load_remote_files()
            ssh.close()

        except Exception as e:
            self.update_label_data(f"Error de conexión SSH: {str(e)}")

def duplicate_item(self):
    """
    Duplicar los archivos o directorios seleccionados en el servidor remoto.
    """
    # Obtener solo los índices de la primera columna para evitar repeticiones
    indexes = [index for index in self.ui.explorer.selectedIndexes() if index.column() == 0]

    if not indexes:
        self.update_label_data("No se ha seleccionado ningún archivo o directorio para duplicar.")
        return

    # Iniciar conexión SSH con paramiko
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.host, username=self.user, password=self.password)

        for index in indexes:
            if not index.isValid():
                continue

            # Obtener el nombre del archivo o directorio seleccionado
            item_name = self.model.itemFromIndex(index).text()

            # Obtener el tipo del ítem desde la columna 4 (tipo de ítem)
            item_type = self.model.itemFromIndex(index.siblingAtColumn(3)).text()  # Obtener tipo del ítem (ej. 'Directory', 'txt', etc.)

            # Preparar el nuevo nombre para duplicar
            if item_type == "Directory":
                new_item_name = item_name + "_copy"  # Para directorios, no agregamos extensión.
                file_extension = ""  # No agregamos extensión para directorios.
            else:
                file_extension = f".{item_type}"  # Para archivos, añadimos la extensión.
                new_item_name = f"{item_name}_copy{file_extension}"  # Para archivos, agregamos extensión al nuevo nombre.

            # Obtener la ruta completa del archivo o directorio
            file_path = f"{self.current_directory}/{item_name}{file_extension}"  # Agregar extensión al archivo de origen
            new_file_path = f"{self.current_directory}/{new_item_name}"

            # Comando para duplicar el archivo o directorio
            if item_type == "Directory":
                mv_command = f"cp -r {file_path} {new_file_path}"
            else:
                mv_command = f"cp {file_path} {new_file_path}"

            stdin, stdout, stderr = ssh.exec_command(mv_command)
            error = stderr.read().decode()

            if error:
                self.update_label_data(f"Error al duplicar {file_path}: {error}")
            else:
                self.update_label_data(f"{file_path} duplicdo.")
        self.load_remote_files()
        ssh.close()

    except Exception as e:
        self.update_label_data(f"Error de conexión SSH: {str(e)}")

def item_type(item, self):
    """
    Devuelve el tipo de archivo (o directorio) de un ítem dado.
    """
    # Obtener el número de filas del modelo
    row_count = self.model.rowCount()

    # Iterar sobre todas las filas
    for row in range(row_count):
        # Obtener el nombre del archivo o directorio desde la primera columna (ítem)
        item_name = self.model.itemFromIndex(self.model.index(row, 0)).text()

        # Obtener el tipo de ítem desde la columna 3
        item_type = self.model.itemFromIndex(self.model.index(row, 3)).text()

        # Si el tipo es 'Directory', solo comparamos el nombre (columna 0)
        if item_type == "Directory":
            if item_name == item:
                return item_type  # Retornar solo el tipo de ítem (Directory)
        else:
            # Si no es un directorio, combinamos el nombre y la extensión (columna 0 y columna 3)
            file_name_with_extension = item_name + "." + item_type
            if file_name_with_extension == item:
                return item_type  # Retornar solo el tipo de ítem (por ejemplo, extensión)

    return ""  # Si no se encuentra el ítem, retornar cadena vacía




def create_dir(self):
    """
    Muestra un cuadro de texto para que el usuario ingrese el nombre del nuevo directorio
    y luego lo crea en el servidor remoto con los permisos del usuario conectado.
    """
    # Mostrar cuadro de texto para ingresar el nombre del directorio
    dir_name, ok = QInputDialog.getText(self, "Nuevo Directorio", "Ingrese el nombre del directorio:")

    # Verificar si el usuario hizo clic en 'OK' y si el nombre del directorio no está vacío
    if ok and dir_name:
        # Componer la ruta completa del nuevo directorio
        new_dir_path = f"{self.current_directory}/{dir_name}"

        # Iniciar conexión SSH con paramiko
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.user, password=self.password)

            # Crear el directorio
            mkdir_command = f"mkdir {new_dir_path}"
            stdin, stdout, stderr = ssh.exec_command(mkdir_command)
            error = stderr.read().decode()

            if error:
                self.update_label_data(f"Error al crear el directorio: {error}")
                return
            else:
                self.update_label_data(f"Directorio '{new_dir_path}' creado.")
            self.load_remote_files()
            ssh.close()

        except Exception as e:
            self.update_label_data(f"Error de conexión SSH: {str(e)}")
    else:
        # Si el usuario canceló o dejó el campo vacío, mostrar un mensaje
        self.update_label_data("No se proporcionó un nombre válido para el directorio.")

    