import tkinter as tk
from tkinter import ttk
import math

def tabulate_function(start, end, step):
    results = []
    for x in range(int(start * 100), int((end + step) * 100), int(step * 100)):
        x /= 100
        y = math.cos(2 * x + 1)
        results.append((f'{x:.2f}', f'{y:.4f}'))
    return results

def tabulate_and_update_listbox(start, end, step, listbox, progressbar):
    listbox.delete(0, tk.END)  # Очистка содержимого Listbox
    total_steps = int((end - start) / step) + 1
    progressbar["maximum"] = total_steps

    for i, (x, y) in enumerate(tabulate_function(start, end, step), 1):
        listbox.insert(tk.END, f'x = {x}, y = {y}')
        progressbar["value"] = i
        listbox.update()
        progressbar.update()

def main():
    window = tk.Tk()
    window.title("Tabulate Function")

    start_value = 0.01
    end_value = 0.9
    step_value = 0.01

    listbox = tk.Listbox(window, width=30, height=15)
    listbox.pack(pady=10)

    progressbar = ttk.Progressbar(window, length=300, mode="determinate")
    progressbar.pack(pady=10)

    tabulate_button = tk.Button(window, text="Tabulate Function",
                                command=lambda: tabulate_and_update_listbox(start_value, end_value, step_value, listbox, progressbar))
    tabulate_button.pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    main()
