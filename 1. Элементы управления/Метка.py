from tkinter import Tk
from tkinter.ttk import Button, Label

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

label = Label(text='Текст метки', font=("Segoe UI", 14))
label.pack()

window.mainloop()