import random
from tkinter import Tk
from tkinter.ttk import Button, Label

window = Tk()
window.title("Главное окно")
window.geometry("300x200")


def  enter(сlick):
    button_no.place(x = random.randint(1,220) , y = random.randint(1,180))


label = Label(text='Довольны ли вы своей зарплатой????', font=("Segoe UI", 12))
button_yes = Button(text='Да')
button_no = Button(text='Нет')

button_yes.grid(row=2, column=1)
button_no.grid(row=2, column=2)
label.grid(row=1, column=1,  ipadx=20)


button_no.bind('<Enter>', enter)

window.mainloop()