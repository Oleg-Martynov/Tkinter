from tkinter import Tk
from tkinter.ttk import Button, Label

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

# TODO: Показать, почему классом создавать форму лучше

value = 0

label_result = Label(text='0', font=("Segoe UI", 24))


def inc_button_click():
    global value
    value += 1
    label_result.config(text=f'{value}')


def dec_button_click():
    global value
    value -= 1
    label_result.config(text=f'{value}')

"""
    command - привязывает событие в виде имени функции
"""
inc_button = Button(text='+', command=inc_button_click)
dec_button = Button(text='-', command=dec_button_click)
inc_button.pack()
dec_button.pack()
label_result.pack()

window.mainloop()
