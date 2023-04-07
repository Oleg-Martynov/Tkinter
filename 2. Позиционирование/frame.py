from tkinter import Tk, BOTH, LEFT
from tkinter.ttk import Button, Entry, Label, Frame

window = Tk()
window.title("Главное окно")
window.geometry("300x200")

"""
   Frame - группирует элементы воедино
   К Frame стоит относиться как к отдельному окну.
"""

frame1 = Frame()
frame2 = Frame()
frame3 = Frame()
frame4 = Frame()
label1 = Label(frame1, text="L1")
label2 = Label(frame2, text="L2")
label3 = Label(frame3, text="L3")
label4 = Label(frame4, text="L4")
label1.pack(side=LEFT)
label2.pack(side=LEFT)
label3.pack(side=LEFT)
label4.pack(side=LEFT)
entry1 = Entry(frame1)
entry2 = Entry(frame2)
entry3 = Entry(frame3)
entry4 = Entry(frame4)
entry1.pack(side=LEFT)
entry2.pack(side=LEFT)
entry3.pack(side=LEFT)
entry4.pack(side=LEFT)
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=0)
frame4.grid(row=1, column=1)

window.mainloop()