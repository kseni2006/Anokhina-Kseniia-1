import tkinter as tk
from tkinter import messagebox


def round_narrow(x, delta):
    return round(x, 2)


def round_broad(x, delta_percent):
    delta = delta_percent / 100
    x_rounded = round(x * (1 - delta), 2)
    return x_rounded


def task2():
    try:
        x = float(entry_x.get())
        rounding_choice = rounding_mode.get()

        if rounding_choice == 'narrow':
            delta = float(entry_delta.get())
            x_narrow = round_narrow(x, delta)
            result_task2.set(f"Округлене число (вузьке) = {x_narrow}")
        elif rounding_choice == 'broad':
            delta_percent = float(entry_delta_percent.get())
            x_broad = round_broad(x, delta_percent)
            result_task2.set(f"Округлене число (широке) = {x_broad}")
        else:
            messagebox.showerror("Помилка", "Оберіть режим округлення.")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")


root = tk.Tk()
root.title("Завдання 2: Округлення числа")
root.geometry("400x300")

tk.Label(root, text="Число (x):").pack(pady=5)
entry_x = tk.Entry(root)
entry_x.pack()

rounding_mode = tk.StringVar(value='narrow')
tk.Radiobutton(root, text="Вузьке", variable=rounding_mode, value='narrow').pack()
tk.Radiobutton(root, text="Широке", variable=rounding_mode, value='broad').pack()

tk.Label(root, text="Абсолютна похибка (delta):").pack(pady=5)
entry_delta = tk.Entry(root)
entry_delta.pack()

tk.Label(root, text="Відсоткова похибка (delta%):").pack(pady=5)
entry_delta_percent = tk.Entry(root)
entry_delta_percent.pack()

result_task2 = tk.StringVar()
tk.Label(root, textvariable=result_task2).pack(pady=5)

tk.Button(root, text="Виконати завдання 2", command=task2).pack(pady=5)

root.mainloop()
