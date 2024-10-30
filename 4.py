import math
import pandas as pd
import matplotlib.pyplot as plt


def prompt_function(default_desc, default_func):
    """Ask the user if they want to use the default function or enter a new one."""
    print(f"Default function: {default_desc}")
    if input("Use this function? (yes/no): ").strip().lower() == "yes":
        return default_func
    user_input = input("Enter your function f(x) = ")
    return lambda x: eval(user_input, {**vars(math), "x": x})


def rectangle_method(func, a, b, n):
    """Calculate the left, right, and midpoint Riemann sums for integration."""
    step = (b - a) / n
    left = sum(func(a + i * step) for i in range(n)) * step
    right = sum(func(a + (i + 1) * step) for i in range(n)) * step
    midpoint = sum(func(a + (i + 0.5) * step) for i in range(n)) * step
    return left, right, midpoint  # Return all three results


def simpson_method(func, a, b, n):
    """Simpson's method (even number of segments required)."""
    if n % 2 != 0:
        raise ValueError("The number of segments must be even.")
    step = (b - a) / n
    odd_sum = sum(func(a + i * step) for i in range(1, n, 2))
    even_sum = sum(func(a + i * step) for i in range(2, n, 2))
    return (step / 3) * (func(a) + func(b) + 4 * odd_sum + 2 * even_sum)


def trapezoidal_method(func, a, b, n):
    """Trapezoidal method for integration."""
    step = (b - a) / n
    total_sum = sum(func(a + i * step) for i in range(1, n))
    return (total_sum + (func(a) + func(b)) / 2) * step


def generate_data_table(func, a, b, n):
    """Generate a table of values x and f(x) at the interval endpoints."""
    step = (b - a) / n
    data = {
        "Index": range(n + 1),
        "x": [round(a + i * step, 4) for i in range(n + 1)],
        "f(x)": [round(func(a + i * step), 4) for i in range(n + 1)]
    }
    return pd.DataFrame(data)


def generate_midpoint_table(func, a, b, n):
    """Generate a table of values at midpoints of the intervals."""
    step = (b - a) / n
    data = {
        "Index": range(1, n + 1),
        "Midpoint x": [round(a + (i - 0.5) * step, 4) for i in range(1, n + 1)],
        "f(Midpoint x)": [round(func(a + (i - 0.5) * step), 4) for i in range(1, n + 1)]
    }
    return pd.DataFrame(data)


def plot_left_rectangles(func, a, b, n, title):
    """Plot the function graph with left rectangles."""
    step = (b - a) / n
    x_values = [a + i * step for i in range(n)]
    f_values = [func(x) for x in x_values]

    x_range = [a + i * (b - a) / 100 for i in range(101)]
    plt.plot(x_range, [func(x) for x in x_range], label='f(x)', color='blue')

    for i in range(n):
        plt.bar(x_values[i], f_values[i], width=step, align='edge', alpha=0.5, color='lightblue',
                label='Left Rectangle' if i == 0 else "")

    plt.scatter(x_values, f_values, color='red', zorder=5)

    plt.title(title, fontsize=16)
    plt.xlabel("x", fontsize=14)
    plt.ylabel("f(x)", fontsize=14)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_function(func, a, b, n, title):
    """Plot the function graph f(x) over the interval [a, b]."""
    x_values = [round(a + i * (b - a) / n, 4) for i in range(n + 1)]
    f_values = [round(func(x), 4) for x in x_values]

    plt.figure(figsize=(10, 5))
    plt.plot(x_values, f_values, marker='o', linestyle='-', color='teal')
    plt.title(title, fontsize=16)
    plt.xlabel("x", fontsize=14)
    plt.ylabel("f(x)", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()


def main():
    print("\nChoose the integration method:")
    print("1. Rectangle Method")
    print("2. Simpson's Method")
    print("3. Trapezoidal Method")
    choice = input("Enter your choice (1/2/3): ").strip()

    if choice == "1":
        func = prompt_function("f(x) = 1 / sqrt(2 * (x ** 2) + 1)", lambda x: 1 / math.sqrt(2 * (x ** 2) + 1))
        a = float(input("Enter lower limit (recommended: 0.8): ") or 0.8)
        b = float(input("Enter upper limit (recommended: 1.6): ") or 1.6)
        n = int(input("Enter number of segments (recommended: 10): ") or 10)

        table = generate_data_table(func, a, b, n)
        print("\nTable of values x and f(x) at the endpoints:")
        print(table.to_string(index=False))

        midpoint_table = generate_midpoint_table(func, a, b, n)
        print("\nTable of f(x) at midpoints:")
        print(midpoint_table.to_string(index=False))

        left_result, right_result, midpoint_result = rectangle_method(func, a, b, n)
        print(f"\nFinal results of integration (Rectangle Method):")
        print(f"Left: {left_result:.4f}, Right: {right_result:.4f}, Midpoint: {midpoint_result:.4f}")

        plot_left_rectangles(func, a, b, n, "Graph: Rectangle Method (Left Rectangles)")

    elif choice == "2":
        func = prompt_function("f(x) = log10(x + 2) / x", lambda x: math.log10(x + 2) / x)
        a = float(input("Enter lower limit (recommended: 1.2): ") or 1.2)
        b = float(input("Enter upper limit (recommended: 2): ") or 2.0)
        n = int(input("Enter number of segments (recommended: 8): ") or 8)

        table = generate_data_table(func, a, b, n)
        print("\nTable of values x and f(x) at the endpoints:")
        print(table.to_string(index=False))

        result = simpson_method(func, a, b, n)
        print(f"\nFinal result of integration (Simpson's Method): {result:.4f}")

        plot_function(func, a, b, n, "Graph: Simpson's Method")

    elif choice == "3":
        func = prompt_function("f(x) = 1 / sqrt(x**2 + 2.3)", lambda x: 1 / math.sqrt(x ** 2 + 2.3))
        a = float(input("Enter lower limit (recommended: 0.32): ") or 0.32)
        b = float(input("Enter upper limit (recommended: 0.66): ") or 0.66)
        n = int(input("Enter number of segments (recommended: 20): ") or 20)

        table = generate_data_table(func, a, b, n)
        print("\nTable of values x and f(x) at the endpoints:")
        print(table.to_string(index=False))

        result = trapezoidal_method(func, a, b, n)
        print(f"\nFinal result of integration (Trapezoidal Method): {result:.4f}")

        plot_function(func, a, b, n, "Graph: Trapezoidal Method")


if __name__ == "__main__":
    main()
