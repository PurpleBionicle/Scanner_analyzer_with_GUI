# -*- coding: utf-8 -*-
import sys
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
import datetime
from langdetect import detect

from PySide6.QtCore import (QCoreApplication,
                            QMetaObject,
                            QSize, Qt)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
                               QMainWindow, QProgressBar, QPushButton, QSizePolicy,
                               QStatusBar, QTextEdit, QWidget)


def print_to_backup_file(items):
    name = f'резервная_копия.txt'
    with open(name, 'a') as file:
        # file.write(f'Номер | Время | Сотрудник |'
        # f' Название оборудования | Серийный номер | Отсканированная строка |\n')
        file.write('* |' + str(items))
        file.write('\n')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(924, 886)
        MainWindow.setMinimumSize(QSize(800, 800))
        MainWindow.setStyleSheet(u"background-color: rgb(192, 191, 188);\n"
                                 "background-color: rgb(222, 221, 218);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"background-color: rgb(237, 51, 59);")

        self.gridLayout.addWidget(self.pushButton_2, 15, 3, 1, 1)

        self.add_button = QPushButton(self.centralwidget)
        self.add_button.setObjectName(u"add_button")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button.sizePolicy().hasHeightForWidth())
        self.add_button.setSizePolicy(sizePolicy)
        self.add_button.setMaximumSize(QSize(16777215, 16777215))
        self.add_button.setFont(font)
        self.add_button.setStyleSheet(u"background-color: rgb(46, 194, 126);\n"
                                      "")

        self.gridLayout.addWidget(self.add_button, 15, 0, 1, 3)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_8.setFont(font1)
        self.label_8.setLayoutDirection(Qt.LeftToRight)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 6, 0, 1, 4)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(20)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setLayoutDirection(Qt.LeftToRight)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 4)

        self.working_label = QComboBox(self.centralwidget)
        self.working_label.addItem("")
        self.working_label.addItem("")
        self.working_label.setObjectName(u"working_label")
        self.working_label.setMaximumSize(QSize(3123214, 16777215))
        font3 = QFont()
        font3.setPointSize(22)
        font3.setBold(True)
        self.working_label.setFont(font3)
        self.working_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.working_label, 11, 0, 2, 1)

        self.result_label = QLabel(self.centralwidget)
        self.result_label.setObjectName(u"result_label")
        self.result_label.setMinimumSize(QSize(0, 60))
        self.result_label.setFont(font2)
        self.result_label.setLayoutDirection(Qt.LeftToRight)
        self.result_label.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.result_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.result_label, 7, 0, 1, 4)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 4)

        self.region_label = QComboBox(self.centralwidget)
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.addItem("")
        self.region_label.setObjectName(u"region_label")
        self.region_label.setMaximumSize(QSize(16777215, 16777215))
        self.region_label.setFont(font3)
        self.region_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.region_label, 11, 1, 1, 2)

        self.error_label_2 = QLabel(self.centralwidget)
        self.error_label_2.setObjectName(u"error_label_2")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.error_label_2.setFont(font4)
        self.error_label_2.setLayoutDirection(Qt.LeftToRight)
        self.error_label_2.setStyleSheet(u"color: rgb(237, 51, 59);")
        self.error_label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.error_label_2, 13, 2, 1, 1)

        self.station = QTextEdit(self.centralwidget)
        self.station.setObjectName(u"station")
        self.station.setMaximumSize(QSize(16777215, 150))
        self.station.setFont(font2)
        self.station.setLayoutDirection(Qt.LeftToRight)
        self.station.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.station, 14, 1, 1, 3)

        self.result_label_2 = QLabel(self.centralwidget)
        self.result_label_2.setObjectName(u"result_label_2")
        self.result_label_2.setMinimumSize(QSize(0, 60))
        self.result_label_2.setFont(font2)
        self.result_label_2.setLayoutDirection(Qt.LeftToRight)
        self.result_label_2.setStyleSheet(u"background-color: rgb(192, 191, 188);")
        self.result_label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.result_label_2, 10, 0, 1, 4)

        self.load1 = QLabel(self.centralwidget)
        self.load1.setObjectName(u"load1")
        self.load1.setFont(font1)
        self.load1.setLayoutDirection(Qt.LeftToRight)
        self.load1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.load1, 16, 2, 1, 2)

        self.label6 = QLabel(self.centralwidget)
        self.label6.setObjectName(u"label6")
        self.label6.setFont(font1)
        self.label6.setLayoutDirection(Qt.LeftToRight)
        self.label6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label6, 8, 0, 1, 4)

        self.error_label_1 = QLabel(self.centralwidget)
        self.error_label_1.setObjectName(u"error_label_1")
        self.error_label_1.setFont(font4)
        self.error_label_1.setLayoutDirection(Qt.LeftToRight)
        self.error_label_1.setStyleSheet(u"color: rgb(237, 51, 59);")
        self.error_label_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.error_label_1, 13, 0, 1, 1)

        self.check_button = QPushButton(self.centralwidget)
        self.check_button.setObjectName(u"check_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.check_button.sizePolicy().hasHeightForWidth())
        self.check_button.setSizePolicy(sizePolicy1)
        self.check_button.setMaximumSize(QSize(16777215, 16777215))
        self.check_button.setFont(font2)
        self.check_button.setStyleSheet(u"background-color: rgb(46, 194, 126);")

        self.gridLayout.addWidget(self.check_button, 3, 0, 1, 4)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setLayoutDirection(Qt.LeftToRight)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 14, 0, 1, 1)

        self.input_label = QTextEdit(self.centralwidget)
        self.input_label.setObjectName(u"input_label")
        self.input_label.setMaximumSize(QSize(16777215, 150))
        self.input_label.setFont(font2)
        self.input_label.setLayoutDirection(Qt.LeftToRight)
        self.input_label.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.input_label, 2, 0, 1, 4)

        self.taking_label = QComboBox(self.centralwidget)
        self.taking_label.addItem("")
        self.taking_label.addItem("")
        self.taking_label.setObjectName(u"taking_label")
        self.taking_label.setFont(font3)
        self.taking_label.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.taking_label, 11, 3, 1, 1)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout.addWidget(self.progressBar, 16, 0, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(100)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy2)
        self.comboBox.setMinimumSize(QSize(40, 70))
        self.comboBox.setFont(font)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 4)

        MainWindow.setCentralWidget(self.centralwidget)
        self.error_label_1.raise_()
        self.pushButton_2.raise_()
        self.error_label_2.raise_()
        self.add_button.raise_()
        self.region_label.raise_()
        self.station.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.input_label.raise_()
        self.check_button.raise_()
        self.label_2.raise_()
        self.result_label.raise_()
        self.result_label_2.raise_()
        self.progressBar.raise_()
        self.label_6.raise_()
        self.taking_label.raise_()
        self.label6.raise_()
        self.label_8.raise_()
        self.load1.raise_()
        self.working_label.raise_()
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow",
                                                             u"\u041e\u043a\u043d\u043e \u0434\u043b\u044f \u0441\u0447\u0438\u0442\u044b\u0432\u0430\u043d\u0438\u044f",
                                                             None))
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow",
                                                           u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443",
                                                           None))
        self.label_8.setText(QCoreApplication.translate("MainWindow",
                                                        u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435",
                                                        None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0437\u0443\u043b\u044c\u0442\u0430\u0442:", None))
        self.working_label.setItemText(0, QCoreApplication.translate("MainWindow",
                                                                     u"\u0418\u0441\u043f\u0440\u0430\u0432\u043d\u043e",
                                                                     None))
        self.working_label.setItemText(1, QCoreApplication.translate("MainWindow",
                                                                     u"\u041d\u0435 \u0438\u0441\u043f\u0440\u0430\u0432\u043d\u043e",
                                                                     None))

        self.result_label.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u041f\u043e\u043c\u0435\u0441\u0442\u0438\u0442\u0435 \u043a\u0443\u0440\u0441\u043e\u0440 \u0432 \u043d\u0438\u0436\u043d\u0435\u0435 \u043f\u043e\u043b\u0435 \u0438 \u043d\u0430\u0447\u0438\u043d\u0430\u0439\u0442\u0435 \u0441\u043a\u0430\u043d\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435",
                                                      None))
        self.region_label.setItemText(0, QCoreApplication.translate("MainWindow", u"1 \u0426\u0435\u043d\u0442\u0440",
                                                                    None))
        self.region_label.setItemText(1, QCoreApplication.translate("MainWindow", u"2 \u0421\u0412", None))
        self.region_label.setItemText(2, QCoreApplication.translate("MainWindow", u"3 \u042e\u0412", None))
        self.region_label.setItemText(3, QCoreApplication.translate("MainWindow", u"5 \u0421\u0417", None))

        self.error_label_2.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0430\u043d\u0433\u043b\u0438\u0439\u0441\u043a\u0438\u0439 \u044f\u0437\u044b\u043a",
                                                              None))
        self.station.setHtml(QCoreApplication.translate("MainWindow",
                                                        u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-family:'Ubuntu'; font-size:20pt; font-weight:600; font-style:normal;\">\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                        "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                        None))
        self.result_label_2.setText("")
        self.load1.setText(QCoreApplication.translate("MainWindow",
                                                      u"\u0447\u0442\u0435\u043d\u0438\u0435 \u0438\u043c\u0435\u043d\u0438",
                                                      None))
        self.label6.setText(QCoreApplication.translate("MainWindow",
                                                       u"\u0441\u0435\u0440\u0438\u0439\u043d\u044b\u0439 \u043d\u043e\u043c\u0435\u0440:",
                                                       None))
        self.error_label_1.setText(QCoreApplication.translate("MainWindow",
                                                              u"\u0418\u0441\u043f\u043e\u043b\u044c\u0437\u0443\u0439\u0442\u0435 ",
                                                              None))
        self.check_button.setText(
            QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0431\u043e\u0442\u0430\u0442\u044c",
                                       None))
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u043d\u0446\u0438\u044f:", None))
        self.taking_label.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u0434\u0430\u044e", None))
        self.taking_label.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0411\u0435\u0440\u0443", None))
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
        self.name = self.name.replace('\n', '')
        self.station = self.station.replace('\n', '')
        self.taking = self.taking.replace('\n', '')
        self.working = self.working.replace('\n', '')
        self.line = self.line.replace('\n', '')
        self.region = self.region.replace('\n', '')
        return f' {now.strftime("%d-%m-%Y %H:%M")} | {self.name} | {self.region} | {self.station} | {self.taking} ' \
               f'| {self.item} | {self.serial} | {self.working} | {self.line} |'


