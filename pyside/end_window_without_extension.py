# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'end_variant_with_extension.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QMainWindow,
    QProgressBar, QPushButton, QSizePolicy, QSplitter,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(975, 885)
        MainWindow.setMinimumSize(QSize(800, 800))
        MainWindow.setStyleSheet(u"background-color: rgb(192, 191, 188);\n"
"background-color: rgb(222, 221, 218);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

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
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(100)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(40, 70))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.comboBox.setFont(font1)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout.addWidget(self.comboBox)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.input_label = QTextEdit(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMaximumSize(QSize(16777215, 150))
        self.input_label.setFont(font2)
        self.input_label.setLayoutDirection(Qt.LeftToRight)
        self.input_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.input_label)

        self.check_button = QPushButton(self.centralwidget)
        self.check_button.setObjectName(u"check_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.check_button.sizePolicy().hasHeightForWidth())
        self.check_button.setSizePolicy(sizePolicy1)
        self.check_button.setMaximumSize(QSize(16777215, 16777215))
        self.check_button.setFont(font2)
        self.check_button.setStyleSheet(u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"background-color: rgb(0, 255, 0);")

        self.verticalLayout.addWidget(self.check_button)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.label_8.setFont(font3)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(0, 60))
        self.result_label.setFont(font2)
        self.result_label.setLayoutDirection(Qt.LeftToRight)
        self.result_label.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result_label)

        self.label6 = QLabel(self.centralwidget)
        self.label6.setObjectName(u"label6")
        self.label6.setFont(font3)
        self.label6.setLayoutDirection(Qt.LeftToRight)
        self.label6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label6)

        self.result_label_2 = QLabel(self.centralwidget)
        self.result_label_2.setObjectName(u"result_label_2")
        self.result_label_2.setMinimumSize(QSize(0, 60))
        self.result_label_2.setFont(font2)
        self.result_label_2.setLayoutDirection(Qt.LeftToRight)
        self.result_label_2.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.result_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.result_label_2)

        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.working_label = QComboBox(self.splitter_3)
        self.working_label.addItem("")
        self.working_label.addItem("")
        self.working_label.setObjectName(u"working_label")
        self.working_label.setFont(font)
        self.working_label.setLayoutDirection(Qt.LeftToRight)
        self.splitter_3.addWidget(self.working_label)
        self.region_label = QComboBox(self.splitter_3)
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.setObjectName(u"region_label")
        self.region_label.setFont(font)
        self.region_label.setLayoutDirection(Qt.LeftToRight)
        self.splitter_3.addWidget(self.region_label)
        self.taking_label = QComboBox(self.splitter_3)
        self.taking_label.addItem("")
        self.taking_label.addItem("")
        self.taking_label.setObjectName(u"taking_label")
        self.taking_label.setFont(font)
        self.taking_label.setLayoutDirection(Qt.LeftToRight)
        self.splitter_3.addWidget(self.taking_label)

        self.verticalLayout.addWidget(self.splitter_3)

        self.splitter_4 = QSplitter(self.centralwidget)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Horizontal)
        self.error_label_1 = QLabel(self.splitter_4)
        self.error_label_1.setObjectName(u"error_label_1")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.error_label_1.setFont(font4)
        self.error_label_1.setLayoutDirection(Qt.LeftToRight)
        self.error_label_1.setStyleSheet(u"color: rgb(237, 51, 59);")
        self.error_label_1.setAlignment(Qt.AlignCenter)
        self.splitter_4.addWidget(self.error_label_1)
        self.error_label_2 = QLabel(self.splitter_4)
        self.error_label_2.setObjectName(u"error_label_2")
        self.error_label_2.setFont(font4)
        self.error_label_2.setLayoutDirection(Qt.LeftToRight)
        self.error_label_2.setStyleSheet(u"color: rgb(237, 51, 59);")
        self.error_label_2.setAlignment(Qt.AlignCenter)
        self.splitter_4.addWidget(self.error_label_2)

        self.verticalLayout.addWidget(self.splitter_4)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.label_6 = QLabel(self.splitter_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.label_6)
        self.station = QTextEdit(self.splitter_2)
        self.station.setObjectName(u"station")
        self.station.setMaximumSize(QSize(16777215, 150))
        self.station.setFont(font2)
        self.station.setLayoutDirection(Qt.LeftToRight)
        self.station.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.splitter_2.addWidget(self.station)

        self.verticalLayout.addWidget(self.splitter_2)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.add_button = QPushButton(self.splitter)
        self.add_button.setObjectName(u"add_button")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy2)
        self.add_button.setMaximumSize(QSize(16777215, 16777215))
        self.add_button.setFont(font1)
        self.add_button.setStyleSheet(u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
"background-color: rgb(0, 255, 0);")
        self.splitter.addWidget(self.add_button)
        self.pushButton_2 = QPushButton(self.splitter)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(237, 51, 59);")
        self.splitter.addWidget(self.pushButton_2)

        self.verticalLayout.addWidget(self.splitter)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.working_label.setCurrentIndex(0)
        self.region_label.setCurrentIndex(0)
        self.taking_label.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u043d\u043e \u0434\u043b\u044f \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u044f", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u0433\u043e \u0441\u043f\u0438\u0441\u043a\u0430 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0415\u0441\u043b\u0438 \u043f\u0440\u0435\u0434\u043c\u0435\u0442\u0430 \u043d\u0435\u0442, \u0442\u043e \u0432\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \"\u0434\u0440\u0443\u0433\u043e\u0435\"", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0441\u0442 \u0422\u0435\u0441\u0442\u043e\u0432\u0438\u0447", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0441\u0435\u043d\u043e\u0432 \u0410\u043d\u0442\u043e\u043d \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0410\u0440\u0445\u0438\u043f\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u0412\u0438\u043a\u0442\u043e\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0411\u043e\u0433\u0430\u0442\u0447\u0443\u043a \u041e\u043b\u0435\u0433 \u0412\u0438\u043a\u0442\u043e\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041a\u0438\u043c \u0411\u043e\u0440\u0438\u0441 \u0412\u0438\u0442\u0430\u043b\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043d\u043d\u0438\u043a\u043e\u0432 \u0414\u043c\u0438\u0442\u0440\u0438\u0439 \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0412\u0438\u043d\u043d\u0438\u043a\u043e\u0432 \u0414\u043c\u0438\u0442\u0440\u0438\u0439 \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043d\u0438\u043b\u043e\u0432 \u041b\u0435\u0432 \u0410\u043d\u0434\u0440\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0414\u0443\u043d\u0430\u0435\u0432 \u041c\u0438\u0445\u0430\u0438\u043b\n"
"", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"\u0417\u0432\u043e\u0440\u044b\u0433\u0438\u043d \u041d\u0438\u043a\u043e\u043b\u0430\u0439 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"\u0417\u0438\u0433\u0430\u043d\u0448\u0438\u043d \u0420\u0438\u0448\u0430\u0442 \u0418\u043b\u044c\u0434\u0430\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0437\u0430\u043a\u043e\u0432 \u0414\u043c\u0438\u0442\u0440\u0438\u0439 \u0412\u0430\u0441\u0438\u043b\u044c\u0435\u0432\u0438\u0447", None))
        self.comboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0440\u043f\u043e\u0432\u0438\u0447 \u0410\u043d\u0434\u0440\u0435\u0439 \u042f\u043a\u043e\u0432\u043b\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0440\u043e\u043b\u0435\u0432 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u0415\u0432\u0433\u0435\u043d\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0442\u0435\u043b\u044c\u043d\u0438\u043a\u043e\u0432 \u0420\u043e\u043c\u0430\u043d \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0437\u043d\u0435\u0446\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"\u041a\u0443\u0440\u0437\u0430\u0435\u0432 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u0410\u043d\u0430\u0442\u043e\u043b\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"\u041c\u0443\u0445\u0430\u043c\u044f\u0442\u0436\u0430\u043d\u043e\u0432 \u0410\u0439\u0440\u0430\u0442 \u0428\u0430\u043c\u0438\u043b\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0441\u0442\u0435\u0440\u0435\u043d\u043a\u043e \u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(19, QCoreApplication.translate("MainWindow", u"\u041e\u043b\u0435\u0439\u043d\u0438\u043a \u0412\u0438\u0442\u0430\u043b\u0438\u0439", None))
        self.comboBox.setItemText(20, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0441\u0442\u0435\u0440\u043d\u0438\u043a\u043e\u0432 \u0418\u0433\u043e\u0440\u044c \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(21, QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0434\u0438\u043a\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(22, QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u0438\u043f\u043d\u0438\u0447\u0435\u043d\u043a\u043e \u0412\u043b\u0430\u0434\u0438\u043c\u0438\u0440 \u0412\u0438\u043a\u0442\u043e\u0440\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(23, QCoreApplication.translate("MainWindow", u"\u0421\u0443\u043b\u0435\u0439\u043c\u0430\u043d\u043e\u0432 \u0410\u043b\u0435\u043a\u0441\u0435\u0439 \u0412\u0430\u043b\u0435\u0440\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(24, QCoreApplication.translate("MainWindow", u"\u0422\u0440\u043e\u043d\u0438\u0446\u043a\u0438\u0439 \u0420\u043e\u043c\u0430\u043d \u0421\u0435\u0440\u0433\u0435\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(25, QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0440\u043d\u0435\u043d\u043a\u043e\u0432 \u0420\u043e\u043c\u0430\u043d \u0415\u0432\u0433\u0435\u043d\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(26, QCoreApplication.translate("MainWindow", u"\u0425\u0440\u0430\u043c\u043e\u0432 \u042e\u0440\u0438\u0439 \u0412\u044f\u0447\u0435\u0441\u043b\u0430\u0432\u043e\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(27, QCoreApplication.translate("MainWindow", u"\u0428\u0443\u0445\u043d\u043e\u0432 \u041d\u0438\u043a\u0438\u0442\u0430 \u0412\u0430\u043b\u0435\u0440\u044c\u0435\u0432\u0438\u0447\n"
"", None))
        self.comboBox.setItemText(28, QCoreApplication.translate("MainWindow", u"\u042d\u043b\u044c\u0434\u044b\u0448 \u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440 \u042e\u0440\u044c\u0435\u0432\u0438\u0447\n"
"", None))

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043c\u0435\u0441\u0442\u0438\u0442\u0435 \u043a\u0443\u0440\u0441\u043e\u0440 \u0432 \u043d\u0438\u0436\u043d\u0435\u0435 \u043f\u043e\u043b\u0435 \u0438 \u043d\u0430\u0447\u0438\u043d\u0430\u0439\u0442\u0435 \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.check_button.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.result_label.setText("")
        self.label6.setText(QCoreApplication.translate("MainWindow", u"\u0441\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440:", None))
        self.result_label_2.setText("")
        self.working_label.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u0440\u0430\u0432\u043d\u043e", None))
        self.working_label.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041d\u0435 \u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e", None))

        self.region_label.setItemText(0, QCoreApplication.translate("MainWindow", u"1 \u0426\u0435\u043d\u0442\u0440", None))
        self.region_label.setItemText(1, QCoreApplication.translate("MainWindow", u"2 \u0421\u0412", None))
        self.region_label.setItemText(2, QCoreApplication.translate("MainWindow", u"3 \u042e\u0412", None))
        self.region_label.setItemText(3, QCoreApplication.translate("MainWindow", u"5 \u0421\u0417", None))

        self.taking_label.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0430\u044e", None))
        self.taking_label.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0443", None))

        self.error_label_1.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ", None))
        self.error_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0446\u0438\u044f:", None))
        self.station.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Ubuntu'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
    # retranslateUi

