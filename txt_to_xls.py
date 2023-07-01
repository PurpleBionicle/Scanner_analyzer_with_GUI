import pandas as pd
import os


def from_txt_to_xls(file_name, sep='|', del_txt=False) -> None:
    """
    :param file_name: name txt file with .txt
    :param sep: separator with which the file will be divided into cells
    :param del_txt: after working delete (True) or not (False) txt file
    :return: None
    """
    records: list[list[str]] = []
    params: list[str] = []
    with open(file_name) as file:
        line: str = file.readline()
        params = line.split(sep)[:-1]
        while line != '':
            line: str = file.readline()
            records.append(list(line.split(sep)[:-1]))

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
            print(
                'Проблема соотнесения полей и значений (возможно их разное количество из-за разного числа разделителей')

    df = pd.DataFrame(result)
    df.to_excel(f'{file_name[:-4]}.xlsx', index=False)

    if del_txt:
        if os.path.isfile(file_name):
            os.remove(file_name)
        else:
            print(f'can not find file -{file_name}')


if __name__ == '__main__':
    from_txt_to_xls('резервная_копия.txt')