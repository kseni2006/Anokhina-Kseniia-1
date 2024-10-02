import tkinter as tk
from tkinter import messagebox
import math


def absolute_error(real_value, approx_value):
    return abs(real_value - approx_value)


def task1():
    try:
        n1 = float(entry_n1.get())
        x1 = float(entry_x1.get())
        n2 = float(entry_n2.get())
        N2 = float(entry_N2.get())
        x2 = float(entry_x2.get())

        sqrt_n1 = math.sqrt(n1)
        exact_ratio = n2 / N2

        error1 = absolute_error(sqrt_n1, x1)
        error2 = absolute_error(exact_ratio, x2)

        if error1 < error2:
            result_task1.set(f"Наближення до sqrt({n1}) точніше: абсолютна похибка = {error1:.4f}")
        else:
            result_task1.set(f"Наближення до {n2}/{N2} точніше: абсолютна похибка = {error2:.4f}")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")


root = tk.Tk()
root.title("Завдання 1: Точність наближень")
root.geometry("400x350")

tk.Label(root, text="Число під коренем (n1):").pack(pady=5)
entry_n1 = tk.Entry(root)
entry_n1.pack()

tk.Label(root, text="Наближення sqrt(n1):").pack(pady=5)
entry_x1 = tk.Entry(root)
entry_x1.pack()

tk.Label(root, text="Чисельник дробу (n2):").pack(pady=5)
entry_n2 = tk.Entry(root)
entry_n2.pack()

tk.Label(root, text="Знаменник дробу (N2):").pack(pady=5)
entry_N2 = tk.Entry(root)
entry_N2.pack()

tk.Label(root, text="Наближення n2/N2:").pack(pady=5)
entry_x2 = tk.Entry(root)
entry_x2.pack()

result_task1 = tk.StringVar()
tk.Label(root, textvariable=result_task1).pack(pady=5)

tk.Button(root, text="Виконати завдання 1", command=task1).pack(pady=5)

root.mainloop()
