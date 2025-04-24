# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'meetings.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
import resources_rc

class Ui_meetings(object):
    def setupUi(self, meetings):
        if not meetings.objectName():
            meetings.setObjectName(u"meetings")
        meetings.resize(800, 600)
        meetings.setMaximumSize(QSize(800, 600))
        meetings.setStyleSheet(u"QWidget {\n"
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
        self.centralwidget = QWidget(meetings)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 785, 133))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_6 = QSpacerItem(27, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.label_logo = QLabel(self.horizontalLayoutWidget)
        self.label_logo.setObjectName(u"label_logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy1)
        self.label_logo.setMinimumSize(QSize(230, 0))
        self.label_logo.setMaximumSize(QSize(230, 100))
        self.label_logo.setPixmap(QPixmap(u":/resources/logo.png"))
        self.label_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_logo)

        self.horizontalSpacer_5 = QSpacerItem(25, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.label_home = QLabel(self.horizontalLayoutWidget)
        self.label_home.setObjectName(u"label_home")
        self.label_home.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_home.sizePolicy().hasHeightForWidth())
        self.label_home.setSizePolicy(sizePolicy1)
        self.label_home.setMinimumSize(QSize(200, 0))
        self.label_home.setMaximumSize(QSize(200, 100))
        self.label_home.setPixmap(QPixmap(u":/resources/home.png"))
        self.label_home.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_home)

        self.horizontalSpacer_4 = QSpacerItem(75, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_back = QLabel(self.horizontalLayoutWidget)
        self.label_back.setObjectName(u"label_back")
        sizePolicy1.setHeightForWidth(self.label_back.sizePolicy().hasHeightForWidth())
        self.label_back.setSizePolicy(sizePolicy1)
        self.label_back.setMinimumSize(QSize(50, 50))
        self.label_back.setMaximumSize(QSize(50, 50))
        self.label_back.setPixmap(QPixmap(u":/resources/back.png"))
        self.label_back.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_back)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.label_refresh = QLabel(self.horizontalLayoutWidget)
        self.label_refresh.setObjectName(u"label_refresh")
        self.label_refresh.setMinimumSize(QSize(50, 50))
        self.label_refresh.setMaximumSize(QSize(50, 50))
        self.label_refresh.setPixmap(QPixmap(u":/resources/refresh.png"))
        self.label_refresh.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_refresh)


        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(9, 149, 781, 61))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.createMeetings = QPushButton(self.horizontalLayoutWidget_2)
        self.createMeetings.setObjectName(u"createMeetings")

        self.horizontalLayout_4.addWidget(self.createMeetings)

        self.publish = QPushButton(self.horizontalLayoutWidget_2)
        self.publish.setObjectName(u"publish")

        self.horizontalLayout_4.addWidget(self.publish)

        self.label_data = QLabel(self.centralwidget)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setGeometry(QRect(10, 570, 781, 21))
        meetings.setCentralWidget(self.centralwidget)

        self.retranslateUi(meetings)

        QMetaObject.connectSlotsByName(meetings)
    # setupUi

    def retranslateUi(self, meetings):
        meetings.setWindowTitle(QCoreApplication.translate("meetings", u"Neutricloud", None))
        self.label_logo.setText("")
        self.label_home.setText("")
        self.label_back.setText("")
        self.label_refresh.setText("")
        self.createMeetings.setText(QCoreApplication.translate("meetings", u"New Meeting", None))
        self.publish.setText(QCoreApplication.translate("meetings", u"Publish", None))
        self.label_data.setText("")
    # retranslateUi

