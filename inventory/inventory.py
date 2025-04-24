import paramiko
from PySide6.QtWidgets import QMainWindow, QTreeView
from PySide6.QtGui import QStandardItem, QStandardItemModel
import inventory.inventory_actions as actions
import inventory.inventory_context_menu as context
from inventory.inventory_ui import Ui_inventory
import utils.utils as utils
import os
import time

class InventoryWindow(QMainWindow):
    def __init__(self, user, password):
        super(InventoryWindow, self).__init__()
        self.ui = Ui_inventory()
        self.ui.setupUi(self)
        
        # Crear atajos de teclado
        context.create_shortcuts(self)

        # Guarda el nombre de usuario
        self.user = user
        self.password = password
        self.host = "150.214.198.59"
        # Ruta inicial
        self.current_directory = f"/home/{self.user}"

        # Configura el modelo para el explorador de archivos
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Name", "Size KiB", "Since Modified", "Type"])
        
        # Cargar los archivos remotos en el modelo
        self.load_remote_files()
        
        # Configurar QTreeView
        self.ui.explorer.setModel(self.model)
        self.ui.explorer.setSortingEnabled(True)
        self.ui.explorer.setSelectionMode(QTreeView.ExtendedSelection)
        
        # Configuración de la ventana
        self.setWindowTitle('Inventory - Neutrocloud App')
        self.setFixedSize(self.size())

        # Ajustar el ancho de las columnas proporcionalmente
        self.adjust_column_widths()

        # Conecta el evento mousePressEvent al método go_home
        self.ui.label_home.mousePressEvent = lambda event: utils.handle_home_click(self, event)
        # Conecta el evento mousePressEvent al método go_back
        self.ui.label_back.mousePressEvent = self.handle_back_click
        # Conecta el evento mousePressEvent al método refresh
        self.ui.label_refresh.mousePressEvent = self.handle_refresh_click
        # Conectar el evento doble clic a la función de cambio de directorio
        self.ui.explorer.doubleClicked.connect(self.on_directory_double_clicked)
        # Conectar el evento de selección en el explorador
        self.ui.explorer.clicked.connect(self.on_item_clicked)

        # Crear el menú contextual para copiar y pegar
        context.create_context_menu(self)
        
    def update_label_data(self, message):
        """
        Actualiza el texto de label_data con el mensaje proporcionado.
        """
        self.ui.label_data.setText(message)  # Muestra el mensaje en la etiqueta
        self.ui.label_data.setToolTip(message)  # Añade un tooltip por si el texto es largo
        
    def on_item_clicked(self, index):
        """
        Muestra la ruta completa del archivo o directorio seleccionado en label_data sin 'file:///' y con la extensión correcta.
        """
        if not index.isValid():
            return

        # Obtener el nombre y tipo del archivo o carpeta seleccionado
        item_name = self.model.itemFromIndex(index).text()
        item_type = self.model.itemFromIndex(index.siblingAtColumn(3)).text()  # Obtener tipo del ítem

        # Si no es un directorio, agregar la extensión
        if item_type != "Directory":
            file_extension = "." + item_type if item_type else ""
        else:
            file_extension = ""

        # Construir la ruta absoluta con la extensión si aplica
        file_path = f"{self.current_directory}/{item_name}{file_extension}"

        # Mostrar la ruta en label_data sin "file:///"
        self.update_label_data(file_path)
    

    def load_remote_files(self):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.host, username=self.user, password=self.password)
            sftp = ssh.open_sftp()
            
            # Usar la ruta actual para cargar los archivos del directorio
            file_list = sftp.listdir_attr(self.current_directory)
            
            # Limpiar el modelo antes de cargar los nuevos archivos
            self.model.clear()  
            self.model.setHorizontalHeaderLabels(["Name", "Size KiB", "Since Modified", "Type"])
            
            for file in file_list:
                if file.filename.startswith("."):
                    continue  # Ignorar archivos ocultos
                
                # Convertir tamaño a KiB con 2 decimales
                size_kib = f"{round(file.st_size / 1024, 2)} KiB"
                
                # Obtener la fecha de última modificación
                modified_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(file.st_mtime))
                
                # Determinar tipo de archivo basado en la extensión
                if file.st_mode & 0o40000:
                    file_type = "Directory"
                else:
                    file_type = os.path.splitext(file.filename)[1][1:] or "Unknown"
                
                item_name = QStandardItem(os.path.splitext(file.filename)[0] if file_type != "Directory" else file.filename)
                item_size = QStandardItem(size_kib)
                item_modified = QStandardItem(modified_time)
                item_type = QStandardItem(file_type)
                self.model.appendRow([item_name, item_size, item_modified, item_type])
                
                # Ajustar el ancho de las columnas proporcionalmente
                self.adjust_column_widths()
            sftp.close()
            ssh.close()
        except Exception as e:
            self.update_label_data("Error al conectar con el servidor: {e}")

    def on_directory_double_clicked(self, index):
        item = self.model.itemFromIndex(index)
        
        if item is not None and item.text() != "":
            # Obtener tipo del ítem
            item_type = self.model.itemFromIndex(index.siblingAtColumn(3)).text()  # Obtener tipo del ítem
            if item_type == "Directory":
                # Construir la nueva ruta correctamente con '/home/{self.user}'
                new_directory = os.path.join(self.current_directory, item.text())
                new_directory = new_directory.replace("\\", "/")  # Reemplazar las barras invertidas con barras normales

                # Verificar si el directorio existe en el servidor remoto
                try:
                    ssh = paramiko.SSHClient()
                    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    ssh.connect(self.host, username=self.user, password=self.password)
                    sftp = ssh.open_sftp()

                    # Verificar si el directorio existe
                    sftp.stat(new_directory)  # Intentar obtener información del directorio
                    
                    # Limpiar el modelo actual antes de cargar el nuevo directorio
                    self.model.clear()  # Limpiar la vista actual

                    # Actualizar la ruta y cargar los archivos del nuevo directorio
                    self.current_directory = new_directory
                    self.load_remote_files()  # Recargar los archivos del nuevo directorio

                    # Actualizar el título de la ventana para reflejar el nuevo directorio
                    self.setWindowTitle(f'Inventory - Neutrocloud App - {self.current_directory}')

                    sftp.close()
                    ssh.close()
                except FileNotFoundError:
                    self.update_label_data("Error: El directorio '{new_directory}' no existe.")
                except Exception as e:
                    self.update_label_data("Error al acceder al directorio: {e}")
            else:
                self.rename_item()

    def adjust_column_widths(self):
        # Ajustar el ancho de las columnas proporcionalmente
        self.ui.explorer.setColumnWidth(0, int(self.ui.explorer.width() * 0.45))  # Name 45%
        self.ui.explorer.setColumnWidth(1, int(self.ui.explorer.width() * 0.20))  # Size 20%
        self.ui.explorer.setColumnWidth(2, int(self.ui.explorer.width() * 0.25))  # Since Modified 25%
        self.ui.explorer.setColumnWidth(3, int(self.ui.explorer.width() * 0.10))  # Type 10%

    def handle_refresh_click(self, event):
        self.load_remote_files()  # Recargar los archivos del directorio actual
        
    def handle_back_click(self, event):
        """
        Maneja el evento de clic en el botón "Back".
        Vuelve al directorio anterior, si existe y no está en la raíz del usuario.
        """
        # Definir la ruta raíz del usuario
        home_directory = f"/home/{self.user}"

        if self.current_directory != home_directory:
            # Obtener el directorio padre
            parent_directory = os.path.dirname(self.current_directory)

            try:
                # Verificar si el directorio padre es accesible
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(self.host, username=self.user, password=self.password)
                sftp = ssh.open_sftp()

                # Verificar si el directorio padre existe
                sftp.stat(parent_directory)  # Lanza una excepción si no existe

                # Actualizar la ruta actual y cargar los archivos del directorio anterior
                self.current_directory = parent_directory
                self.load_remote_files()

                # Actualizar el título de la ventana
                self.setWindowTitle(f'Inventory - Neutrocloud App - {self.current_directory}')

                sftp.close()
                ssh.close()
            except FileNotFoundError:
                self.update_label_data("Error: El directorio '{parent_directory}' no existe.")
            except Exception as e:
                self.update_label_data("Error al acceder al directorio anterior: {e}")
        else:
            self.update_label_data("Ya estás en el directorio raíz.")

        
    # Usar las funciones importadas de inventory_actions
    def copy_to_clipboard(self):
        actions.copy_to_clipboard(self)  # Llama a la función de inventory_actions

    def paste_from_clipboard(self):
        actions.paste_from_clipboard(self)  # Llama a la función de inventory_actions

    def delete_item(self):
        actions.delete_item(self)  # Llama a la función de inventory_actions
    
    def rename_item(self):
        actions.rename_item(self)  # Llama a la función de inventory_actions  
    
    def duplicate_item(self):
        actions.duplicate_item(self)  # Llama a la función de inventory_actions  
    def create_dir(self):
        actions.create_dir(self)
    
    def show_context_menu(self, pos):
        context.show_context_menu(self, pos)