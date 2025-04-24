# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.setEnabled(True)
        login.resize(305, 400)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMaximumSize(QSize(305, 400))
        palette = QPalette()
        brush = QBrush(QColor(51, 51, 51, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(79, 127, 143, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(0, 128, 191, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(0, 106, 159, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(0, 42, 63, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(0, 56, 84, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush6 = QBrush(QColor(255, 255, 255, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush8 = QBrush(QColor(85, 255, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush9 = QBrush(QColor(0, 85, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
        login.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial,sans-serif"])
        login.setFont(font)
        login.setStyleSheet(u"QWidget {\n"
"    background-color: #4f7f8f;  /* Fondo azul verdoso para la ventana */\n"
"    color: #333333;  /* Texto oscuro para el fondo azul */\n"
"    font-family: \"Arial\", sans-serif;\n"
"    font-size: 16px;  /* Tama\u00f1o de fuente m\u00e1s grande para toda la aplicaci\u00f3n */\n"
"}\n"
"\n"
"QLabel {\n"
"    color: #a8d8a8;  /* Verde claro para el texto de los labels */\n"
"    font-size: 18px;  /* Tama\u00f1o de fuente m\u00e1s grande en los labels */\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #6baed6;  /* Azul suave para los botones */\n"
"    color: white;\n"
"    border: 2px solid #4f7f8f;  /* Borde del bot\u00f3n en color azul verdoso */\n"
"    border-radius: 5px;\n"
"    padding: 10px 20px;\n"
"    font-size: 16px;  /* Tama\u00f1o de fuente m\u00e1s grande en los botones */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #4f7f8f;  /* Al pasar el rat\u00f3n se vuelve m\u00e1s oscuro */\n"
"    color: white;\n"
"    border-color: #6baed6;\n"
""
                        "}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3b6e7d;  /* Cuando se presiona, un tono m\u00e1s oscuro */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: #e0f7fa;  /* Fondo suave de color verde claro para los inputs */\n"
"    border: 1px solid #4f7f8f;  /* Borde verde para los campos de texto */\n"
"    color: #333333;\n"
"    padding: 8px;\n"
"    border-radius: 5px;\n"
"    font-size: 16px;  /* Tama\u00f1o de fuente m\u00e1s grande en los inputs */\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: #a8d8a8;  /* Verde claro para el texto del checkbox */\n"
"    font-size: 16px;  /* Tama\u00f1o de fuente m\u00e1s grande en el checkbox */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: #a8d8a8;  /* Verde claro para el texto del radiobutton */\n"
"    font-size: 16px;  /* Tama\u00f1o de fuente m\u00e1s grande en el radiobutton */\n"
"}\n"
"\n"
"QComboBox {\n"
"    background-color: #e0f7fa;  /* Fondo verde claro */\n"
"    border: 1px solid #4f7f8f;  /* Borde del combobox */\n"
"    color: #333333;\n"
"  "
                        "  font-size: 16px;  /* Tama\u00f1o de fuente m\u00e1s grande en el combobox */\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border-color: #6baed6;  /* Borde azul claro cuando se pasa el rat\u00f3n */\n"
"}\n"
"\n"
"QScrollBar {\n"
"    background-color: #e0f7fa;  /* Fondo verde claro para la barra de desplazamiento */\n"
"    border: 1px solid #4f7f8f;  /* Borde azul verdoso */\n"
"}\n"
"\n"
"QScrollBar::handle {\n"
"    background-color: #6baed6;  /* Color del control de la barra de desplazamiento */\n"
"}\n"
"\n"
"QScrollBar::handle:hover {\n"
"    background-color: #4f7f8f;  /* Color m\u00e1s oscuro cuando se pasa el rat\u00f3n */\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #4f7f8f;  /* Borde para los paneles de las pesta\u00f1as */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #6baed6;  /* Fondo azul claro para las pesta\u00f1as */\n"
"    color: white;\n"
"    padding: 12px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #4f7f8f;  /* Fondo azul"
                        " oscuro para la pesta\u00f1a seleccionada */\n"
"}\n"
"\n"
"QSlider {\n"
"    background-color: #e0f7fa;  /* Fondo verde claro */\n"
"    border: 1px solid #4f7f8f;  /* Borde azul verdoso */\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    background-color: #6baed6;  /* Color del control deslizante */\n"
"    border: 1px solid #4f7f8f;\n"
"}\n"
"\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #4f7f8f;  /* Borde para los paneles de las pesta\u00f1as */\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background-color: #6baed6;  /* Fondo azul claro para las pesta\u00f1as */\n"
"    color: white;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background-color: #4f7f8f;  /* Fondo azul oscuro para la pesta\u00f1a seleccionada */\n"
"}\n"
"\n"
"QSlider {\n"
"    background-color: #e0f7fa;  /* Fondo verde claro */\n"
"    border: 1px solid #4f7f8f;  /* Borde azul verdoso */\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    background-color: #6baed6;  /* Color del control deslizante */\n"
"    border: 1px solid #4f7"
                        "f8f;\n"
"}\n"
"\n"
"")
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush9)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
        self.centralwidget.setPalette(palette1)
        self.centralwidget.setFont(font)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(39, 30, 221, 341))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_user = QLabel(self.verticalLayoutWidget)
        self.label_user.setObjectName(u"label_user")
        palette2 = QPalette()
        brush10 = QBrush(QColor(168, 216, 168, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush10)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        self.label_user.setPalette(palette2)
        self.label_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_user)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.entry_user = QLineEdit(self.verticalLayoutWidget)
        self.entry_user.setObjectName(u"entry_user")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush11 = QBrush(QColor(224, 247, 250, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        self.entry_user.setPalette(palette3)
        self.entry_user.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.entry_user)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_password = QLabel(self.verticalLayoutWidget)
        self.label_password.setObjectName(u"label_password")
        self.label_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_password)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.entry_password = QLineEdit(self.verticalLayoutWidget)
        self.entry_password.setObjectName(u"entry_password")
        self.entry_password.setEchoMode(QLineEdit.Password)
        self.entry_password.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.entry_password)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_8)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.checkBox_remember = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_remember.setObjectName(u"checkBox_remember")
        self.checkBox_remember.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_remember.sizePolicy().hasHeightForWidth())
        self.checkBox_remember.setSizePolicy(sizePolicy1)
        self.checkBox_remember.setLayoutDirection(Qt.LeftToRight)

        self.horizontalLayout.addWidget(self.checkBox_remember)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.button_login = QPushButton(self.verticalLayoutWidget)
        self.button_login.setObjectName(u"button_login")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush12 = QBrush(QColor(107, 174, 214, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush6)
        brush13 = QBrush(QColor(212, 255, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush13)
        brush14 = QBrush(QColor(85, 127, 127, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush14)
        brush15 = QBrush(QColor(113, 170, 170, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush15)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush13)
        brush16 = QBrush(QColor(255, 255, 220, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush16)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush14)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush15)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush13)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush16)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush14)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush15)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush12)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush17 = QBrush(QColor(170, 255, 255, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush17)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush16)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush7)
        self.button_login.setPalette(palette4)

        self.horizontalLayout_2.addWidget(self.button_login)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_result = QLabel(self.verticalLayoutWidget)
        self.label_result.setObjectName(u"label_result")
        self.label_result.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_result)

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"Neutricloud", None))
        self.label_user.setText(QCoreApplication.translate("login", u"User", None))
        self.label_password.setText(QCoreApplication.translate("login", u"Password", None))
        self.checkBox_remember.setText(QCoreApplication.translate("login", u"Remember", None))
        self.button_login.setText(QCoreApplication.translate("login", u"Login", None))
        self.label_result.setText("")
    # retranslateUi

