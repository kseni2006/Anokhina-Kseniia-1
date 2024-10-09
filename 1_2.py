import tkinter as tk
from tkinter import messagebox


def round_value_narrow(value, uncertainty):
    if uncertainty < 0.05:
        return round(value, 1)
    return round(value)


def round_value_broad(value, percent_error):
    uncertainty = value * (percent_error / 100)
    return round(value - uncertainty, 2)


def perform_rounding():
    try:
        value = float(value_entry.get())
        rounding_mode = mode.get()

        if rounding_mode == 'narrow':
            uncertainty = float(uncertain_entry.get())
            rounded_value = round_value_narrow(value, uncertainty)
            result_text.set(f"Округлене (вузьке): {rounded_value}")
        elif rounding_mode == 'broad':
            percent_error = float(uncertain_percent_entry.get())
            rounded_value = round_value_broad(value, percent_error)
            result_text.set(f"Округлене (широке): {rounded_value}")
    except ValueError:
        messagebox.showerror("Помилка", "Невірні дані!")


# Інтерфейс
app = tk.Tk()
app.title("Округлення значень")
app.geometry("400x300")
app.configure(bg="#e6f2ff")  # Зміна кольору фону

font_large = ("Arial", 14)
font_medium = ("Arial", 12)

tk.Label(app, text="Число:", bg="#e6f2ff", font=font_medium).pack(pady=10)
value_entry = tk.Entry(app, font=font_medium)
value_entry.pack()

mode = tk.StringVar(value='narrow')
tk.Radiobutton(app, text="Вузьке", variable=mode, value='narrow', bg="#e6f2ff", font=font_medium).pack(pady=5)
tk.Radiobutton(app, text="Широке", variable=mode, value='broad', bg="#e6f2ff", font=font_medium).pack(pady=5)

tk.Label(app, text="Абсолютна похибка:", bg="#e6f2ff", font=font_medium).pack(pady=10)
uncertain_entry = tk.Entry(app, font=font_medium)
uncertain_entry.pack()

tk.Label(app, text="Відсоткова похибка:", bg="#e6f2ff", font=font_medium).pack(pady=10)
uncertain_percent_entry = tk.Entry(app, font=font_medium)
uncertain_percent_entry.pack()

result_text = tk.StringVar()
tk.Label(app, textvariable=result_text, bg="#e6f2ff", font=font_medium, fg="blue").pack(pady=20)

tk.Button(app, text="Округлити", command=perform_rounding, bg="#0066cc", fg="white", font=font_large).pack(pady=10)

app.mainloop()
