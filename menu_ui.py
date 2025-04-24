# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_menu(object):
    def setupUi(self, menu):
        if not menu.objectName():
            menu.setObjectName(u"menu")
        menu.resize(800, 600)
        menu.setMaximumSize(QSize(800, 600))
        menu.setStyleSheet(u"QWidget {\n"
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
"    font-size: 25px;  /* Tama\u00f1o de fuente m\u00e1s grande en los botones */\n"
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
        self.centralwidget = QWidget(menu)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(-1, 139, 801, 451))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setVerticalSpacing(3)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.button_calendar = QPushButton(self.gridLayoutWidget)
        self.button_calendar.setObjectName(u"button_calendar")
        self.button_calendar.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.button_calendar, 0, 3, 1, 1)

        self.button_meetings = QPushButton(self.gridLayoutWidget)
        self.button_meetings.setObjectName(u"button_meetings")
        self.button_meetings.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.button_meetings, 1, 1, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.pushButton_4, 1, 3, 1, 1)

        self.button_inventory = QPushButton(self.gridLayoutWidget)
        self.button_inventory.setObjectName(u"button_inventory")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_inventory.sizePolicy().hasHeightForWidth())
        self.button_inventory.setSizePolicy(sizePolicy1)
        self.button_inventory.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setFamilies([u"Arial,sans-serif"])
        self.button_inventory.setFont(font)

        self.gridLayout.addWidget(self.button_inventory, 0, 1, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.pushButton_6, 2, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.pushButton_5, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 781, 133))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(27, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.logo = QLabel(self.horizontalLayoutWidget)
        self.logo.setObjectName(u"logo")
        self.logo.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.logo.sizePolicy().hasHeightForWidth())
        self.logo.setSizePolicy(sizePolicy2)
        self.logo.setMinimumSize(QSize(230, 0))
        self.logo.setMaximumSize(QSize(230, 100))
        self.logo.setPixmap(QPixmap(u":/resources/logo.png"))
        self.logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo)

        self.horizontalSpacer_5 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.home = QLabel(self.horizontalLayoutWidget)
        self.home.setObjectName(u"home")
        self.home.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy2)
        self.home.setMinimumSize(QSize(200, 0))
        self.home.setMaximumSize(QSize(200, 100))
        self.home.setPixmap(QPixmap(u":/resources/home.png"))
        self.home.setScaledContents(True)

        self.horizontalLayout.addWidget(self.home)

        self.horizontalSpacer_4 = QSpacerItem(75, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.image_profile = QLabel(self.horizontalLayoutWidget)
        self.image_profile.setObjectName(u"image_profile")
        sizePolicy2.setHeightForWidth(self.image_profile.sizePolicy().hasHeightForWidth())
        self.image_profile.setSizePolicy(sizePolicy2)
        self.image_profile.setMinimumSize(QSize(200, 100))
        self.image_profile.setMaximumSize(QSize(200, 16777215))

        self.verticalLayout.addWidget(self.image_profile)

        self.name_profile = QLabel(self.horizontalLayoutWidget)
        self.name_profile.setObjectName(u"name_profile")
        sizePolicy2.setHeightForWidth(self.name_profile.sizePolicy().hasHeightForWidth())
        self.name_profile.setSizePolicy(sizePolicy2)
        self.name_profile.setMinimumSize(QSize(200, 0))
        self.name_profile.setMaximumSize(QSize(200, 16777215))
        self.name_profile.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.name_profile)


        self.horizontalLayout.addLayout(self.verticalLayout)

        menu.setCentralWidget(self.centralwidget)

        self.retranslateUi(menu)

        QMetaObject.connectSlotsByName(menu)
    # setupUi

    def retranslateUi(self, menu):
        menu.setWindowTitle(QCoreApplication.translate("menu", u"Neutricloud", None))
        self.button_calendar.setText(QCoreApplication.translate("menu", u"Calendar", None))
        self.button_meetings.setText(QCoreApplication.translate("menu", u"Group meetings", None))
        self.pushButton_4.setText(QCoreApplication.translate("menu", u"Cactus", None))
        self.button_inventory.setText(QCoreApplication.translate("menu", u"Inventory", None))
        self.pushButton_6.setText(QCoreApplication.translate("menu", u"Web", None))
        self.pushButton_5.setText(QCoreApplication.translate("menu", u"Wiki", None))
        self.logo.setText("")
        self.home.setText("")
        self.image_profile.setText("")
        self.name_profile.setText("")
    # retranslateUi

