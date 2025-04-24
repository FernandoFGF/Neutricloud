from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMenu
from PySide6.QtCore import Qt, QPoint

def create_context_menu(self):
    """Crea el menú contextual para el QCalendarWidget."""
    
    # Crear acciones del menú
    self.add_event_action = QAction('Add event', self)
    self.add_event_action.triggered.connect(self.add_event)

    self.edit_event_action = QAction('Edit event', self)
    self.edit_event_action.triggered.connect(self.edit_event)

    self.delete_event_action = QAction('Delete event', self)
    self.delete_event_action.triggered.connect(self.delete_event)

    # Crear el menú contextual
    self.context_menu = QMenu(self)
    self.context_menu.addAction(self.add_event_action)
    self.context_menu.addAction(self.edit_event_action)
    self.context_menu.addAction(self.delete_event_action) 
    
    # Establecer un estilo personalizado para el menú
    self.context_menu.setStyleSheet("""
        QMenu {
            background-color: #2d2d2d;
            border: 2px solid black;
            border-radius: 5px;
        }
        QMenu::item {
            padding: 10px;
            color: white;
        }
        QMenu::item:selected {
            background-color: #575757;
        }
    """)

    # Conectar el menú al QCalendarWidget
    self.ui.calendarWidget.setContextMenuPolicy(Qt.CustomContextMenu)
    self.ui.calendarWidget.customContextMenuRequested.connect(self.show_context_menu)

def show_context_menu(self, pos: QPoint):
    """Muestra el menú contextual en la posición del clic derecho."""
    self.context_menu.exec(self.ui.calendarWidget.mapToGlobal(pos))
