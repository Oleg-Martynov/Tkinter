"""
    TODO: Вводится строка в поле ввода.
          Ниже необходимо вывести модифицированную строку в текст боксе, чтобы можно было его копировать.
          Варианты модификации выбираются при помощи checkbutton-ов.
          1. Все слова с большой буквы
          2. Увеличить пробелы между словами
          3. Развернуть строку
          4. Удалить слова, короче значения (значение задаётся в поле ввода рядом с пунктом)
          Действия происходят сразу после выбора пункта. Все эффекты накладываются друг на друга.
          Желательно оформлять окно в ООП стиле.
"""
from tkinter import Tk, Checkbutton, IntVar, StringVar
from tkinter.messagebox import showinfo
from tkinter.ttk import Entry
window = Tk()
window.title("Главное окно")
window.geometry("300x200")

entry = Entry()

v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()
# Дополнительная возможность изменять метку checkbutton-а
on = 'Включено'
off = 'Отключено'
switcher = StringVar(value=on)


# Привязка события и переменной к checkbutton
check1 = Checkbutton(text='Все слова с большой буквы', variable=v1)
check2 = Checkbutton(text='Увеличить пробелы между словами', variable=v2)
check3 = Checkbutton(text='Развернуть строку', variable=v3)
check4 = Checkbutton(text='Удалить все значения', variable=v4)

entry.pack()
check1.pack()
check2.pack()
check3.pack()
check4.pack()

window.mainloop()

