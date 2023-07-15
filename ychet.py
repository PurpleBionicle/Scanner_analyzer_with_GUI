# -*- coding: utf-8 -*-
import sys

from src import GUI, print_methods, Google_sheets,Barcode
from src.Item import *

from langdetect import detect

from PySide6.QtCore import (QCoreApplication)
from PySide6.QtWidgets import (QApplication, QMainWindow)


class GUI_controller(QMainWindow):
    """
    Контроллер для управления интерфейсом, который в свою очередь зависит от всех остальных файлов.
    """

    def start_settings(self):
        """
        Вызывается при инициализации.
        Задает связи кнопок и их методов, а также, что должно изначально быть спрятано
        """
        self.ui = GUI.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.check_button.clicked.connect(self.analyzer)
        self.ui.add_button.clicked.connect(self.__add_to_table)
        self.ui.pushButton_2.clicked.connect(self.__delete)
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
        "Поскольку инициализация поля сотрудников гибкая и задается из файла, то ее инициализация отложена" \
        "Так, вначале создается окно и лишь потом заполняется combobox сотрудников"
        self.__fill_workers_from_file()

    def __fill_workers_from_file(self):
        """
        Считываем из файла и заполняем окно интерфейса,
        число сотрудников необходимо подсчитывать для присвоения номера в окне
        """
        self.count_of_workers = 0
        with open(f'Список_сотрудников.txt', 'r+') as file:
            self.lines: list[str] = file.readlines()
            self.lines = [x.rstrip() for x in self.lines]
        for name in self.lines:
            self.__fill_workers_combobox(name)

    def __check_language(self):
        """
        Функция проверки языка одного окна в интерфейсе, он обязательно должен быть английским
        Однако используемая библиотека иногда считает, что введенные наименования не англ.
        А другие языки (поскольку это не реальные слова, а сокращенные наименования)
        Поэтому практическим путем были найдены основные определяемые языки
        """
        # while detect(self.ui.station.toPlainText()) !='eng':
        error = ["bg", "mk", "uk"]
        if self.ui.station.toPlainText() is not None and self.ui.station.toPlainText() != '' and detect(
                self.ui.station.toPlainText()) in error:
            print(detect(self.ui.station.toPlainText()))
            "В случае ошибки вывод соответсвующее сообщение"
            self.ui.error_label_1.show()
            self.ui.error_label_2.show()
            return False
        return True

    def analyzer(self):
        """
        Основная функция класса, которая сопоставляет отсканированную строку с реальным именем оборудования
        """
        # Number analyzer
        start_time = datetime.datetime.now()
        analyzer = Barcode.Analyzer()
        if self.ui.input_label.toPlainText() == '' or self.ui.input_label.toPlainText() == '\n':
            self.ui.input_label.setText('Обязательное поле')
            self.ui.input_label.setStyleSheet("color: rgb(255, 0, 0)")
        else:
            "Поиск среди известных"
            self.item = analyzer.analyze(self.ui.input_label.toPlainText())
            self.ui.result_label.setText(self.item.item) if self.item.item else self.ui.result_label.setText(
                'Вероятно этого оборудования нет в базе')
            self.ui.result_label_2.setText(self.item.serial)
        print('analyze ', datetime.datetime.now() - start_time)

    def __delete(self):
        """
        Очищает все формы - кнопка "Удалить"
        """
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.input_label.clear()
        self.ui.result_label.clear()
        self.ui.result_label_2.clear()
        self.ui.station.clear()

    def __debug_print(self):
        """
        Неиспользуемый метод для отладки
        """
        print(f'name - {self.item.name}')
        print(f'item - {self.item.item}')
        print(f'region - {self.item.region}')
        print(f'working - {self.item.working}')
        print(f'taking - {self.item.taking}')
        print(f'station - {self.item.station}')

    def __add_to_table(self):
        """
        Метод занесения объекта в гугл таблицу
        """
        start_time = datetime.datetime.now()
        self.ui.error_label_1.hide()
        self.ui.error_label_2.hide()
        self.ui.load1.hide()

        flag = True
        "Проверка полей на обязательное заполнение"
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

        "Если все поля заполнены и на правильном языке"
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
            print_methods.print_to_backup_file(self.item)
            self.ui.progressBar.setValue(6)

            # self.__debug_print()
            self.ui.load1.setText('подключение к таблице')
            "Получение объекта таблицы"
            controller = Google_sheets.Google_sheets()
            self.ui.progressBar.setValue(7)

            now = datetime.datetime.now()
            params = [f'{now.strftime("%d-%m-%Y %H:%M")}', self.item.name, self.item.station,
                      self.item.taking, self.item.item, self.item.serial, self.item.working, self.item.line]
            pages = ['Центр', 'СВ', 'ЮВ', 'СЗ']
            self.ui.load1.setText('получение страницы')
            self.ui.progressBar.setValue(8)

            "Нахождение нужной страницы"
            input_page = self.item.region
            page = ''
            for p in pages:
                if p in input_page or input_page in p:
                    page = p
                    break
            if page == '':
                page = 'Центр'
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

    def __fill_workers_combobox(self, name):
        """
        Пообъектное заполнение интерфейсной формы
        """
        self.ui.comboBox.addItem("")
        self.ui.comboBox.setItemText(self.count_of_workers, QCoreApplication.translate("MainWindow", f"{name}\n", None))
        self.count_of_workers += 1

    def add_workers_to_txt(self, name):
        "Не используемый метод"
        with open(f'Список_сотрудников.txt', 'a') as file:
            file.write(f'{name}\n')


def Controller():
    """
    Главный контроллер, создает окно интерфейса
    """
    app = QApplication()
    window = GUI_controller()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    'Основная точка входа в программу для версии с интерфейсом'
    Controller()
