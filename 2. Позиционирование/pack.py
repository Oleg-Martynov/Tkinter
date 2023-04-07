from tkinter import Tk, BOTH
from tkinter.ttk import Button

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

button1 = Button(text='OK')
"""
    Свойства:
    expand - если True, то элемент заполняет всё пространство контейнера
    fill - растягивание компонента по горизонтали (X), вертикали (Y) или во всех направлениях (BOTH)
    anchor - перемещение компонента в определённую позицию контейнера (n, e, s, w, ne, nw, se, sw, c)
    side - выравнивает виджет по одной из сторон контейнера: TOP (по умолчанию, верхней стороне), 
    BOTTOM (нижней стороне), LEFT (левой стороне), RIGHT (правой стороне)
    ipadx, ipady - внутренние отступы по горизонтали и вертикали
    padx, pady - внешние отступы по горизонтали и вертикали. Можно задавать массивом [верх, низ], [лево, право]
"""
button1.pack(fill=BOTH)

window.mainloop()