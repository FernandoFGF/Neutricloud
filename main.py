import sys
from PySide6.QtWidgets import QApplication
from login import LoginWindow

# Iniciar la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())