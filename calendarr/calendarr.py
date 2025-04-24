from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QTextCharFormat, QColor
from calendarr.calendarr_ui import Ui_calendarr
import calendarr.calendarr_context_menu as context
import calendarr.calendarr_actions as actions
from calendarr.evento import Evento
from calendarr.calendarr_config import ConfigManager  # Importamos el nuevo archivo para la configuración
from utils.utils import handle_home_click  # Importar la función desde utils.py


class CalendarrWindow(QMainWindow):
    def __init__(self, user, password, host="150.214.198.59"):
        super(CalendarrWindow, self).__init__()
        self.ui = Ui_calendarr()
        self.ui.setupUi(self)

        self.user = user
        self.password = password
        self.host = host

        # Usamos la clase ConfigManager para cargar la configuración
        self.config_manager = ConfigManager(self.user, self.password, self.host)
        self.config = self.config_manager.load_or_create_config()
        self.highlight_events()
        
        # Configuración del calendario
        self.ui.calendarWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.calendarWidget.customContextMenuRequested.connect(self.show_context_menu)
        
        self.ui.label_home.mousePressEvent = lambda event: handle_home_click(self, event)

        
        context.create_context_menu(self)

    def highlight_events(self):
        """Resalta los días con eventos en el calendario."""
        # Limpia los formatos previos
        self.ui.calendarWidget.setDateTextFormat(QDate(), QTextCharFormat())

        # Establecer el formato para los días con eventos (fondo naranja)
        event_format = QTextCharFormat()
        event_format.setBackground(QColor("#FFA500"))  # Color naranja para los días con eventos

        # Recorrer las fechas con eventos y aplicar el formato
        for date_str in self.config["events"]:
            qdate = QDate.fromString(date_str, "yyyy-MM-dd")
            if qdate.isValid():
                self.ui.calendarWidget.setDateTextFormat(qdate, event_format)

    def get_selected_date(self):
        """Obtiene la fecha seleccionada en el calendario."""
        return self.ui.calendarWidget.selectedDate().toString("yyyy-MM-dd")

    def show_context_menu(self, pos):
        context.show_context_menu(self, pos)

    # Usar las funciones importadas de calendarr_actions
    def add_event(self):
        actions.add_event(self)  # Llama a la función de inventory_actions

    def edit_event(self):
        actions.edit_event(self)  # Llama a la función de inventory_actions

    def delete_event(self):
        actions.delete_event(self)  # Llama a la función de inventory_actions

    def closeEvent(self, event):
        """Cerrar la ventana y desconectar del servidor"""
        self.config_manager.save_config(self.config)  # Guardar la configuración cuando se cierre
        event.accept()