from tkinter import Tk


# Наследование от Tk
class MainWindow(Tk):

    def __init__(self):
        Tk.__init__(self)

        # Настройка главного окна
        # Создание элементов формы

        self.mainloop()

    # Описание обработчиков событий