import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


def get_points(prompt):
    points = []
    num_points = int(input(f"Enter the number of known {prompt} points: "))
    print(f"Enter values for {prompt} (known points):")
    for i in range(num_points):
        value = float(input(f"{prompt}[{i}]: "))
        points.append(value)
    return points


def display_table(XX, YY):
    table_X = "X: " + "".join([f"{x:7.3f}|" for x in XX])
    table_Y = "Y: " + "".join([f"{y:7.3f}|" for y in YY])
    print("\nTable of values of a function:")
    print(table_X)
    print(table_Y)


def compute_lagrange_polynomial(XX, YY):
    x = sp.Symbol('x')
    terms = [
        YY[i] * np.prod([(x - XX[j]) / (XX[i] - XX[j]) for j in range(len(XX)) if i != j])
        for i in range(len(XX))
    ]
    L = sp.simplify(sum(terms))
    print(f"\nThe interpolation polynomial L(x) is:\n{L}")
    return L


def interpolate_values(L, XX, num_points=1):
    for _ in range(num_points):
        r = float(input(f"\nEnter value X to interpolate: "))
        y_value = L.subs(sp.Symbol('x'), r)
        print(f"For X = {r:.1f}, Y = {y_value:.3f}")


def plot_interpolation(L_func, XX, YY):
    x_vals = np.linspace(min(XX) - 1, max(XX) + 1, 500)
    y_vals = L_func(x_vals)
    plt.plot(x_vals, y_vals, label='Lagrange Polynomial', color='green')
    plt.scatter(XX, YY, color='red', label='Given Points')
    plt.axhline(0, color='black', linestyle='--')
    plt.axvline(0, color='black', linestyle='--')
    plt.title('Lagrange Interpolation Polynomial')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.legend()
    plt.show()


def main():
    XX = get_points("X")
    YY = get_points("Y")
    display_table(XX, YY)

    L_simplified = compute_lagrange_polynomial(XX, YY)
    L_func = sp.lambdify(sp.Symbol('x'), L_simplified, 'numpy')

    num_interp = int(input("\nEnter the number of points to interpolate: "))
    interpolate_values(L_simplified, XX, num_interp)

    plot_interpolation(L_func, XX, YY)


if __name__ == "__main__":
    main()