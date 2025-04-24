# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'event.ui'
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDialog, QHBoxLayout,
    QLineEdit, QPushButton, QSizePolicy, QTimeEdit,
    QVBoxLayout, QWidget)

class Ui_event(object):
    def setupUi(self, event):
        if not event.objectName():
            event.setObjectName(u"event")
        event.resize(400, 350)
        event.setMaximumSize(QSize(400, 350))
        event.setStyleSheet(u"QWidget {\n"
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
"}")
        self.verticalLayoutWidget = QWidget(event)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 381, 331))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title = QLineEdit(self.verticalLayoutWidget)
        self.title.setObjectName(u"title")

        self.verticalLayout.addWidget(self.title)

        self.description = QLineEdit(self.verticalLayoutWidget)
        self.description.setObjectName(u"description")
        self.description.setMinimumSize(QSize(0, 152))
        self.description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout.addWidget(self.description)

        self.time = QTimeEdit(self.verticalLayoutWidget)
        self.time.setObjectName(u"time")
        self.time.setMinimumSize(QSize(0, 50))
        self.time.setAlignment(Qt.AlignCenter)
        self.time.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout.addWidget(self.time)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancel = QPushButton(self.verticalLayoutWidget)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)

        self.confirm = QPushButton(self.verticalLayoutWidget)
        self.confirm.setObjectName(u"confirm")

        self.horizontalLayout.addWidget(self.confirm)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(event)

        QMetaObject.connectSlotsByName(event)
    # setupUi

    def retranslateUi(self, event):
        event.setWindowTitle(QCoreApplication.translate("event", u"Event", None))
        self.title.setInputMask("")
        self.title.setPlaceholderText(QCoreApplication.translate("event", u"Title", None))
        self.description.setPlaceholderText(QCoreApplication.translate("event", u"Description", None))
        self.cancel.setText(QCoreApplication.translate("event", u"Cancel", None))
        self.confirm.setText(QCoreApplication.translate("event", u"Confirm", None))
    # retranslateUi

