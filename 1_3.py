import tkinter as tk
from tkinter import messagebox


def compute_error(value, mode):
    decimal_places = len(str(value).split(".")[1]) if "." in str(value) else 0
    last_digit_value = 10 ** (-decimal_places)

    if mode == 'narrow':
        return last_digit_value / 2
    return last_digit_value


def show_errors():
    try:
        value = float(entry_value.get())
        error_mode = mode_choice.get()

        abs_error = compute_error(value, error_mode)
        relative_error = (abs_error / value) * 100

        result_text.set(f"Абс. похибка = {abs_error:.5f}, Відносна похибка = {relative_error:.5f}%")
    except ValueError:
        messagebox.showerror("Помилка", "Перевірте правильність введених даних!")


# Інтерфейс
app = tk.Tk()
app.title("Розрахунок похибок")
app.geometry("400x250")
app.configure(bg="#e6f2ff")

font_large = ("Arial", 14)
font_medium = ("Arial", 12)

tk.Label(app, text="Значення:", bg="#e6f2ff", font=font_medium).pack(pady=10)
entry_value = tk.Entry(app, font=font_medium)
entry_value.pack()

mode_choice = tk.StringVar(value='narrow')
tk.Radiobutton(app, text="Вузьке", variable=mode_choice, value='narrow', bg="#e6f2ff", font=font_medium).pack(pady=5)
tk.Radiobutton(app, text="Широке", variable=mode_choice, value='broad', bg="#e6f2ff", font=font_medium).pack(pady=5)

result_text = tk.StringVar()
tk.Label(app, textvariable=result_text, bg="#e6f2ff", font=font_medium, fg="blue").pack(pady=20)

tk.Button(app, text="Обчислити похибку", command=show_errors, bg="#0066cc", fg="white", font=font_large).pack(pady=10)

app.mainloop()
