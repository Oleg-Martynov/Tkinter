from tkinter import Tk

# Класс окна
window = Tk()
# Установка заголовка окна
window.title("Главное окно")
# Установка размеров окна
window.geometry("300x200")
# Возможность изменять размеры окна (по ширине, по высоте)
# window.resizable(False, False)

# Запуск окна
window.mainloop()