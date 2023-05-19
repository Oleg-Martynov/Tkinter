from tkinter import Tk, Checkbutton, IntVar, StringVar
from tkinter.messagebox import showinfo

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

# Переменные для хранения значений checkbutton-ов
v1 = IntVar()
v2 = IntVar()

# Дополнительная возможность изменять метку checkbutton-а
on = 'Включено'
off = 'Отключено'
switcher = StringVar(value=on)

def checkbutton_changed():
    if v1.get() == 1:
        # Вывод служебного сообщения
        showinfo(title='Информация', message='Пункт 1 - TRUE')
    if v2.get() == 1:
        showinfo(title='Информация', message='Пункт 2 - TRUE')
    if v1.get() == 0:
        showinfo(title='Информация', message='Пункт 1 - FALSE')
    if v2.get() == 0:
        showinfo(title='Информация', message='Пункт 2 - FALSE')

# Привязка события и переменной к checkbutton
check1 = Checkbutton(text='Пункт 1', variable=v1, command=checkbutton_changed)
check2 = Checkbutton(text='Пункт 2', variable=v2, command=checkbutton_changed)
check3 = Checkbutton(text='Выключено', textvariable=switcher, variable=switcher, offvalue=off, onvalue=on)
check1.pack()
check2.pack()
check3.pack()

window.mainloop()
