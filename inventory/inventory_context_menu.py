from PySide6.QtGui import QAction, QShortcut, QKeySequence
from PySide6.QtWidgets import QMenu
from PySide6.QtCore import Qt

def create_context_menu(self):
    # Crear una acción para copiar
    self.copy_action = QAction('Copy', self)
    self.copy_action.triggered.connect(self.copy_to_clipboard)

    # Crear una acción para pegar
    self.paste_action = QAction('Paste', self)
    self.paste_action.triggered.connect(self.paste_from_clipboard)

    # Crear una acción para eliminar
    self.delete_action = QAction('Delete', self)
    self.delete_action.triggered.connect(self.delete_item)
    
    # Crear una acción para cambiar nombre
    self.rename_action = QAction('Rename', self)
    self.rename_action.triggered.connect(self.rename_item)
    
    # Crear una acción para duplicar
    self.duplicate_action = QAction('Duplicate', self)
    self.duplicate_action.triggered.connect(self.duplicate_item)
    
    # Crear una acción para duplicar
    self.create_dir_action = QAction('Create directory', self)
    self.create_dir_action.triggered.connect(self.create_dir)

    # Crear el menú contextual
    self.context_menu = QMenu(self)
    self.context_menu.addAction(self.copy_action)
    self.context_menu.addAction(self.paste_action)
    self.context_menu.addAction(self.delete_action)
    self.context_menu.addAction(self.rename_action)
    self.context_menu.addAction(self.duplicate_action)
    self.context_menu.addAction(self.create_dir_action)   
    
    # Establecer un estilo personalizado para el menú contextual
    self.context_menu.setStyleSheet("""
        QMenu {
            background-color: #2d2d2d;  /* Color de fondo */
            border: 2px solid black;    /* Borde negro */
            border-radius: 5px;         /* Bordes redondeados */
        }
        QMenu::item {
            padding: 10px;              /* Espaciado entre los elementos */
            color: white;               /* Color de texto */
        }
        QMenu::item:selected {
            background-color: #575757;  /* Color de fondo cuando un ítem está seleccionado */
        }
    """)

    # Conectar el evento del menú contextual al QTreeView
    self.ui.explorer.setContextMenuPolicy(Qt.CustomContextMenu)
    self.ui.explorer.customContextMenuRequested.connect(self.show_context_menu)

def show_context_menu(self, pos):
    # Mostrar el menú contextual en la posición del clic
    self.context_menu.exec(self.ui.explorer.mapToGlobal(pos))
        
def create_shortcuts(self):
    # Atajo para copiar (Ctrl+C)
    self.copy_shortcut = QShortcut(QKeySequence.Copy, self)
    self.copy_shortcut.activated.connect(self.copy_to_clipboard)

    # Atajo para pegar (Ctrl+V)
    self.paste_shortcut = QShortcut(QKeySequence.Paste, self)
    self.paste_shortcut.activated.connect(self.paste_from_clipboard)

    # Atajo para eliminar (Delete)
    self.delete_shortcut = QShortcut(QKeySequence.Delete, self)
    self.delete_shortcut.activated.connect(self.delete_item)