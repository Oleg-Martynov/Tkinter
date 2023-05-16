from tkinter import Tk, messagebox
from tkinter.messagebox import askyesno
from tkinter.ttk import Button

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

"""
    Вывод служебных сообщений
    Об ошибке
        showerror
    Предупреждение
        showwarning
    Информации
        showinfo
        
    Вывод окон с подтверждением
        askyesno
        askokcancel
        askretrycancel
"""


def on_button_click():
    messagebox.showinfo("Заголовок", "Сообщение")


def on_button_close_click():
    result = askyesno(title='Подтвердите закрытие', message='Вы уверены, что хотите закрыть приложение?')
    if result:
        window.destroy()


button = Button(text='OK', command=on_button_click)
button.pack()

button_close = Button(text='Закрыть', command=on_button_close_click)
button_close.pack()

window.mainloop()