import datetime
import pandas as pd


class Item:
    def __init__(self, item: str, serial: str, line: str):
        self.line: str = line
        self.item: str = item
        self.serial: str = serial
        self.name: str = 'Пушкин Илья Дмитриевич'

    def __str__(self):
        now = datetime.datetime.now()
        return f'{now.strftime("%d-%m-%Y %H:%M")} | {self.name} | {self.item} | {self.serial} | {self.line} |'




class Numbers_analyzer:
    def __init__(self):
        self.name: str = ''
        self.lines: list[str] = []
        self.items: list[Item] = []
        self.file_name: str = 'Результат_инвентаризация.txt'

    def work_with_file(self) -> None:
        with open(f'Сканы.txt', 'r+') as file:
            self.lines: list[str] = file.readlines()
            self.lines = [x.rstrip() for x in self.lines]
            self.lines = [x.replace(' ', '') for x in self.lines]

    def analyzer(self) -> Item:
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

        def __TRP_analyzer(line: str) -> Item:
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
            return Item( serial=serial, line=line, item=item)

        # if not special:
        if not 0:
            name = ''
            for line in self.lines:
                if line.count(',') > 0 and (line.find('TRP') != -1 or line.find('NWA') != -1) and line.find(
                    'MDP') == -1:
                    self.items.append(__TRP_analyzer(line))
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
                    self.items.append(Item(item, serial, line))

        else:
            pass
            # TODO add

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
