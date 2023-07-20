from src.Item import Item


class Analyzer:
    def __init__(self):
        self.name: str = ''
        self.lines: list[str] = []
        self.items: list[Item] = []
        self.file_name: str = 'Результат_инвентаризации.txt'

    def analyze(self, line) -> Item:
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
        line = self.change_layout(line)
        if line.count(',') > 0 and (line.find('TRP') != -1 or line.find('NWA') != -1) and line.find('MDP') == -1:
            return self.__TRP_analyzer(line, name)
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
            return Item(item, serial, line, name)

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

    def __TRP_analyzer(self, line: str, name) -> Item:
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
        return Item(name=name, serial=serial, line=line, item=item)

    def __fill_variants_and_IDs(self):
        "Заполним варианты в виде словаря(сокращение):предмет"
        variants: dict = {}
        IDs = []
        with open(f'Список_оборудования.txt', 'r+',encoding='utf-8') as file:
            lines: list[str] = file.readlines()
            lines = [x.rstrip() for x in lines]
        for line in lines:
            params = line.split(':')
            variants[params[0]] = params[1]
            IDs.append(params[0])

        return variants, IDs

    def change_layout(self, line):
        """
        :param line: прочитанная строка
        :return: та же строка, но перевод на англ. раскладку
        """
        layout = dict(zip(map(ord, "йцукенгшщзхъфывапролджэячсмитьбю.ё"
                                   'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ,Ё'),
                          "qwertyuiop[]asdfghjkl;'zxcvbnm,./`"
                          'QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>?~'))
        return line.translate(layout)

