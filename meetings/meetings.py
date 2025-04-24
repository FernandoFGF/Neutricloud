# meetings_window.py
from PySide6.QtWidgets import QMainWindow
from meetings.meetings_ui import Ui_meetings
import utils.utils as utils
from meetings.meetings_actions import createMeeting
from meetings.publish import PublishDialog  # Importa el diálogo con lógica desde publish.py

class MeetingsWindow(QMainWindow):
    def __init__(self, user, password, host="150.214.198.59"):
        super(MeetingsWindow, self).__init__()
        self.ui = Ui_meetings()
        self.ui.setupUi(self)

        self.user = user
        self.password = password
        self.host = host
        
        self.ui.label_home.mousePressEvent = lambda event: utils.handle_home_click(self, event)
        self.ui.createMeetings.clicked.connect(self.createMeeting)  # Conectar el botón "createMeetings"
        self.ui.publish.clicked.connect(self.openPublishDialog)  # Conectar el botón "publish"

    def createMeeting(self):
        """Añade una nueva reunión en el archivo remoto."""
        createMeeting(self)  # Llamar a la función createMeeting del archivo meetings_actions.py

    def openPublishDialog(self):
        """Abre el diálogo de publicación."""
        dialog = PublishDialog(self)  # Usar PublishDialog que contiene la lógica de interacción
        dialog.exec()  # Abrir el diálogo de manera modal
