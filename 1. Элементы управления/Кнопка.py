from tkinter import Tk
from tkinter.ttk import Button

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

# Создание кнопки в окне
button = Button(text='OK')
# Позиционирование элемента (установка места расположения)
button.pack()

window.mainloop()