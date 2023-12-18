import tkinter as tk

def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    total_amount = principal + interest
    return total_amount

def calculate_compound_interest(principal, rate, time):
    amount = principal * pow((1 + rate / 100), time)
    interest = amount - principal
    return amount

def on_button_click():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())

    if interest_type.get() == 1:
        result = calculate_simple_interest(principal, rate, time)
    else:
        result = calculate_compound_interest(principal, rate, time)

    result_label.config(text="Общая сумма: $" + str(result))

# Создаем окно
window = tk.Tk()
window.title("Калькулятор процентов")

# Создание ввода основной суммы
principal_label = tk.Label(window, text="Основная сумма:")
principal_label.pack()
principal_entry = tk.Entry(window)
principal_entry.pack()

# Создание ввода процентной ставки
rate_label = tk.Label(window, text="Процентная ставка:")
rate_label.pack()
rate_entry = tk.Entry(window)
rate_entry.pack()

# Создание ввода периода времени
time_label = tk.Label(window, text="Период времени (в днях):")
time_label.pack()
time_entry = tk.Entry(window)
time_entry.pack()

# Создание выбора типа процентов
interest_type = tk.IntVar()
simple_interest_button = tk.Radiobutton(window, text="Простые проценты ", variable=interest_type, value=1)
simple_interest_button.pack()
compound_interest_button = tk.Radiobutton(window, text="Сложные проценты ", variable=interest_type, value=2)
compound_interest_button.pack()

#Создание кнопки "Calculate"
calculate_button = tk.Button(window, text="Calculate", command=on_button_click)
calculate_button.pack()

# Создание вывода результата
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()