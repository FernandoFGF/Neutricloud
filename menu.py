# menu.py
from PySide6.QtWidgets import QMainWindow
from menu_ui import Ui_menu  # Importa la clase generada desde el archivo .ui

class MenuWindow(QMainWindow):
    def __init__(self, username, password):
        super(MenuWindow, self).__init__()
        self.ui = Ui_menu()
        self.ui.setupUi(self)

        # Establece la información del usuario
        self.ui.name_profile.setText(username)
        self.user=username
        self.password=password
        
        # Conectar el botón de inventario a la función open_inventory
        self.ui.button_inventory.clicked.connect(self.open_inventory)
        # Conectar el botón de calendario a la función open_inventory
        self.ui.button_calendar.clicked.connect(self.open_calendarr)
        # Conectar el botón de meetings a la función open_inventory
        self.ui.button_meetings.clicked.connect(self.open_meetings)


        # Configuración de la ventana
        self.setWindowTitle('Neutrocloud App - Menu')
        self.setFixedSize(self.size())  # Evita que se redimensione

    def open_inventory(self):
        from inventory.inventory import InventoryWindow  # Importación diferida
        # Abre la ventana de inventario
        self.close()
        self.inventory_window = InventoryWindow(self.user, self.password)
        self.inventory_window.show()  # Usa exec() para abrirla como un diálogo modal
    def open_calendarr(self):
        from calendarr.calendarr import CalendarrWindow  # Importación diferida
        # Abre la ventana de inventario
        self.close()
        self.calendarr_window = CalendarrWindow(self.user, self.password)
        self.calendarr_window.show()  # Usa exec() para abrirla como un diálogo modal
    def open_meetings(self):
        from meetings.meetings import MeetingsWindow  # Importación diferida
        # Abre la ventana de inventario
        self.close()
        self.meetings_window = MeetingsWindow(self.user, self.password)
        self.meetings_window.show()  # Usa exec() para abrirla como un diálogo modal
