# Функция для кнопки
def button_callback(char, entry):
    entry.insert("end", char)


# Функция для того чтоб стереть весь текст
def clear_entry(entry):
    entry.delete(0, "end")


# Функция равно
def calculate(entry):
    result = entry.get()

    result = result.replace("×", "*").replace("÷", "/").replace("−", "-")

    try:
        result = eval(result)

        entry.delete(0, "end")

        entry.insert("end", result)

    except ZeroDivisionError:
        entry.delete(0, "end")
        entry.insert("end", "Division by zero")

    except SyntaxError:
        entry.delete(0, "end")
        entry.insert("end", "NaN")

    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Error")


# Функция для корня
def square_func(entry):
    result = entry.get()

    try:
        result = eval(result)
        result = result ** 0.5
        entry.delete(0, "end")
        entry.insert("end", result)
    except Exception:
        entry.delete(0, "end")
        entry.insert("end", "Error")