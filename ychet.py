# -*- coding: utf-8 -*-
import sys
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import datetime
import pandas as pd
import os
import time
from langdetect import detect

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)


def print_to_file(items):
    name = f'резервная_копия.txt'
    with open(name, 'a') as file:
        # file.write(
        #     f'Номер | Время | Сотрудник |'
            # f' Название оборудования | Серийный номер | Отсканированная строка |\n')
        if len(items.line) >= 10:
            file.write('* |'+str(items))
            file.write('\n')



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(982, 916)
        MainWindow.setMinimumSize(QSize(800, 800))
        MainWindow.setStyleSheet(u"background-color: rgb(192, 191, 188);\n"
"background-color: rgb(222, 221, 218);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.error_label_1 = QLabel(self.centralwidget)
        self.error_label_1.setObjectName(u"error_label_1")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.error_label_1.setFont(font)
        self.error_label_1.setLayoutDirection(Qt.LeftToRight)
        self.error_label_1.setStyleSheet(u"color: rgb(237, 51, 59);")
        self.error_label_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.error_label_1, 12, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(22)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 5)

        self.working_label = QComboBox(self.centralwidget)
        self.working_label.addItem("")
        self.working_label.addItem("")
        self.working_label.setObjectName(u"working_label")
        self.working_label.setFont(font1)
        self.working_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.working_label, 11, 0, 1, 1)

        self.check_button = QPushButton(self.centralwidget)
        self.check_button.setObjectName(u"check_button")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.check_button.sizePolicy().hasHeightForWidth())
        self.check_button.setSizePolicy(sizePolicy)
        self.check_button.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.check_button.setFont(font2)
        self.check_button.setStyleSheet(u"background-color: rgb(46, 194, 126);")

        self.gridLayout.addWidget(self.check_button, 5, 0, 1, 6)

        self.result_label_2 = QLabel(self.centralwidget)
        self.result_label_2.setObjectName(u"result_label_2")
        self.result_label_2.setMinimumSize(QSize(0, 60))
        self.result_label_2.setFont(font2)
        self.result_label_2.setLayoutDirection(Qt.LeftToRight)
        self.result_label_2.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.result_label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.result_label_2, 10, 0, 1, 6)

        self.label6 = QLabel(self.centralwidget)
        self.label6.setObjectName(u"label6")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.label6.setFont(font3)
        self.label6.setLayoutDirection(Qt.LeftToRight)
        self.label6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label6, 9, 0, 1, 6)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font4 = QFont()
        font4.setPointSize(17)
        font4.setBold(True)
        self.pushButton_2.setFont(font4)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.gridLayout.addWidget(self.pushButton_2, 14, 4, 1, 2)

        self.error_label_2 = QLabel(self.centralwidget)
        self.error_label_2.setObjectName(u"error_label_2")
        self.error_label_2.setFont(font)
        self.error_label_2.setLayoutDirection(Qt.LeftToRight)
        self.error_label_2.setStyleSheet(u"color: rgb(237, 51, 59);")
        self.error_label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.error_label_2, 12, 3, 1, 2)

        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(0, 60))
        self.result_label.setFont(font2)
        self.result_label.setLayoutDirection(Qt.LeftToRight)
        self.result_label.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.result_label, 8, 0, 1, 6)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 3, 0, 1, 6)

        self.taking_label = QComboBox(self.centralwidget)
        self.taking_label.addItem("")
        self.taking_label.addItem("")
        self.taking_label.setObjectName(u"taking_label")
        self.taking_label.setFont(font1)
        self.taking_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.taking_label, 11, 4, 1, 2)

        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy1)
        self.add_button.setMaximumSize(QSize(16777215, 16777215))
        self.add_button.setFont(font4)
        self.add_button.setStyleSheet(u"background-color: rgb(46, 194, 126);\n"
"")

        self.gridLayout.addWidget(self.add_button, 14, 0, 1, 4)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 6)

        self.region_label = QComboBox(self.centralwidget)
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.setObjectName(u"region_label")
        self.region_label.setFont(font1)
        self.region_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.region_label, 11, 1, 1, 3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 6)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 4)

        self.input_label = QTextEdit(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMaximumSize(QSize(16777215, 150))
        self.input_label.setFont(font2)
        self.input_label.setLayoutDirection(Qt.LeftToRight)
        self.input_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.input_label, 4, 0, 1, 6)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMinimumSize(QSize(40, 70))
        self.comboBox.setFont(font4)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 6)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 13, 0, 1, 1)

        self.station = QTextEdit(self.centralwidget)
        self.station.setObjectName(u"station")
        self.station.setMaximumSize(QSize(16777215, 150))
        self.station.setFont(font2)
        self.station.setLayoutDirection(Qt.LeftToRight)
        self.station.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.station, 13, 1, 1, 5)

        self.load1 = QLabel(self.centralwidget)
        self.load1.setObjectName(u"load1")
        self.load1.setFont(font3)
        self.load1.setLayoutDirection(Qt.LeftToRight)
        self.load1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.load1, 15, 3, 1, 3)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 15, 0, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.label_3.raise_()
        self.label_5.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.input_label.raise_()
        self.check_button.raise_()
        self.label_2.raise_()
        self.label_8.raise_()
        self.result_label.raise_()
        self.label6.raise_()
        self.result_label_2.raise_()
        self.progressBar.raise_()
        self.label_6.raise_()
        self.taking_label.raise_()
        self.working_label.raise_()
        self.load1.raise_()
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.working_label.setCurrentIndex(0)
        self.taking_label.setCurrentIndex(0)
        self.region_label.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043d\u043e \u0434\u043b\u044f \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u044f", None))
        self.error_label_1.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.working_label.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u0440\u0430\u0432\u043d\u043e", None))
        self.working_label.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e", None))

        self.check_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.result_label_2.setText("")
        self.label6.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.error_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a", None))
        self.result_label.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u0435\u0441\u0442\u0438\u0442\u0435 \u043a\u0443\u0440\u0441\u043e\u0440 \u0432 \u043d\u0438\u0436\u043d\u0435\u0435 \u043f\u043e\u043b\u0435 \u0438 \u043d\u0430\u0447\u0438\u043d\u0430\u0439\u0442\u0435 \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.taking_label.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0430\u044e", None))
        self.taking_label.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0443", None))

        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.region_label.setItemText(0, QCoreApplication.translate("MainWindow", u"1 \u0426\u0435\u043d\u0442\u0440", None))
        self.region_label.setItemText(1, QCoreApplication.translate("MainWindow", u"2 \u0421\u0412", None))
        self.region_label.setItemText(2, QCoreApplication.translate("MainWindow", u"3 \u042e\u0412", None))
        self.region_label.setItemText(3, QCoreApplication.translate("MainWindow", u"5 \u0421\u0417", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u043b\u0438 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430 \u043d\u0435\u0442, \u0442\u043e \u0432\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \"\u0434\u0440\u0443\u0433\u043e\u0435\"", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0422\u0435\u0441\u0442\u043e\u0432\u0438\u0447", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0441\u0435\u043d\u043e\u0432 \u0410\u043d\u0442\u043e\u043d \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u043f\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u0412\u0438\u043a\u0442\u043e\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0411\u043e\u0433\u0430\u0442\u0447\u0443\u043a \u041e\u043b\u0435\u0433 \u0412\u0438\u043a\u0442\u043e\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043d\u043d\u0438\u043a\u043e\u0432 \u0414\u043c\u0438\u0442\u0440\u0438\u0439 \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u0438\u043b\u043e\u0432 \u041b\u0435\u0432 \u0410\u043d\u0434\u0440\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0414\u0443\u043d\u0430\u0435\u0432 \u041c\u0438\u0445\u0430\u0438\u043b\n"
"", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0417\u0432\u043e\u0440\u044b\u0433\u0438\u043d \u041d\u0438\u043a\u043e\u043b\u0430\u0439 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0417\u0438\u0433\u0430\u043d\u0448\u0438\u043d \u0420\u0438\u0448\u0430\u0442 \u0418\u043b\u044c\u0434\u0430\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"\u0417\u044b\u0431\u0440\u0438\u043a\u043e\u0432 \u0410\u0440\u0442\u0435\u043c", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0437\u0430\u043a\u043e\u0432 \u0414\u043c\u0438\u0442\u0440\u0438\u0439 \u0412\u0430\u0441\u0438\u043b\u044c\u0435\u0432\u0438\u0447", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u043f\u043e\u0432 \u041a\u043e\u043d\u0441\u0442\u0430\u043d\u0442\u0438\u043d", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u043f\u043e\u0432\u0438\u0447 \u0410\u043d\u0434\u0440\u0435\u0439 \u042f\u043a\u043e\u0432\u043b\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"\u041a\u0438\u043c \u0411\u043e\u0440\u0438\u0441 \u0412\u0438\u0442\u0430\u043b\u044c\u0435\u0432\u0438\u0447", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u043e\u043b\u0435\u0432 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u0415\u0432\u0433\u0435\u043d\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0442\u0435\u043b\u044c\u043d\u0438\u043a\u043e\u0432 \u0420\u043e\u043c\u0430\u043d \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0437\u043d\u0435\u0446\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0437\u0430\u0435\u0432 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u0410\u043d\u0430\u0442\u043e\u043b\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"\u041c\u0443\u0445\u0430\u043c\u044f\u0442\u0436\u0430\u043d\u043e\u0432 \u0410\u0439\u0440\u0430\u0442 \u0428\u0430\u043c\u0438\u043b\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0441\u0442\u0435\u0440\u0435\u043d\u043a\u043e \u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(20, QCoreApplication.translate("MainWindow", u"\u041e\u043b\u0435\u0439\u043d\u0438\u043a \u0412\u0438\u0442\u0430\u043b\u0438\u0439", None))
        self.comboBox.setItemText(21, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u0442\u0435\u0440\u043d\u0438\u043a\u043e\u0432 \u0418\u0433\u043e\u0440\u044c \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(22, QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0434\u0438\u043a\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(23, QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u0438\u043f\u043d\u0438\u0447\u0435\u043d\u043a\u043e \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440 \u0412\u0438\u043a\u0442\u043e\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(24, QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043b\u0435\u0439\u043c\u0430\u043d\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u0412\u0430\u043b\u0435\u0440\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(25, QCoreApplication.translate("MainWindow", u"\u0422\u0440\u043e\u043d\u0438\u0446\u043a\u0438\u0439 \u0420\u043e\u043c\u0430\u043d \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(26, QCoreApplication.translate("MainWindow", u"\u0423\u0442\u0438\u043d \u0413\u0440\u0438\u0433\u043e\u0440\u0438\u0439", None))
        self.comboBox.setItemText(27, QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0440\u043d\u0435\u043d\u043a\u043e\u0432 \u0420\u043e\u043c\u0430\u043d \u0415\u0432\u0433\u0435\u043d\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(28, QCoreApplication.translate("MainWindow", u"\u0425\u0440\u0430\u043c\u043e\u0432 \u042e\u0440\u0438\u0439 \u0412\u044f\u0447\u0435\u0441\u043b\u0430\u0432\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(29, QCoreApplication.translate("MainWindow", u"\u0428\u0443\u0445\u043d\u043e\u0432 \u041d\u0438\u043a\u0438\u0442\u0430 \u0412\u0430\u043b\u0435\u0440\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(30, QCoreApplication.translate("MainWindow", u"\u042d\u043b\u044c\u0434\u044b\u0448 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u042e\u0440\u044c\u0435\u0432\u0438\u0447\n"
"", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0446\u0438\u044f:", None))
        self.station.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.load1.setText(QCoreApplication.translate("MainWindow", u"\u0447\u0442\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438", None))
    # retranslateUi




class Item:
    def __init__(self, item: str, serial: str, line: str, name: str):
        self.line: str = line
        self.item: str = item
        self.serial: str = serial
        self.name: str = name
        self.region: str = ''
        self.working: str = ''
        self.station: str = ''
        self.taking: str = ''

    def __str__(self):
        now = datetime.datetime.now()
        self.name = self.name.replace('\n','')
        self.station = self.station.replace('\n','')
        self.taking = self.taking.replace('\n','')
        self.working = self.working.replace('\n','')
        self.line = self.line.replace('\n','')
        return f' {now.strftime("%d-%m-%Y %H:%M")} | {self.name} | {self.station} | {self.taking} ' \
               f'| {self.item} | {self.serial} | {self.working} | {self.line} |'


class Numbers_analyzer:
    def __init__(self):
        self.name: str = ''
        self.lines: list[str] = []
        self.items: list[Item] = []
        self.file_name: str = 'Результат_инвентаризации.txt'

    def analyzer(self, line, special) -> Item:
        def __get_serial_number(line: str) -> str:
            # serial_number_index: int = name[::-1].find('S')
            serial_number_index: int = 10
            if len(line) >= 11:
                if line[-11] == 'S':
                    return line[-serial_number_index:]
            return 'скорее всего прибор должен иметь серийный номер вида S******'

        def __get_name(line: str):

            variants: dict = {'KRC161549/1': 'Приемопередатчик Radio 2217 B20',
                              'KRC161428/1': 'Приемопередатчик Radio 2217 B7',
                              'KRC161622/1': 'Приемопередатчик Radio 2219 B1',
                              'KRC161495/1': 'Приемопередатчик Radio 4415 B7',
                              'KRC161945/1': 'Приемопередатчик Radio 4418 B40 100МГц',
                              'KRC161706/1': 'Приемопередатчик Radio 4418 B40T',
                              'KRC118070/1': 'Приемопередатчик RadioUnit AIR 21 B7A 2P',
                              'KRC11876/1': 'Приемопередатчик RRUS-01 B1',
                              'KRC161255/2': 'Приемопередатчик RRUS-11 B1',
                              'KRC11891/2': 'Приемопередатчик RRUS-11 B20',
                              'KRC161253/1': 'Приемопередатчик RRUS-11 B7',
                              'KRC161605/1': 'Приемопередатчик RRUS-13 B31',
                              'KDU127620/11': 'Цифровой модуль Baseband 6620',
                              'KDU137848/11': 'Цифровой модуль Baseband 6630',
                              'KDU127174/3': 'Цифровой модуль DUW 31 01',
                              # Цифровой модуль DUS 31 01 или
                              'KDU137624/31': 'Цифровой модуль DUS 31 02',
                              'KDU137624/31/5': 'Цифровой модуль DUS 31 02 5MHz',
                              'KDU137624/11': 'Цифровой модуль DUS 41 02',
                              'KDU137739/1': 'Транспортный модуль TCU-02 01',
                              # Цифровой модуль DUW 20
                              'KDU127161/2': 'Цифровой модуль DUW 20 01',
                              'KRD901060/41': 'TRANSCEIVER/RBS 6402;2X B1 B3 B7',
                              'SK-EH-ANT-1FT': 'Антенна 0.3м Siklu',
                              'SK-EH-1200L-ODU-1ft-F': 'Антенна 0.3м Siklu EH-1200L-ODU-1ft-F',
                              'SK-EH-1200L-ODU-EXT': 'Антенна 0.6м Siklu EH-1200L-ODU-EXT',
                              'SK-EH-ANT-2FT': 'Антенна 0.6м Siklu EH-ANT-2ft',
                              'SCX3-127BNEO': 'Антенна 13 ГГц 0,9 м DP HP SCX3-127BNEO',
                              'VHLPX1-13S-NC3': 'Антенна 13GHz-0.3m (ODU I-T with OMT)',
                              'VHLP1-13-NC3-E': 'Антенна 13GHz-0.3m (ODU I-T)',
                              'VFEED-NC3-E-1-13S': 'Антенна 13GHz-0.3m (ODU I-T)',
                              'VHLPX2-13S-NC3': 'Антенна 13GHz-0.6m (ODU I-T with OMT)',
                              'VHLP2-13S-NC3': 'Антенна 13GHz-0.6m (ODU I-T)',
                              'VHLP2-13S-NC3-E': 'Антенна 13GHz-0.6m (ODU I-type)',
                              'VHLPX3-13S-NC3O': 'Антенна 13GHz-0.9m (ODU I-T with OMT)',
                              'VHLPX3-13S-NC3': 'Антенна 13GHz-1.0m (ODU I-T with OMT)',
                              'VHLPX4-13S-NC3': 'Антенна 13GHz-1.2m (ODU I-T with OMT)',
                              'SC2-142AMPT': 'Антенна 15 ГГц 0,6 м SinPol HP SC2-142AMPT',
                              'SCX3-142ANEO': 'Антенна 15 ГГц 0,9 м DualPol HP',
                              'VHLPX2-15-NC3': 'Антенна 15GHz-0.6m (ODU I-T with OMT)',
                              'VHLP2-15-NC3-E': 'Антенна 15GHz-0.6m (ODU I-T)',
                              'VHLP2-15-NC3-F': 'Антенна 15GHz-0.6m (ODU I-T)',
                              'VHLP2.5-15-NC3-B': 'Антенна 15GHz-0.8m (ODU I-T)',
                              'VHLPX3-15-NC3': 'Антенна 15GHz-1.0m (ODU I-T with OMT)',
                              'VHLP3-15-NC3-E': 'Антенна 15GHz-1.0m (ODU I-type)',
                              '15GCDMA': 'Антенна 15GHz-1.2m (CDMA)',
                              'VHLPX4-15-NC3': 'Антенна 15GHz-1.2m (ODU I-T with OMT)',
                              'VHLP4-15-NC3-E': 'Антенна 15GHz-1.2m (ODU I-T)',
                              'VHLP4-15-NC3-F': 'Антенна 15GHz-1.2m (ODU I-T)',
                              'VHLP6-15-NC3': 'Антенна 15GHz-1.8m (ODU I-T)',
                              'SBX1-190CNEO': 'Антенна 18 ГГц 0,3 м DualPol HP',
                              'SB1-190CNEC': 'Антенна 18 ГГц 0,3 м SinglePol SB1-190C',
                              'SC1-190ANEC': 'Антенна 18 ГГц 0,3 м SinPol HP SC1-190A',
                              'SCX2-190CNEO': 'Антенна 18 ГГц 0,6 м DP HP SCX2-190CNEO',
                              'SCX2-190BNEO': 'Антенна 18 ГГц 0,6 м DualPol HP',
                              'SC2-190BNEC': 'Антенна 18 ГГц 0,6 м SinglePol SC2-190B',
                              'SC2-190CNEC': 'Антенна 18 ГГц 0,6 м SinPol HP SC2-190С',
                              'VHLPX1-18-NC3-O': 'Антенна 18GHz-0.3m (ODU I-T with OMT)',
                              'VHLP1-18-NC3-E': 'Антенна 18GHz-0.3m (ODU I-T)',
                              'VHLP1-18-NC3-F': 'Антенна 18GHz-0.3m (ODU I-T)',
                              'VHLPX1-18-NC3': 'Антенна 18GHz-0.3m (ODU I-T) или Антенна 18GHz-0.3m-Dual Pol (ODU I-type)',
                              'VHLPX2-18-NC3-O': 'Антенна 18GHz-0.6m (ODU I-T with OMT)',
                              'VHLP2-18-NC3-E': 'Антенна 18GHz-0.6m (ODU I-T)',
                              'VHLP2-18-NC3-F': 'Антенна 18GHz-0.6m (ODU I-T)',
                              'VHLPX2-18-NC3': 'Антенна 18GHz-0.6m-Dual Pol (ODU I-type)',
                              'VHLPX3-18-NC3O': 'Антенна 18GHz-0.9m (ODU I-T with OMT)',
                              'VHLPX3-18-NC3': 'Антенна 18GHz-0.9m-Dual Pol (ODU I-type)',
                              'VHLP3-18-NC3-E': 'Антенна 18GHz-1.0m (ODU I-type)',
                              'VHLP4-18-NC3-E': 'Антенна 18GHz-1.2m (ODU I-type)',
                              'SBX1-220CNEO': 'Антенна 23 ГГц 0,3 м DualPol HP',
                              'HAE1-23-NECR2A': 'Антенна 23 Ггц 0,3 м SinglePol HP',
                              'SB1-220CNEC': 'Антенна 23 ГГц 0,3 м SinglePol SB1-220C',
                              'SB1-220CMPT': 'Антенна 23 ГГц 0,3 м SinglePol SB1-220CMPT',
                              'SC1-220ANEC': 'Антенна 23 ГГц 0,3 м SinPol HP SC1-220A',
                              'SCX2-220CNEO': 'Антенна 23 ГГц 0,6 м DP HP SCX2-220CNEO',
                              'SCX2-220BNEO': 'Антенна 23 ГГц 0,6 м DualPol HP',
                              'HAE2-23-NECR3A': 'Антенна 23 Ггц 0,6 м SinglePol HP',
                              'SC2-220CUBTR': 'Антенна 23 ГГц 0,6 м SinPol HP SC2-220CUBTR',
                              'VHLPX1-23-NC3': 'Антенна 23GHz-0.3m (ODU I-T with OMT)',
                              'VHLP1-23-NC3-E': 'Антенна 23GHz-0.3m (ODU I-T)',
                              'VHLP1-23-NC3-Q': 'Антенна 23GHz-0.3m (ODU I-T)',
                              'VHLP1-23-NC3-G': 'Антенна 23GHz-0.3m (ODU I-T)',
                              'VHLPX2-23-NC3O': 'Антенна 23GHz-0.6m (ODU I-T with OMT)',
                              'VHLP2-23-NC3-E': 'Антенна 23GHz-0.6m (ODU I-T)',
                              'VFEED-NC3-E-2-23': 'Антенна 23GHz-0.6m (ODU I-T)',
                              'VHLP2-23-NC3-F': 'Антенна 23GHz-0.6m (ODU I-T)',
                              'SBX1-380CNEO': 'Антенна 38 ГГц 0,3 м DualPol HP',
                              'HAE1-38-NECR1A': 'Антенна 38 Ггц 0,3 м SinglePol HP',
                              'SB1-380CNEC': 'Антенна 38 ГГц 0,3 м SinglePol SB1-380C',
                              'VHLPX1-38-NC3-O': 'Антенна 38GHz-0.3m (ODU I-T with OMT)',
                              'VHLP1-38-NC3-E': 'Антенна 38GHz-0.3m (ODU I-T)',
                              'VHLP2-38-NC3': 'Антенна 38GHz-0.6m (ODU I-T)',
                              'VHLP2-38-NC3-E': 'Антенна 38GHz-0.6m (ODU I-T)',
                              'HU-A80S03HAC': 'Антенна 80GHz-0.3m-27dB,HP,SinglePol',
                              'HU-A80S06HAC': 'Антенна 80GHz-0.6m-27dB,HP,SinglePol',
                              'NWA-055300-322': 'Карта Модема (MODEM-A)',
                              'NC-NWA-096324': 'Карта Модема (MODEM-AV)',
                              'NC-NWA-A03700-102': 'Карта Модема (MODEM-EV)',
                              'MDP-400MB-1AA': 'Корзина Ipaso 400',
                              'MDP-1200MB-1BB': 'Блок Ipaso VR10',
                              'MDP-400MB-1BB': 'Корзина Ipaso 1000',
                              'MDP-1200MB-1AA': 'Блок Ipaso VR4',
                              }

            IDs: list[str] = ['KRC161549/1', 'KRC161428/1', 'KRC161622/1', 'KRC161495/1', 'KRC161945/1',
                              'KRC161706/1', 'KRC118070/1', 'KRC11876/1', 'KRC11876/1', 'KRC161255/2',
                              'KRC11891/2', 'KRC161253/1', 'KRC161253/1', 'KRC161605/1',
                              'KDU127620/11', 'KDU137848/11', 'KDU137739/1',
                              'KDU127174/3', 'KDU137624/31', 'KDU137624/31/5', 'KDU137624/11', 'KDU127161/2',
                              'KRD901060/41',
                              'SK-EH-ANT-1FT', 'SK-EH-1200L-ODU-1ft-F', 'SK-EH-1200L-ODU-EXT',
                              'SK-EH-ANT-2FT',
                              'SCX3-127BNEO', 'VHLPX1-13S-NC3', 'VHLP1-13-NC3-E',
                              'VFEED-NC3-E-1-13S',
                              'VHLPX2-13S-NC3', 'VHLP2-13S-NC3', 'VHLP2-13S-NC3-E',
                              'VHLPX3-13S-NC3O', 'VHLPX3-13S-NC3', 'VHLPX4-13S-NC3',
                              'SC2-142AMPT', 'SCX3-142ANEO', 'VHLPX2-15-NC3',
                              'VHLP2-15-NC3-E', 'VHLP2-15-NC3-F', 'VHLP2.5-15-NC3-B',
                              'VHLPX3-15-NC3', 'VHLP3-15-NC3-E',
                              '15GCDMA',
                              'VHLPX4-15-NC3', 'VHLP4-15-NC3-E', 'VHLP4-15-NC3-F',
                              'VHLP6-15-NC3',
                              'SBX1-190CNEO', 'SB1-190CNEC', 'SC1-190ANEC', 'SCX2-190CNEO', 'SCX2-190BNEO',
                              'SC2-190BNEC',
                              'SC2-190CNEC',
                              'VHLPX1-18-NC3-O', 'VHLP1-18-NC3-E', 'VHLP1-18-NC3-F', 'VHLPX1-18-NC3',
                              'VHLPX2-18-NC3-O',
                              'VHLP2-18-NC3-E', 'VHLP2-18-NC3-F', 'VHLPX2-18-NC3', 'VHLPX3-18-NC3O',
                              'VHLPX3-18-NC3', 'VHLP3-18-NC3-E', 'VHLP4-18-NC3-E',
                              'SBX1-220CNEO',
                              'HAE1-23-NECR2A',
                              'SB1-220CNEC', 'SB1-220CMPT', 'SC1-220ANEC', 'SCX2-220CNEO', 'SCX2-220BNEO',
                              'HAE2-23-NECR3A',
                              'SC2-220CUBTR',
                              'VHLPX1-23-NC3', 'VHLP1-23-NC3-E', 'VHLP1-23-NC3-Q', 'VHLP1-23-NC3-G',
                              'VHLPX2-23-NC3O', 'VHLP2-23-NC3-E', 'VFEED-NC3-E-2-23',
                              'VHLP2-23-NC3-F', 'SBX1-380CNEO', 'HAE1-38-NECR1A', 'SB1-380CNEC',
                              'VHLPX1-38-NC3-O', 'VHLP1-38-NC3-E', 'VHLP2-38-NC3', 'VHLP2-38-NC3-E',
                              'HU-A80S03HAC', 'HU-A80S06HAC',
                              'NWA-055300-322', 'NC-NWA-096324', 'NC-NWA-A03700-102',
                              'MDP-400MB-1AA', 'MDP-1200MB-1BB', 'MDP-400MB-1BB', 'MDP-1200MB-1AA']
            correct_number: str = ''
            line = line.replace('\n', '')
            line = line.replace(' ', '')
            for number in IDs:
                if (number in line or line in number) and line != '':
                    correct_number = number
                    break

            name = variants[correct_number] if correct_number != '' else ''
            return name

        def __TRP_analyzer(line: str, name) -> Item:
            def __fill_name():
                if line.find('MODEM-EA') != -1:
                    return 'MODEM-EA'

                item: str = f'Радиоблок {line_[:index]}'
                if 'lo' in params[-1].lower() or 'lo' in line_.lower():
                    params[-1] = 'Low'
                elif 'hi' in params[-1].lower() or 'hi' in line_.lower():
                    params[-1] = 'High'
                if params[-1] == 'High' or params[-1] == 'Low' and len(params[-2]) == 1:
                    item += f' {params[-2]}-{params[-1]}'
                    return item

                index_for_low_or_high = 0
                if params[-1] == 'High':
                    index_for_low_or_high = line_.lower().find('high')
                if params[-1] == 'Low':
                    index_for_low_or_high = line_.lower().find('low')
                new_line = reversed(line_[:index_for_low_or_high])
                for char in new_line:
                    if char.isalpha():
                        item += f' {char}-{params[-1]}'
                        return item

            line_ = line.replace('\n', '').rstrip()
            line_ = line_.replace(' ', '')
            index: int = line_.find(',')
            params = line_.split(',')
            while len(params[-1]) == 0:
                params.pop()

            item = __fill_name()
            serial = params[2]
            while serial[0] == '0':
                serial = serial[1:]
            return Item(name=name, serial=serial, line=line, item=item)

        if not special:
            name = ''
            if line.count(',') > 0 and (line.find('TRP') != -1 or line.find('NWA') != -1) and line.find('MDP') == -1:
                return __TRP_analyzer(line, name)
            else:
                line = line.rstrip()
                item: str = __get_name(line)
                serial: str = __get_serial_number(line)
                if line.find('MDP') != -1:
                    line_ = line.replace('\n', '').rstrip()
                    line_ = line_.replace(' ', '')
                    params = line_.split(',')
                    serial = params[2]
                    while serial[0] == '0':
                        serial = serial[1:]
                return Item(item, serial, line, name)
        else:
            pass
        # TODO add


class Google_sheets():
    def __init__(self):
        CREDENTIALS_FILE = 'creds.json'
        self.spreadsheet_id = '17M3TZf863oP0lsw3efMPXbZelDqlApPfUbBZn3AX_0U'
        # Авторизуемся и получаем service — экземпляр доступа к API
        credentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE,
            ['https://www.googleapis.com/auth/spreadsheets',
             'https://www.googleapis.com/auth/drive'])
        httpAuth = credentials.authorize(httplib2.Http())
        # self.service = googleapiclient.discovery.build('sheets', 'v4', http=httpAuth)
        try:
            self.service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials)
        except:
            DISCOVERY_SERVICE_URL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
            self.service = googleapiclient.discovery.build('sheets', 'v4', credentials=credentials,
                                                           discoveryServiceUrl=DISCOVERY_SERVICE_URL)

    def write(self, page, params) -> None:
        # чтение из файла для получения последней строки
        # в следующую запишем новую строку
        values = self.service.spreadsheets().values().get(
            spreadsheetId=self.spreadsheet_id,
            range=f'{page}!A1:B10000',
            majorDimension='COLUMNS'
        ).execute()
        # pprint(len(values['values'][0]))

        count_records: int = len(values['values'][0])

        # Пример записи в файл
        values = self.service.spreadsheets().values().batchUpdate(
            spreadsheetId=self.spreadsheet_id,
            body={
                "valueInputOption": "USER_ENTERED",
                "data": [
                    {"range": f"{page}!A{count_records + 1}:H{count_records + 1}",
                     "majorDimension": "ROWS",
                     "values": [params]},

                ]
            }
        ).execute()


class GUI_controller(QMainWindow):
    def __init__(self, parent=None):
        super(GUI_controller, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.check_button.clicked.connect(self.analyzer)
        self.ui.add_button.clicked.connect(self.add_to_table)
        self.ui.pushButton_2.clicked.connect(self.delete)
        self.item = Item
        # self.ui.special_label.hide()
        self.ui.label_5.hide()
        self.ui.label_3.hide()
        self.ui.error_label_1.hide()
        self.ui.error_label_2.hide()
        self.ui.progressBar.hide()
        self.ui.load1.hide()
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMinimum(10)
        self.ui.progressBar.setRange(0, 10)

    def __check_language(self):
        # while detect(self.ui.station.toPlainText()) !='eng':
        error = ["bg", "mk", "uk"]
        if self.ui.station.toPlainText() is not None and self.ui.station.toPlainText() != '' and detect(
                self.ui.station.toPlainText()) in error:
            print(detect(self.ui.station.toPlainText()))
            self.ui.error_label_1.show()
            self.ui.error_label_2.show()
            return False
        return True

        # TODO ADD special analys

    def analyzer(self):
        # Number analyzer
        start_time = datetime.datetime.now()
        analyzer = Numbers_analyzer()
        special = False
        if self.ui.input_label.toPlainText() == '' or self.ui.input_label.toPlainText() == '\n':
            self.ui.input_label.setText('Обязательное поле')
            self.ui.input_label.setStyleSheet("color: rgb(255, 0, 0)")
        else:
            self.item = analyzer.analyzer(self.ui.input_label.toPlainText(), special)
            self.ui.result_label.setText(self.item.item) if self.item.item else self.ui.result_label.setText(
                'Вероятно этого оборудования нет в базе')
            self.ui.result_label_2.setText(self.item.serial)
        print('analyze ', datetime.datetime.now() - start_time)

    def delete(self):
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.input_label.clear()
        self.ui.result_label.clear()
        self.ui.result_label_2.clear()
        self.ui.station.clear()

    def debug_print(self):
        print(f'name - {self.item.name}')
        print(f'item - {self.item.item}')
        print(f'region - {self.item.region}')
        print(f'working - {self.item.working}')
        print(f'taking - {self.item.taking}')
        print(f'station - {self.item.station}')

    def add_to_table(self):
        start_time = datetime.datetime.now()
        self.ui.error_label_1.hide()
        self.ui.error_label_2.hide()
        self.ui.load1.hide()

        flag = True
        if self.ui.station.toPlainText() == 'Обязательное поле':
            self.ui.station.setText('')

        if self.ui.station.toPlainText().rstrip() == '':
            self.ui.station.setText('Обязательное поле')
            self.ui.station.setStyleSheet("color: rgb(255, 0, 0)")
            flag = False

        if self.ui.input_label.toPlainText() == 'Обязательное поле':
            self.ui.input_label.setText('')

        if self.ui.input_label.toPlainText() == '':
            self.ui.input_label.setText('Обязательное поле')
            self.ui.input_label.setStyleSheet("color: rgb(255, 0, 0)")
            flag = False

        if self.__check_language() and flag:
            self.ui.progressBar.show()
            self.ui.load1.show()
            self.ui.progressBar.setValue(1)
            self.ui.load1.setText('чтение имени')
            self.item.name = self.ui.comboBox.currentText().replace('\n', '')
            self.ui.progressBar.setValue(2)
            self.ui.load1.setText('чтение состояния')
            self.item.working = self.ui.working_label.currentText()
            self.ui.progressBar.setValue(3)
            self.ui.load1.setText('чтение региона')
            self.item.region = self.ui.region_label.currentText()
            self.ui.progressBar.setValue(4)
            self.ui.load1.setText('чтение действия')
            self.item.taking = self.ui.taking_label.currentText()
            self.ui.progressBar.setValue(5)
            self.ui.load1.setText('чтение станции')
            self.item.station = self.ui.station.toPlainText().replace('\n', '')
            print_to_file(self.item)
            self.ui.progressBar.setValue(6)
            # self.debug_print()
            # Google_sheets_controller
            self.ui.load1.setText('подключение к таблице')
            controller = Google_sheets()
            self.ui.progressBar.setValue(7)
            now = datetime.datetime.now()
            params = [f'{now.strftime("%d-%m-%Y %H:%M")}', self.item.name, self.item.station,
                      self.item.taking, self.item.item, self.item.serial, self.item.working, self.item.line]

            pages = ['Центр', 'СВ', 'ЮВ', 'СВ']
            self.ui.load1.setText('получение страницы таблицы')
            self.ui.progressBar.setValue(8)
            input_page = self.item.region
            page = ''
            for p in pages:
                if p in input_page or input_page in p:
                    page = p
                    break
            self.ui.progressBar.setValue(9)
            self.ui.load1.setText('запись')
            controller.write(page, params)
            self.ui.progressBar.setValue(10)
            self.ui.progressBar.hide()
            self.ui.load1.hide()
            self.ui.input_label.clear()
            self.ui.result_label.clear()
            self.ui.result_label_2.clear()
            self.ui.station.clear()
        print('write ', datetime.datetime.now() - start_time)


def Controller():
    # GUI_controller()
    app = QApplication()
    window = GUI_controller()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    Controller()
