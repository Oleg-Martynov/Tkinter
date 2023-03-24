from tkinter import Tk
from tkinter.ttk import Entry

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

entry = Entry()
entry.pack()

window.mainloop()