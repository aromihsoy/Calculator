import customtkinter as ctk
from logic import button_callback
from ui import create_ui


# Настройка внешнего вида (тема и цветовая схема)
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# Создание главного окна
app = ctk.CTk()
app.title("Base Calculator")
app.geometry("400x500")

# Запрещает изменение по ширине и высоте(растягивать окно)
app.resizable(False, False)


# Вызов функции, которая рисует кнопки
create_ui(app, button_callback)


# Запуск
app.mainloop()