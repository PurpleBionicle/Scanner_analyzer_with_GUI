import tkinter
from tkinter import ttk
import datetime


class Item:
    def __init__(self, item: str, serial: str, line: str):
        self.line: str = line
        self.item: str = item
        self.serial: str = serial
        self.name: str = '***REMOVED***'

    def __str__(self):
        now = datetime.datetime.now()
        return f'{now.strftime("%d-%m-%Y %H:%M")} | {self.name} | {self.item} | {self.serial} | {self.line} |'


class Numbers_analyzer:
    def __init__(self):
        self.name: str = ''
        self.lines: list[str] = []
        self.items: list[Item] = []

    def openGUI(self):
        # self.lines # TODO fill this
        gui = GUI()

    def analyzer(self) -> None:
        def __get_serial_number(line: str) -> str:
            # serial_number_index: int = name[::-1].find('S')
            serial_number_index: int = 10
            return line[-serial_number_index:] if line[-11] == 'S' else 'нет S в конце'

        def __get_name(line: str) -> str:

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
                              'KDV127620/11': 'Цифровой модуль Baseband 6620',
                              'KDV127621/11': 'Цифровой модуль Baseband 6630',
                              'KDU127174/3': 'Цифровой модуль DUW 31 01',
                              # Цифровой модуль DUS 31 01 или
                              'KDU137624/31': 'Цифровой модуль DUS 31 02',
                              'KDU137624/31/5': 'Цифровой модуль DUS 31 02 5MHz',
                              'KDU137624/11': 'Цифровой модуль DUS 41 02',
                              'ER-KDU137739/1': 'Транспортный модуль TCU-02 01',
                              # Цифровой модуль DUW 20
                              'KDU127161/2': 'Цифровой модуль DUW 20 01'}
            serial_numbers: list[str] = ['KRC161549/1',
                                         'KRC161428/1',
                                         'KRC161622/1',
                                         'KRC161495/1',
                                         'KRC161945/1',
                                         'KRC161706/1',
                                         'KRC118070/1',
                                         'KRC11876/1',
                                         'KRC11876/1',
                                         'KRC161255/2',
                                         'KRC11891/2',
                                         'KRC161253/1',
                                         'KRC161253/1',
                                         'KRC161605/1',
                                         'KDV127620/11',
                                         'KDV127621/11',
                                         'KDU127174/3',
                                         'KDU137624/31',
                                         'KDU137624/31/5',
                                         'KDU137624/11',
                                         'KDU127161/2',
                                         'KDU127161/2',
                                         'KDU127174/3']
            correct_number: str = ''
            for number in serial_numbers:
                if number in line:
                    correct_number = number
                    break

            name = variants[correct_number] if correct_number != '' else ''
            return name

        for line in self.lines:
            item: str = __get_name(line)
            serial: str = __get_serial_number(line)
            self.items.append(Item(item, serial, line))

    def print_to_file(self):
        with open('../Результат_инвентаризации.txt', 'w') as file:
            file.write(
                f'Номер | Время | Сотрудник |'
                f' Название оборудования | Серийный номер | Отсканированная строка |\n')
            for i in range(len(self.items)):
                if len(self.items[i].line) >= 10:
                    file.write(f'{i + 1} | ')
                    file.write(str(self.items[i]))
                    file.write('\n')


class GUI:
    def __open_main(self):
        self.consider_window.destroy()
        self.__main_window()

    def __consider_window(self):
        def __get_value_and_print_():
            value = input_space.get()
            tkinter.Label(self.consider_window, text=f'{value}', font=('Arial', 20, 'bold')).pack()

        self.consider_window = tkinter.Tk()
        self.consider_window.geometry(f'1000x600+500+200')
        self.consider_window.title('Окно для считывания')

        self.consider_string = ''
        tkinter.Label(self.consider_window, text='Поместите курсор в поле ниже и начинайте сканирование',
                      font=('Arial', 20, 'bold')).pack()
        input_space = tkinter.Entry(self.consider_window, width=40,)
        input_space.pack()
        tkinter.Button(self.consider_window, text='Добавить', width=40, height=5, background='green',
                       command=__get_value_and_print_).pack()

        tkinter.Label(self.consider_window, text='Результат:', font=('Arial', 20, 'bold')).pack()
        tkinter.Button(self.consider_window, text='Вернуться к главному окну', width=40, height=5, background='grey',
                       command=self.__open_main).pack()
        self.consider_window.mainloop()

    def __close_main_window_and_open_consider(self):
        self.window.destroy()
        self.__consider_window()

    def __main_window(self):
        self.window = tkinter.Tk()
        self.window.geometry(f'1000x600+500+200')
        self.window.title('Учет оборудования')

        tkinter.Label(self.window, text='Выберете регион:', font=('Arial', 20, 'bold')).pack()
        region_result = tkinter.IntVar()
        tkinter.Radiobutton(self.window, text='Центр', variable=region_result, value=1, width=20, height=2,
                            font=('Arial', 20, 'bold')).pack()
        tkinter.Radiobutton(self.window, text='Северо-Восток', variable=region_result, value=2, width=20,
                            height=2,
                            font=('Arial', 20, 'bold')).pack()
        tkinter.Radiobutton(self.window, text='Юго-Восток', variable=region_result, value=3, width=20,
                            height=2,
                            font=('Arial', 20, 'bold')).pack()

        tkinter.Label(self.window, text='Выберете сотрудника из выпадающего списка:', font=('Arial', 20, 'bold'),
                      height=1).pack()
        names: list[str] = ['Гадршин Реваль Ревович', 'Голикова Элина Михайловна']
        ttk.Combobox(self.window, values=names, width=30, height=70, font=('Arial', 20, 'bold')).pack()

        # статус беру сдаю
        tkinter.Label(self.window, text='Выберете статус:', font=('Arial', 20, 'bold'),
                      height=2).pack()
        status = tkinter.IntVar()
        tkinter.Radiobutton(self.window, text='Сдаю', variable=status, value=2, width=20, height=2,
                            font=('Arial', 20, 'bold')).pack()
        tkinter.Radiobutton(self.window, text='Беру', variable=status, value=3, width=20, height=2,
                            font=('Arial', 20, 'bold')).pack()
        tkinter.Button(self.window, text='Перейти к считыванию', width=40, height=5, background='green',
                       command=self.__close_main_window_and_open_consider).pack()

        self.window.mainloop()

    def __init__(self):
        self.consider_string = ''
        self.__main_window()


# f'{now.strftime("%d-%m-%Y %H:%M")} | Регион | Сотрудник |Статус | Название оборудования | Серийный номер | Отсканированная строка |')


def main():
    # gui = GUI()
    analyzer = Numbers_analyzer()
    analyzer.openGUI()
    # analyzer.work_with_file()
    analyzer.analyzer()
    analyzer.print_to_file()


if __name__ == '__main__':
    main()


#             # # получение всех страниц документа
#         # for sheet in vals['sheets']:
#         #     pprint(sheet['properties']['title'])
