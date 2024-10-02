import tkinter as tk
from tkinter import messagebox


def calculate_delta_narrow(x):
    decimal_places = len(str(x).split(".")[1]) if "." in str(x) else 0
    last_digit_value = 10 ** (-decimal_places)
    return last_digit_value / 2


def calculate_delta_broad(x):
    decimal_places = len(str(x).split(".")[1])
    last_digit_value = 10 ** (-decimal_places)
    return last_digit_value


def task3():
    try:
        x = float(entry_x_task3.get())
        choice = error_mode.get()

        if choice == 'narrow':
            delta_narrow = calculate_delta_narrow(x)
            relative_error = delta_narrow / x
            result_task3.set(f"Абсолютна похибка (вузьке) = {delta_narrow:.4f}, Відносна похибка = {relative_error * 100:.4f}%")
        elif choice == 'broad':
            delta_broad = calculate_delta_broad(x)
            relative_error = delta_broad / x
            result_task3.set(f"Абсолютна похибка (широке) = {delta_broad:.4f}, Відносна похибка = {relative_error * 100:.4f}%")
        else:
            messagebox.showerror("Помилка", "Оберіть тип похибки.")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених значень!")


root = tk.Tk()
root.title("Завдання 3: Обчислення похибок")
root.geometry("400x200")

tk.Label(root, text="Число (x):").pack(pady=5)
entry_x_task3 = tk.Entry(root)
entry_x_task3.pack()

error_mode = tk.StringVar(value='narrow')
tk.Radiobutton(root, text="Вузьке", variable=error_mode, value='narrow').pack()
tk.Radiobutton(root, text="Широке", variable=error_mode, value='broad').pack()

result_task3 = tk.StringVar()
tk.Label(root, textvariable=result_task3).pack(pady=5)

tk.Button(root, text="Виконати завдання 3", command=task3).pack(pady=5)

root.mainloop()
