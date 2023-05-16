from tkinter import Tk
from tkinter.ttk import Button

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

button1 = Button(text='Кнопка 1')
button2 = Button(text='Кнопка 2')
button3 = Button(text='Кнопка 3')
button4 = Button(text='Кнопка 4')
"""
    Grid - расположение элементов в невидимой сетке
    column - номер столбца (с нуля)
    row - номер строки (с нуля)
    columnspan - число столбцов, занимаемых элементом (объединение столбцов)
    rowspan - число строк, занимаемых элементом (объединение строк)
    ipadx, ipady - внутренние отступы по горизонтали и вертикали
    padx, pady - внешние отступы по горизонтали и вертикали. Можно задавать массивом [верх, низ], [лево, право]
    sticky - расположение элемента внутри ячейки (n, e, s, w, ne, nw, se, sw)
    North(север - вверх), South (юг - низ), East (восток - правая сторона), West (запад - левая сторона)
"""
button1.grid(row=0, column=0, columnspan=2, ipadx=40, pady=[0, 10])
button2.grid(row=0, column=3, pady=[0, 10])
button3.grid(row=1, column=0, pady=[0, 10])
button4.grid(row=1, column=1, pady=[0, 10])

window.mainloop()