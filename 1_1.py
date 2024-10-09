import tkinter as tk
from tkinter import messagebox
import math


def percent_error(real, approx):
    return abs((real - approx) / real) * 100


def calculate_accuracy():
    try:
        # Перевірка, чи поля не порожні
        if not num1_entry.get() or not sqrt1_entry.get() or not num2_entry.get() or not denom2_entry.get() or not approx2_entry.get():
            messagebox.showerror("Помилка", "Усі поля повинні бути заповнені!")
            return

        number1 = float(num1_entry.get())
        approx_sqrt1 = float(sqrt1_entry.get())
        numerator = float(num2_entry.get())
        denominator = float(denom2_entry.get())
        approx_fraction = float(approx2_entry.get())

        # Перевірка, чи знаменник не є нулем
        if denominator == 0:
            messagebox.showerror("Помилка", "Знаменник не може бути нульовим!")
            return

        actual_sqrt = math.sqrt(number1)
        actual_fraction = numerator / denominator

        sqrt_error = percent_error(actual_sqrt, approx_sqrt1)
        fraction_error = percent_error(actual_fraction, approx_fraction)

        # Показуємо результати: оновлюємо значення StringVar
        if sqrt_error < fraction_error:
            result_text.set(f"Корінь точніше: похибка = {sqrt_error:.4f}%")
        else:
            result_text.set(f"Дріб точніше: похибка = {fraction_error:.4f}%")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених даних!")


# Інтерфейс
app = tk.Tk()
app.title("Точність наближень")
app.geometry("400x400")
app.configure(bg="#e6f2ff")  # Зміна кольору фону

font_large = ("Arial", 14)
font_medium = ("Arial", 12)

tk.Label(app, text="Число для кореня:", bg="#e6f2ff", font=font_medium).pack(pady=10)
num1_entry = tk.Entry(app, font=font_medium)
num1_entry.pack()

tk.Label(app, text="Приблизне sqrt:", bg="#e6f2ff", font=font_medium).pack(pady=10)
sqrt1_entry = tk.Entry(app, font=font_medium)
sqrt1_entry.pack()

tk.Label(app, text="Чисельник дробу:", bg="#e6f2ff", font=font_medium).pack(pady=10)
num2_entry = tk.Entry(app, font=font_medium)
num2_entry.pack()

tk.Label(app, text="Знаменник дробу:", bg="#e6f2ff", font=font_medium).pack(pady=10)
denom2_entry = tk.Entry(app, font=font_medium)
denom2_entry.pack()

tk.Label(app, text="Приблизний дріб:", bg="#e6f2ff", font=font_medium).pack(pady=10)
approx2_entry = tk.Entry(app, font=font_medium)
approx2_entry.pack()

result_text = tk.StringVar()
tk.Label(app, textvariable=result_text, bg="#e6f2ff", font=font_medium, fg="blue").pack(pady=20)

tk.Button(app, text="Обчислити", command=calculate_accuracy, bg="#0066cc", fg="white", font=font_large).pack(pady=10)

app.mainloop()
