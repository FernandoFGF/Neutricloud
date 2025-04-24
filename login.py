import os
import requests
import pickle
from PySide6.QtWidgets import QMainWindow
from login_ui import Ui_login  # Importa el archivo generado desde el .ui

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_login()
        self.ui.setupUi(self)

        # Cargar credenciales guardadas
        self.load_credentials()

        # Conectar la función de login al botón
        self.ui.button_login.clicked.connect(self.login)
        
        # Conectar la tecla 'Enter' en los campos de usuario y contraseña al login
        self.ui.entry_user.returnPressed.connect(self.login)
        self.ui.entry_password.returnPressed.connect(self.login)

    # Función para cargar las credenciales guardadas
    def load_credentials(self):
        if os.path.exists("credentials.pkl"):
            with open("credentials.pkl", "rb") as file:
                user, password = pickle.load(file)
                self.ui.entry_user.setText(user)
                self.ui.entry_password.setText(password)
                self.ui.checkBox_remember.setChecked(True)

    def login(self):
        from menu import MenuWindow  # Importación diferida
        self.ui.label_result.setText("Loading...")
        self.ui.label_result.setStyleSheet("color: black")

        user = self.ui.entry_user.text()
        password = self.ui.entry_password.text()

        if self.ui.checkBox_remember.isChecked():
            with open("credentials.pkl", "wb") as file:
                pickle.dump((user, password), file)

        try:
            # Intentar conectar con el servidor
            response = requests.post('http://150.214.198.59:5000/login', json={'user': user, 'password': password})

            if response.status_code == 200:
                result = response.json()
                if result.get('success'):  # Solo verifica que el servidor respondió
                    self.ui.label_result.setText("Connected successfully!")
                    self.ui.label_result.setStyleSheet("color: green")

                    # Cerrar login y abrir menú
                    self.close()
                    self.menu_window = MenuWindow(user, password)
                    self.menu_window.show()
                else:
                    self.ui.label_result.setText("Login error")
                    self.ui.label_result.setStyleSheet("color: red")
            else:
                self.ui.label_result.setText("Server connection error")
                self.ui.label_result.setStyleSheet("color: red")

        except requests.exceptions.RequestException as e:
            self.ui.label_result.setText(f"Connection error: {e}")
            self.ui.label_result.setStyleSheet("color: red")
