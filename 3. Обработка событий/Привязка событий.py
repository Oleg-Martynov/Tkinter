from tkinter import Tk, CENTER
from tkinter.ttk import Button, Label

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

button = Button(text='OK')
button.pack(anchor=CENTER)

"""
    button['text'] - изменение текста компонента
    button.place() - установка местоположения кнопки
    button.winfo_x() - получение координаты компонента
"""


def button_enter(event):
    button['text'] = 'ENTERED'
    button.place(x=button.winfo_x() + 5)


"""
События для привязки
Activate: окно становится активным.
Deactivate: окно становится неактивным.
MouseWheel: прокрутка колеса мыши.
KeyPress: нажатие клавиши на клавиатуре.
KeyRelease: освобождение нажатой клавиши
ButtonPress: нажатие кнопки мыши.
ButtonRelease: освобождение кнопки мыши.
Motion: движение мыши.
Configure: изменение размера и положения виджета
Destroy: удаление виджета
FocusIn: получение фокуса
FocusOut: потеря фокуса.
Enter: указатель мыши вошел в пределы виджета.
Leave: указатель мыши покинул виджет.
"""

button.bind('<Enter>', button_enter)

window.mainloop()