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

    def work_with_file(self) -> None:
        with open(f'Сканы.txt', 'r+') as file:
            self.lines: list[str] = file.readlines()
            self.lines = [x.rstrip() for x in self.lines]
            self.lines = [x.replace(' ', '') for x in self.lines]

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
        with open('Результат_инвентаризация.txt', 'w') as file:
            file.write(
                f'Номер | Время | Сотрудник |'
                f' Название оборудования | Серийный номер | Отсканированная строка |\n')
            for i in range(len(self.items)):
                if len(self.items[i].line) >= 10:
                    file.write(f'{i + 1} | ')
                    file.write(str(self.items[i]))
                    file.write('\n')


def main():
    analyzer = Numbers_analyzer()
    # analyzer.openGUI()
    analyzer.work_with_file()
    analyzer.analyzer()
    analyzer.print_to_file()


if __name__ == '__main__':
    main()
