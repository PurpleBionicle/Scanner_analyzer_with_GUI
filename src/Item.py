import datetime


class Item:
    """
    Класс для оборудования. Имеет один метод - __str__ для печати
    Класс содержит:
    1) line - отсканированную строку
    2) item - какое это оборудование. Узнается после анализа
    3) serial - серийный номер. Узнается после анализа
    4) name - имя сотрудника, который вносит это в базу
    5) region - с какого региона оборудование (варианты: 'Центр','СВ','ЮВ','СЗ')
    6) working - в рабочем ли состоянии (варианты: 'ИСправно','Не исправно')
    7) station - тип станции
    8) taking - состояние (варианты: 'Сдаю','Беру')
    """

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