class Numbers_analyzer:
    def __init__(self):
        self.name: str = ''
        self.lines: list[str] = []
        self.items: list[Item] = []
        self.file_name: str = 'Результат_инвентаризации.txt'

    def analyzer(self, line) -> Item:
        name = ''
        if line.count(',') > 0 and (line.find('TRP') != -1 or line.find('NWA') != -1) and line.find('MDP') == -1:
            return self.__TRP_analyzer(line, name)
        else:
            line = line.rstrip()
            item: str = self.__get_name(line)
            serial: str = self.__get_serial_number(line)
            if line.find('MDP') != -1:
                line_ = line.replace('\n', '').rstrip()
                line_ = line_.replace(' ', '')
                params = line_.split(',')
                serial = params[2]
                while serial[0] == '0':
                    serial = serial[1:]
            return Item(item, serial, line, name)

    def __get_name(self, line: str):
        variants, IDs = self.__fill_variants_and_IDs()
        correct_number: str = ''
        line = line.replace('\n', '')
        line = line.replace(' ', '')
        for number in IDs:
            if (number in line or line in number) and line != '':
                correct_number = number
                break

        name = variants[correct_number] if correct_number != '' else ''
        return name

    def __get_serial_number(self, line: str) -> str:
        # serial_number_index: int = name[::-1].find('S')
        serial_number_index: int = 10
        if len(line) >= 11:
            if line[-11] == 'S':
                return line[-serial_number_index:]
        return 'скорее всего прибор должен иметь серийный номер вида S******'

    def __TRP_analyzer(self, line: str, name) -> Item:
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

    def __fill_variants_and_IDs(self):
        variants: dict = {}
        IDs = []
        with open(f'Список_оборудования.txt', 'r+') as file:
            lines: list[str] = file.readlines()
            lines = [x.rstrip() for x in lines]
        for line in lines:
            params = line.split(':')
            variants[params[0]] = params[1]
            IDs.append(params[0])

        return variants, IDs


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

    def start_settings(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.check_button.clicked.connect(self.analyzer)
        self.ui.add_button.clicked.connect(self.add_to_table)
        self.ui.pushButton_2.clicked.connect(self.delete)
        self.item = Item
        self.ui.error_label_1.hide()
        self.ui.error_label_2.hide()
        self.ui.progressBar.hide()
        self.ui.load1.hide()
        self.ui.progressBar.setMinimum(0)
        self.ui.progressBar.setMinimum(10)
        self.ui.progressBar.setRange(0, 10)

    def __init__(self, parent=None):
        super(GUI_controller, self).__init__(parent)
        self.start_settings()
        self.start_settings()
        self.fill_workers_from_file()

    def fill_workers_from_file(self):
        self.count_of_workers = 0
        # считаем из файла сотрудников
        with open(f'Список_сотрудников.txt', 'r+') as file:
            self.lines: list[str] = file.readlines()
            self.lines = [x.rstrip() for x in self.lines]
        for name in self.lines:
            self.fill_workers_combobox(name)

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


    def analyzer(self):
        # Number analyzer
        start_time = datetime.datetime.now()
        analyzer = Numbers_analyzer()
        if self.ui.input_label.toPlainText() == '' or self.ui.input_label.toPlainText() == '\n':
            self.ui.input_label.setText('Обязательное поле')
            self.ui.input_label.setStyleSheet("color: rgb(255, 0, 0)")
        else:
            self.item = analyzer.analyzer(self.ui.input_label.toPlainText())
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
            print_to_backup_file(self.item)
            self.ui.progressBar.setValue(6)
            # self.debug_print()
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

    def fill_workers_combobox(self, name):
        self.ui.comboBox.addItem("")
        self.ui.comboBox.setItemText(self.count_of_workers, QCoreApplication.translate("MainWindow", f"{name}\n", None))
        self.count_of_workers += 1

    def add_workers_to_txt(self, name):
        "Не используемый метод"
        with open(f'Список_сотрудников.txt', 'a') as file:
            file.write(f'{name}\n')


def Controller():
    app = QApplication()
    window = GUI_controller()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    Controller()
