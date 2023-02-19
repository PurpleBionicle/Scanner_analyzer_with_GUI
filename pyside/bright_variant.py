# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'bright_variant_to.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
                               QMainWindow, QPushButton, QSizePolicy, QStatusBar,
                               QTextEdit, QVBoxLayout, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(899, 847)
        MainWindow.setStyleSheet(u"\n""background-color: rgb(170, 170, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 150))
        self.textEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.textEdit_2)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(17)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(
            u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
            "background-color: rgb(0, 255, 0);")

        self.verticalLayout.addWidget(self.pushButton)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        font2.setItalic(True)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)
        self.comboBox.setFont(font1)

        self.horizontalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.centralwidget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy1)
        self.comboBox_2.setFont(font1)

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.comboBox_3 = QComboBox(self.centralwidget)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy1)
        self.comboBox_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.comboBox_3)

        self.comboBox_4 = QComboBox(self.centralwidget)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy1)
        self.comboBox_4.setFont(font1)

        self.horizontalLayout_3.addWidget(self.comboBox_4)

        self.pushButton_4 = QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.horizontalLayout_3.addWidget(self.pushButton_4)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.comboBox_5 = QComboBox(self.centralwidget)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.comboBox_5.sizePolicy().hasHeightForWidth())
        self.comboBox_5.setSizePolicy(sizePolicy1)
        self.comboBox_5.setFont(font1)

        self.horizontalLayout_4.addWidget(self.comboBox_5)

        self.comboBox_6 = QComboBox(self.centralwidget)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.comboBox_6.sizePolicy().hasHeightForWidth())
        self.comboBox_6.setSizePolicy(sizePolicy1)
        self.comboBox_6.setFont(font1)

        self.horizontalLayout_4.addWidget(self.comboBox_6)

        self.pushButton_5 = QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.horizontalLayout_4.addWidget(self.pushButton_5)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_9)

        self.comboBox_7 = QComboBox(self.centralwidget)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.comboBox_7.sizePolicy().hasHeightForWidth())
        self.comboBox_7.setSizePolicy(sizePolicy1)
        self.comboBox_7.setFont(font1)

        self.horizontalLayout_6.addWidget(self.comboBox_7)

        self.comboBox_8 = QComboBox(self.centralwidget)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.comboBox_8.sizePolicy().hasHeightForWidth())
        self.comboBox_8.setSizePolicy(sizePolicy1)
        self.comboBox_8.setFont(font1)

        self.horizontalLayout_6.addWidget(self.comboBox_8)

        self.pushButton_8 = QPushButton(self.centralwidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.horizontalLayout_6.addWidget(self.pushButton_8)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.pushButton_7 = QPushButton(self.centralwidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setMaximumSize(QSize(16777215, 16777215))
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setStyleSheet(
            u"background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147));\n"
            "background-color: rgb(0, 255, 0);")

        self.verticalLayout.addWidget(self.pushButton_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041e\u043a\u043d\u043e \u0434\u043b\u044f \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u044f",
                                                             None))
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u041f\u043e\u043c\u0435\u0441\u0442\u0438\u0442\u0435 \u043a\u0443\u0440\u0441\u043e\u0440 \u0432 \u043d\u0438\u0436\u043d\u0435\u0435 \u043f\u043e\u043b\u0435 \u0438 \u043d\u0430\u0447\u0438\u043d\u0430\u0439\u0442\u0435 \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u0435",
                                                      None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u041f\u043e\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0440\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442",
                                                           None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0443", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0430\u044e", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_3.setItemText(0,
                                    QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0443", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0430\u044e", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.pushButton_4.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_5.setItemText(0,
                                    QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0443", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0430\u044e", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.pushButton_5.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_7.setItemText(0,
                                    QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0442\u0440", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainWindow", u"1", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0443", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0430\u044e", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainWindow", u"2", None))

        self.pushButton_8.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_7.setText(
            QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi


class Scanner_Window(QMainWindow):
    def __init__(self, parent=None):
        super(Scanner_Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.current_label: int = 0
        self.ui.label_3.hide()
        self.ui.pushButton.clicked.connect(self.add_label)

    def add_label(self):
        labels = [self.ui.label_3 , self.ui.label_4, self.ui.label_5 , self.ui.label_9]
        if self.current_label<len(labels):
            text = self.ui.textEdit_2.toPlainText()
            labels[self.current_label].setText(text)
            labels[self.current_label].show()
            self.current_label += 1



if __name__ == '__main__':
    app = QApplication()
    window = Scanner_Window()
    window.show()
    sys.exit(app.exec())
