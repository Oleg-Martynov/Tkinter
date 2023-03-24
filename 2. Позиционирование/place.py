from tkinter import Tk
from tkinter.ttk import Entry

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

entry = Entry()
"""
    Place - фиксированное расположение элемента
    x, y - расположение элемента
    height, width - высота, ширина элемента
    anchor - растяжение элемента (n, e, s, w, ne, nw, se, sw, c)
    North(север - вверх), South (юг - низ), East (восток - правая сторона), West (запад - левая сторона) и Center (по центру)
"""
entry.place(x=50, y=50)

window.mainloop()
