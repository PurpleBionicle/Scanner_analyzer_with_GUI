import pandas as pd
import datetime
import secret


class Item:
    """
    Укороченная версия - см. описание в файле Item
    """

    def __init__(self, item: str, serial: str, line: str):
        self.line: str = line
        self.item: str = item
        self.serial: str = serial
        self.name: str = secret.name

    def __str__(self):
        now = datetime.datetime.now()
        return f'{now.strftime("%d-%m-%Y %H:%M")} | {self.name} | {self.item} | {self.serial} | {self.line} |'


class Numbers_analyzer:
    def __init__(self):
        self.name: str = ''
        self.lines: list[str] = []
        self.items: list[Item] = []
        self.file_name: str = 'Результат_инвентаризации.txt'

    def work_with_file(self) -> None:
        with open(f'Сканы.txt', 'r+') as file:
            self.lines: list[str] = file.readlines()
            self.lines = [x.rstrip() for x in self.lines]
            self.lines = [x.replace(' ', '') for x in self.lines]

    def analyzer(self):
        """
        Главный метод - по поданной отсканированный строке делает анализ по заведенному оборудованию
        :param line: отсканированная строка
        :return: сопоставленное оборудование
        Все существует 3 семейства, к каждому из которых собственный подход
        1) TRP или NWA - сканируются с большим количеством запятых (как и MDP - оно вынесено в отдельный случай):
        TRP-*,*,*,*,*,Low
        Дальнейшее описание алгоритма в __TRP_analyzer
        2) остальное (не считая MDP): не имеет запятых (подробнее в __get_serial_number, __get_name)
        3) MDP - имя и серийный, как п.2, но серийный начинается с нулей (которые надо удалить), между 2 и 3 запятой
        """

        "Показан первый случае, если падаем в else - 2,3"
        name = ''
        for line in self.lines:
            if line.count(',') > 0 and (line.find('TRP') != -1 or line.find('NWA') != -1) and line.find(
                    'MDP') == -1:
                self.items.append(self.__TRP_analyzer(line))
            else:
                "п.2,3"
                line = line.rstrip()
                item: str = self.__get_name(line)
                serial: str = self.__get_serial_number(line)
                if line.find('MDP') != -1:
                    "п.3"
                    line_ = line.replace('\n', '').rstrip()
                    line_ = line_.replace(' ', '')
                    params = line_.split(',')
                    serial = params[2]
                    while serial[0] == '0':
                        serial = serial[1:]
                self.items.append(Item(item, serial, line))

    def __get_serial_number(self, line: str) -> str:
        """
        11 всегда 'S' после нее вырезаем номер
        :param line: отсканированная строка
        :return: полученный из нее серийный номер
        """
        # serial_number_index: int = name[::-1].find('S')
        serial_number_index: int = 10
        if len(line) >= 11:
            if line[-11] == 'S':
                return line[-serial_number_index:]
        return 'скорее всего прибор должен иметь серийный номер вида S******'

    def __get_name(self, line: str):
        """
        Читаем из файлов возможные варианты и находим нужный
        :param line: отсканированная строка
        :return: Возвращает сопоставленный предмет
        """
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

    def __fill_variants_and_IDs(self):
        "Заполним варианты в виде словаря(сокращение):предмет"
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

    def __TRP_analyzer(self, line: str) -> Item:
        def __fill_name():
            "Вырожденный случай"
            if line.find('MODEM-EA') != -1:
                return 'MODEM-EA'

            "Два варианты концовок - low/high"
            "Приведенные варианты имеют одинаковое начало, поэтому вынесены отдельно"
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
        "Удалим незначащие нули для серийного номера"
        while serial[0] == '0':
            serial = serial[1:]
        return Item(serial=serial, line=line, item=item)

    def print_to_file(self):
        with open(self.file_name, 'w') as file:
            file.write(
                f'Номер | Время | Сотрудник |'
                f' Название оборудования | Серийный номер | Отсканированная строка |\n')
            for i in range(len(self.items)):
                if len(self.items[i].line) >= 10:
                    file.write(f'{i + 1} | ')
                    file.write(str(self.items[i]))
                    file.write('\n')

        self.txt_to_xls()

    def txt_to_xls(self):
        records: list[list[str]] = []
        params: list[str] = []
        with open(self.file_name) as file:
            line: str = file.readline()
            params = line.split('|')[:-1]
            while line != '':
                line: str = file.readline()
                records.append(list(line.split('|')[:-1]))

        columns = [[] for _ in range(len(params))]

        for i in range(len(params)):
            for record in records:
                if len(record) <= 1:
                    records.remove(record)
                    continue
                columns[i].append(record[i])

        result = dict()
        for i in range(len(params)):
            try:
                result[params[i]] = columns[i]
            except:
                print('Проблема соотнесения полей и значений (возможно их разное количество из-за "|" в конце')

        df = pd.DataFrame(result)
        df.to_excel(f'{self.file_name[:-4]}.xlsx', index=False)


def main():
    analyzer = Numbers_analyzer()
    analyzer.work_with_file()
    analyzer.analyzer()
    analyzer.print_to_file()


if __name__ == '__main__':
    main()
