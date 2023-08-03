from src.Item import *


def print_to_backup_file(items: Item):
    """
    Общая информация записывается в гугл-таблицу
    Но также создается локальная резервная копия
    :param items: оборудование, которое будет записано
    :return: Ничего, результатом является измененный файл резервной копии
    """
    name = f'резервная_копия.txt'
    with open(name, 'a',encoding='utf-8') as file:
        # file.write(f'Номер | Время | Сотрудник |'
        # f' Название оборудования | Серийный номер | Отсканированная строка |\n')
        file.write('* |' + str(items))
        file.write('\n')

if __name__=='__main__':
    print_to_backup_file(Item('1','1','1','1'))