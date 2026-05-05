import customtkinter as ctk
from logic import clear_entry, calculate, square_func


# Функция создания кнопок
def create_ui(app, button_callback):
    # Центрируем кнопки
    app.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
    app.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

    entry = ctk.CTkEntry(app, placeholder_text="0", font=("Arial", 40), height=60, takefocus=False)
    # Растягиваем на все 5 колонок, чтобы он был сверху над кнопками
    entry.grid(row=0, column=0, columnspan=5, padx=20, pady=20, sticky="nsew")


    # Кнопки цифры
    button_number_1 = ctk.CTkButton(app, text="1",  font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000", width=60, height=40, command = lambda: button_callback("1", entry))
    button_number_2 = ctk.CTkButton(app, text="2", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000", width=60, height=40, command = lambda: button_callback("2", entry))
    button_number_3 = ctk.CTkButton(app, text="3", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000", width=60, height=40, command = lambda: button_callback("3", entry))
    button_number_4 = ctk.CTkButton(app, text="4", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000", width=60, height=40, command = lambda: button_callback("4", entry))
    button_number_5 = ctk.CTkButton(app, text="5", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000", width=60, height=40, command = lambda: button_callback("5", entry))
    button_number_6 = ctk.CTkButton(app, text="6", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000", width=60, height=40, command = lambda: button_callback("6", entry))
    button_number_7 = ctk.CTkButton(app, text="7", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000", width=60, height=40, command = lambda: button_callback("7", entry))
    button_number_8 = ctk.CTkButton(app, text="8", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000", width=60, height=40, command = lambda: button_callback("8", entry))
    button_number_9 = ctk.CTkButton(app, text="9", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000", width=60, height=40, command = lambda: button_callback("9", entry))
    button_number_0 = ctk.CTkButton(app, text="0", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000",  width=60, height=40, command = lambda: button_callback("0", entry))
    button_number_0 = ctk.CTkButton(app, text="0", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000",  width=60, height=40, command = lambda: button_callback("0", entry))
    button_number_0 = ctk.CTkButton(app, text="0", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000",  width=60, height=40, command = lambda: button_callback("0", entry))
    #Кнопки для скобок (open / close)
    button_bracket_open = ctk.CTkButton(app, text="(", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000",  width=60, height=40, command = lambda: button_callback("(", entry))
    button_bracket_close = ctk.CTkButton(app, text=")", font=("Arial", 30), fg_color="#FFFFFF", hover_color="#E5E5E5", text_color="#000000",  width=60, height=40, command = lambda: button_callback(")", entry))
    # Арифметические кнопки
    button_plus = ctk.CTkButton(app, text="+", font=("Arial", 30), fg_color="#1976D2", hover_color="#1565C0", width=60, height=40, command = lambda: button_callback("+", entry))
    button_minus = ctk.CTkButton(app, text="–", font=("Arial", 30), fg_color="#1976D2", hover_color="#1565C0", width=60, height=40, command = lambda: button_callback("–", entry))
    button_multiply = ctk. CTkButton(app, text="×", font=("Arial", 30), fg_color="#1976D2", hover_color="#1565C0", width=60, height=40, command = lambda: button_callback("×", entry))
    button_divide = ctk.CTkButton(app, text="÷", font=("Arial", 30), fg_color="#1976D2", hover_color="#1565C0", width=60, height=40, command = lambda: button_callback("÷", entry))
    # Корень числа
    button_square = ctk.CTkButton(app, text="√", font=("Arial", 30), fg_color="#1976D2", hover_color="#1565C0", width=60, height=40, command = lambda: square_func(entry))
    # Кнопка удаления
    button_delete = ctk.CTkButton(app, text="C", font=("Arial", 30), fg_color="#E74C3C", hover_color="#C0392B", width=60, height=40, command = lambda: clear_entry(entry))
    # Кнопка равно
    button_equal = ctk.CTkButton(app, text="=", font=("Arial", 30), fg_color="#2ecc71", hover_color="#27ae60", width=60, height=40, command = lambda: calculate(entry))


    # Расставим их в сетке с помощью grid()
    button_number_1.grid(row=3, column=0, padx=(20, 5), pady=5, sticky="nsew")
    button_number_2.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")
    button_number_3.grid(row=3, column=2, padx=5, pady=5, sticky="nsew")
    button_number_4.grid(row=2, column=0, padx=(20, 5), pady=5, sticky="nsew")
    button_number_5.grid(row=2, column=1, padx=5, pady=5, sticky="nsew")
    button_number_6.grid(row=2, column=2, padx=5, pady=5, sticky="nsew")
    button_number_7.grid(row=1, column=0, padx=(20, 5), pady=5, sticky="nsew")
    button_number_8.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
    button_number_9.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
    button_number_0.grid(row=4, column=0, padx=(20, 5), pady=(5, 20), sticky="nsew")

    button_bracket_open.grid(row=4, column=1, padx=5, pady=(5, 20), sticky="nsew")
    button_bracket_close.grid(row=4, column=2, padx=5, pady=(5, 20), sticky="nsew")

    button_plus.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")
    button_minus.grid(row=3, column=4, padx=(5, 20), pady=5, sticky="nsew")
    button_multiply.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")
    button_divide.grid(row=2, column=4, padx=(5, 20), pady=5, sticky="nsew")
    button_square.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

    button_delete.grid(row=1, column=4, padx=(5, 20), pady=5, sticky="nsew")

    button_equal.grid(row=4, column=4, padx=(5, 20), pady=(5, 20), sticky="nsew")