import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Button, Toplevel

# Функції для обчислень
def f_euler(x, y):
    return x + np.cos(y / np.sqrt(5))

def f_euler_cauchy(x, y):
    return x + np.sin(y / 3)

# Метод Ейлера
def euler_method(x0, y0, h, n):
    x = [x0]
    y = [y0]
    for i in range(n):
        x_next = x[-1] + h
        y_next = y[-1] + h * f_euler(x[-1], y[-1])
        x.append(x_next)
        y.append(y_next)
    return x, y

# Метод Ейлера-Коші
def euler_cauchy_method(x0, y0, h, n):
    x = [x0]
    y = [y0]
    for i in range(n):
        x_next = x[-1] + h
        y_predict = y[-1] + h * f_euler_cauchy(x[-1], y[-1])
        y_next = y[-1] + h / 2 * (f_euler_cauchy(x[-1], y[-1]) + f_euler_cauchy(x_next, y_predict))
        x.append(x_next)
        y.append(y_next)
    return x, y

# Основна функція для GUI
def main():
    # Початкові умови
    x0_a, y0_a, h_a, n_a = 1.8, 2.6, 0.1, 10  # Метод Ейлера
    x0_b, y0_b, h_b, n_b = 1.6, 4.6, 0.1, 10  # Метод Ейлера-Коші

    # Обчислення
    x_euler, y_euler = euler_method(x0_a, y0_a, h_a, n_a)
    x_euler_cauchy, y_euler_cauchy = euler_cauchy_method(x0_b, y0_b, h_b, n_b)

    # Форматування таблиць з чотирма знаками після коми
    table_euler = "\n".join([f"{i:2d} | {xi:6.4f} | {yi:6.4f}" for i, (xi, yi) in enumerate(zip(x_euler, y_euler))])
    table_euler_cauchy = "\n".join([f"{i:2d} | {xi:6.4f} | {yi:6.4f}" for i, (xi, yi) in enumerate(zip(x_euler_cauchy, y_euler_cauchy))])

    # Головне вікно
    root = Tk()
    root.title("Методи чисельного розв'язання")
    root.geometry("400x400")

    # Перша сторінка
    def show_first_page():
        Label(root, text="Початкові умови", font=("Arial", 14, "bold")).pack(pady=10)

        # Дані для методу Ейлера
        Label(root, text="Метод Ейлера:", font=("Arial", 12, "bold")).pack(anchor="w", padx=20)
        Label(root, text=f"x0 = {x0_a}", font=("Arial", 12)).pack(anchor="w", padx=40)
        Label(root, text=f"y0 = {y0_a}", font=("Arial", 12)).pack(anchor="w", padx=40)
        Label(root, text=f"h = {h_a}", font=("Arial", 12)).pack(anchor="w", padx=40)
        Label(root, text=f"Кроків = {n_a}", font=("Arial", 12)).pack(anchor="w", padx=40)

        # Дані для методу Ейлера-Коші
        Label(root, text="Метод Ейлера-Коші:", font=("Arial", 12, "bold")).pack(anchor="w", padx=20, pady=10)
        Label(root, text=f"x0 = {x0_b}", font=("Arial", 12)).pack(anchor="w", padx=40)
        Label(root, text=f"y0 = {y0_b}", font=("Arial", 12)).pack(anchor="w", padx=40)
        Label(root, text=f"h = {h_b}", font=("Arial", 12)).pack(anchor="w", padx=40)
        Label(root, text=f"Кроків = {n_b}", font=("Arial", 12)).pack(anchor="w", padx=40)

        Button(root, text="Переглянути таблиці", command=show_second_page, font=("Arial", 12)).pack(pady=20)

    # Друга сторінка
    def show_second_page():
        second_page = Toplevel(root)
        second_page.title("Таблиці результатів")
        second_page.geometry("500x500")

        Label(second_page, text="Таблиця для методу Ейлера", font=("Arial", 14)).pack(pady=10)
        Label(second_page, text="i  |   xi   |   yi", font=("Courier", 12, "bold")).pack()
        Label(second_page, text=table_euler, font=("Courier", 12), justify="left").pack(pady=10)

        Label(second_page, text="Таблиця для методу Ейлера-Коші", font=("Arial", 14)).pack(pady=10)
        Label(second_page, text="i  |   xi   |   yi", font=("Courier", 12, "bold")).pack()
        Label(second_page, text=table_euler_cauchy, font=("Courier", 12), justify="left").pack(pady=10)

        Button(second_page, text="Закрити", command=second_page.destroy, font=("Arial", 12)).pack(pady=10)
        Button(second_page, text="Перейти до графіків", command=show_third_page, font=("Arial", 12)).pack(pady=10)


    # Третя сторінка
    def show_third_page():
        # Графік для методу Ейлера
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)
        plt.plot(x_euler, y_euler, marker='o', label="Метод Ейлера")
        plt.title("Метод Ейлера")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.legend()

        # Графік для методу Ейлера-Коші
        plt.subplot(1, 2, 2)
        plt.plot(x_euler_cauchy, y_euler_cauchy, marker='s', label="Метод Ейлера-Коші", color="orange")
        plt.title("Метод Ейлера-Коші")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid()
        plt.legend()

        # Показати графіки
        plt.tight_layout()
        plt.show()

    show_first_page()
    root.mainloop()

# Запуск основної функції
if __name__ == "__main__":
    main()
