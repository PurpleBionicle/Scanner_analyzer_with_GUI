import tkinter
from tkinter import ttk
import datetime


def consider_window():
    def __del_label():
        label.destroy()

    def __get_value_and_print_():
        global label
        value = input_space.get()
        label = tkinter.Label(consider_window, text=f'{value}', font=('Arial', 20, 'bold')).grid(row=4,column=0)
        names: list[str] = ['Беру', 'Сдаю']
        ttk.Combobox(consider_window, values=names, width=20, height=70, font=('Arial', 20, 'bold')).grid(row=4,column=1)
        tkinter.Button(consider_window, text='Удалить', width=20, height=3, background='red',
                       command=__del_label).grid(row=4, column=2)

    consider_window = tkinter.Tk()
    consider_window.geometry(f'1000x600+500+200')
    consider_window.title('Окно для считывания')
    label = tkinter.Label(consider_window, text=f'', font=('Arial', 20, 'bold'))
    consider_string = ''
    consider_window.grid_columnconfigure(0, weight=3)
    tkinter.Label(consider_window, text='Поместите курсор в поле ниже и начинайте сканирование',
                  font=('Arial', 20, 'bold')).grid(row=0,column=0,sticky='we',columnspan=3)
    input_space = tkinter.Entry(consider_window, width=20)
    input_space.grid(row=1,column=0,columnspan=3)
    tkinter.Button(consider_window, text='Добавить', width=40, height=5, background='green',
                   command=__get_value_and_print_).grid(row=2,column=0,columnspan=3)

    tkinter.Label(consider_window, text='Результат:', font=('Arial', 20, 'bold')).grid(row=3,column=0,sticky='we',columnspan=3)
    consider_window.mainloop()


if __name__ == '__main__':
    consider_window()
