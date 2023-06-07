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
#from tkinter import Tk, Checkbutton, IntVar, StringVar
from tkinter.messagebox import showinfo
#from tkinter.ttk import Entry,Label
from tkinter import *
window = Tk()
window.title("Главное окно")
window.geometry("300x200")

entry = Entry()
entry2 = Entry()
v1 = IntVar()
v2 = IntVar()
v3 = IntVar()
v4 = IntVar()


# Дополнительная возможность изменять метку checkbutton-а
on = 'Включено'
off = 'Отключено'
switcher = StringVar(value=on)

def checkbutton_changed():
    save_entry = entry.get()
    save_entry2 = ""
    if v1.get() == 1:
        save_entry = save_entry.upper()
        text.delete('1.0', END)
        text.insert(1.0,f'{save_entry}')
    if v2.get() == 1:
        for i in save_entry:
            if i == " ":
                save_entry2 = save_entry2 + i +  " "
            else:
                save_entry2 = save_entry2 + i
        text.delete('1.0', END)
        text.insert(1.0,f'{save_entry2}')

    if v3.get() == 1:
        save_entry = ''.join(reversed(save_entry))
        text.delete('1.0', END)
        text.insert(1.0,f'{save_entry}')
    if v4.get() == 1:
        save_entry3 = entry2.get()
        start_value=save_entry.find(save_entry3)
        end_value = start_value+ len(save_entry3)
        save_entry4 = save_entry[:start_value] + save_entry[end_value:]
        text.delete('1.0', END)
        text.insert(1.0,f'{save_entry4}')
# Привязка события и переменной к checkbutton
check1 = Checkbutton(text='Все слова с большой буквы', variable=v1,command=checkbutton_changed)
check2 = Checkbutton(text='Увеличить пробелы между словами', variable=v2,command=checkbutton_changed)
check3 = Checkbutton(text='Развернуть строку', variable=v3,command=checkbutton_changed)
check4 = Checkbutton(text='Удалить все значения', variable=v4,command=checkbutton_changed)
text = Text(width=20, height=1, fg='black', wrap=WORD)

entry.grid(row=0, column=0, sticky='W')
check1.grid(row=2, column=0, sticky='W')
check2.grid(row=3, column=0, sticky='W')
check3.grid(row=4, column=0, sticky='W')
check4.grid(row=5, column=0, sticky='W')
entry2.grid(row=5, column=1)
text.grid(row=6,column=0,sticky='W')


window.mainloop()

