from inventory.inventory_ui import Ui_inventory
import inventory.inventory_actions as actions
import inventory.inventory_context_menu as context
from PySide6.QtCore import QDir, Qt
from PySide6.QtWidgets import QMainWindow, QFileSystemModel, QAbstractItemView

class InventoryWindow(QMainWindow):
    def __init__(self, user):
        super(InventoryWindow, self).__init__()
        self.ui = Ui_inventory()
        self.ui.setupUi(self)

        # Crear atajos de teclado
        context.create_shortcuts(self)

        self.overwrite_all = False  # Variable de control para sobreescribir todos

        # Guarda el nombre de usuario
        self.user = user
        self.password = "macarra671"
        self.host = "150.214.198.59"

        # Configura el modelo de sistema de archivos
        self.fileSystemModel = QFileSystemModel()
        self.fileSystemModel.setRootPath(QDir.rootPath())  # Establece la raíz del sistema de archivos

        # Establece el directorio que deseas mostrar (modifica la ruta si es necesario)
        directory = "C:/Users/Ferna/Desktop/test"

        # Asocia el modelo al QTreeView en el UI
        self.ui.explorer.setModel(self.fileSystemModel)
        self.ui.explorer.setRootIndex(self.fileSystemModel.index(directory))

        # Habilitar la ordenación en el QTreeView
        self.ui.explorer.setSortingEnabled(True)

        # Ajustar el ancho de la primera columna (nombre)
        self.ui.explorer.setColumnWidth(0, 450)  # Cambia 450 por el valor deseado para el ancho

        # Habilitar barras de desplazamiento
        self.ui.explorer.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # Barra horizontal solo cuando sea necesario
        self.ui.explorer.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)  # Barra vertical solo cuando sea necesario

        # Configuración de la ventana
        self.setWindowTitle('Inventory - Neutrocloud App')
        self.setFixedSize(self.size())  # Evita que se redimensione

        # Habilitar la selección múltiple en el QTreeView
        self.ui.explorer.setSelectionMode(QAbstractItemView.ExtendedSelection)

        # Conecta el evento mousePressEvent al método go_home
        self.ui.label_home.mousePressEvent = self.handle_home_click

        # Crear el menú contextual para copiar y pegar
        context.create_context_menu(self)
        

        
    def handle_home_click(self, event):
        # Llama al método go_home cuando se haga clic
        self.go_home()

    # Método para volver al menú
    def go_home(self):
        from menu import MenuWindow  # Importación diferida
        self.close()
        self.menu_window = MenuWindow(self.user)  # Crea el menú con el usuario
        self.menu_window.show()
        
    # Usar las funciones importadas de inventory_actions
    def copy_to_clipboard(self):
        actions.copy_to_clipboard(self)  # Llama a la función de inventory_actions

    def paste_from_clipboard(self):
        actions.paste_from_clipboard(self)  # Llama a la función de inventory_actions

    def delete_item(self):
        actions.delete_item(self)  # Llama a la función de inventory_actions

    def cut_to_clipboard(self):
        actions.cut_to_clipboard(self)  # Llama a la función de inventory_actions  
    
    def rename_item(self):
        actions.rename_item(self)  # Llama a la función de inventory_actions  
        
    def duplicate_item(self):
        actions.duplicate_item(self)  # Llama a la función de inventory_actions  
        
    def show_context_menu(self, pos):
        context.show_context_menu(self, pos)
