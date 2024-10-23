import matplotlib.pyplot as plt
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


def compute_deltas(Y):
    """Обчислює таблицю дельт."""
    n = len(Y)
    deltas = [Y[:]]  # Копіюємо Y
    for i in range(1, n):
        deltas.append([deltas[i - 1][j + 1] - deltas[i - 1][j] for j in range(n - i)])
    return deltas


def display_function_table(X, Y):
    """Друк таблиці значень функції."""
    print("\nTable of values of a function:")
    print("\tX\t|\tY")
    print(" ---------------------------")
    for x, y in zip(X, Y):
        print(f"\t{x:.1f}\t|\t{y:.3f}")
    print()


def display_deltas(deltas):
    """Друк таблиці дельт без обмежень на кількість елементів у рядку."""
    df = pd.DataFrame(deltas).transpose()
    df.columns = [f"Delta {i}" for i in range(len(deltas))]
    df.fillna(' ', inplace=True)  # Заповнюємо порожні значення пробілами
    pd.set_option('display.max_columns', None)
    pd.set_option('display.expand_frame_repr', False)
    print("\nDeltas table:")
    print(df.to_string(index=False))


def calculate_q(X, xx, h):
    """Обчислення q для конкретного значення xx."""
    if not (X[0] <= xx <= X[-1]):
        raise ValueError(f"Value {xx} is out of bounds of the X values.")
    j = max(i for i in range(len(X)) if X[i] <= xx)
    q = (xx - X[j]) / h
    return q, j


def compute_derivatives(q, j, deltas, h):
    """Обчислення першої та другої похідної."""
    first_derivative = (
        (deltas[1][j] if len(deltas) > 1 else 0)
        + (deltas[2][j] * (2 * q - 1) / 2 if len(deltas) > 2 and j < len(deltas[2]) else 0)
        + (deltas[3][j] * (3 * q**2 - 6 * q + 2) / 6 if len(deltas) > 3 and j < len(deltas[3]) else 0)
        + (deltas[4][j] * (4 * q**3 - 18 * q**2 + 22 * q - 6) / 24 if len(deltas) > 4 and j < len(deltas[4]) else 0)
        + (deltas[5][j] * (5 * q**4 - 40 * q**3 + 105 * q**2 - 100 * q + 24) / 120 if len(deltas) > 5 and j < len(deltas[5]) else 0)
    ) / h

    second_derivative = (
        (deltas[2][j] if len(deltas) > 2 and j < len(deltas[2]) else 0)
        + (deltas[3][j] * (q - 1) if len(deltas) > 3 and j < len(deltas[3]) else 0)
        + (deltas[4][j] * (12 * q**2 - 36 * q + 22) / 24 if len(deltas) > 4 and j < len(deltas[4]) else 0)
        + (deltas[5][j] * (20 * q**3 - 120 * q**2 + 210 * q - 100) / 120 if len(deltas) > 5 and j < len(deltas[5]) else 0)
    ) / (h**2)

    return first_derivative, second_derivative


def plot_functions(X, Y, xx_values, first_derivatives, second_derivatives):
    """Графік функції та похідних."""
    plt.figure(figsize=(10, 8))

    # Графік функції
    plt.subplot(3, 1, 1)
    plt.plot(X, Y, 'purple', marker='o', label="Y(x)")
    plt.title("Function Y(x)")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.legend()

    # Графік першої похідної
    plt.subplot(3, 1, 2)
    plt.plot(xx_values, first_derivatives, 'orange', marker='o', label="Y'(x)")
    plt.title("First Derivative Y'(x)")
    plt.xlabel("X")
    plt.ylabel("Y'")
    plt.grid(True)
    plt.legend()

    # Графік другої похідної
    plt.subplot(3, 1, 3)
    plt.plot(xx_values, second_derivatives, 'lightblue', marker='o', label="Y''(x)")
    plt.title("Second Derivative Y''(x)")
    plt.xlabel("X")
    plt.ylabel("Y''")
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()


def main():
    # Читання даних
    data = pd.read_csv(r'C:\Users\user\PycharmProjects\methods\3.csv', delimiter='\s+')
    X = data['x_i'].values
    Y = data['y_i'].values

    # Обчислення h
    h = X[1] - X[0]
    print(f"Calculated h = {h:.2f}")

    # Друк таблиці функцій та дельт
    display_function_table(X, Y)
    deltas = compute_deltas(Y)
    display_deltas(deltas)

    # Введення користувачем значень xx
    m = int(input("\nEnter the number of values to check (xx): "))
    xx_values, first_derivatives, second_derivatives = [], [], []

    for i in range(m):
        xx = float(input(f"Enter value xx[{i}] = "))
        if not (X[0] <= xx <= X[-1]):
            print(f"Value {xx} is out of bounds of the X values.")
            continue


        q, j = calculate_q(X, xx, h)
        first_deriv, second_deriv = compute_derivatives(q, j, deltas, h)

        xx_values.append(xx)
        first_derivatives.append(first_deriv)
        second_derivatives.append(second_deriv)

        print(f"For x = {xx:.2f}: Y' = {first_deriv:.4f}, Y'' = {second_deriv:.4f}")

    # Побудова графіків
    plot_functions(X, Y, xx_values, first_derivatives, second_derivatives)


if __name__ == "__main__":
    main()