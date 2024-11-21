import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, diff, solve, oo, lambdify

x = symbols('x')
equation = 9 * x**4 + 8 * x**3 + 1.5 * x**2 + 2 * x - 10
print("Використовується функція: f(x) = 9x^4 + 8x^3 + 1.5x^2 + 2x - 10")

# Похідна функції
derivative = diff(equation, x)
print("\nПохідна функції: f'(x) =", derivative)

# Знаходження коренів похідної
derivative_roots = solve(derivative, x)
real_derivative_roots = [r.evalf() for r in derivative_roots if r.is_real]
print("\nКорені похідної функції (тільки дійсні):")
for i, root in enumerate(real_derivative_roots, 1):
    print(f"x{i} ≈ {root:.6f}")

# Проміжки знаків похідної функції
critical_points = sorted(real_derivative_roots)
intervals = [(-oo, critical_points[0])] + \
            [(critical_points[i], critical_points[i + 1]) for i in range(len(critical_points) - 1)] + \
            [(critical_points[-1], oo)]

print("\nПроміжки знаків похідної функції:")
for i, interval in enumerate(intervals, 1):
    print(f"Проміжок {i}: {interval}")

# Метод Ньютона
def newton_method(equation, derivative, x0, epsilon=1e-7, max_iterations=6):
    f = lambdify(x, equation)
    f_prime = lambdify(x, derivative)
    xn = x0
    steps = []
    for i in range(max_iterations):
        fxn = f(xn)
        fpxn = f_prime(xn)
        if fpxn == 0:
            print("Помилка: Похідна дорівнює нулю.")
            break
        xn_next = xn - fxn / fpxn
        delta = abs(xn_next - xn) if i > 0 else None
        steps.append((i, xn, fxn, fpxn, delta))
        xn = xn_next
    return xn, steps

# Метод бісекції
def bisection_method(equation, a, b, epsilon=1e-7, max_iterations=14):
    f = lambdify(x, equation)
    steps = []
    for i in range(max_iterations):
        c = (a + b) / 2
        fc = f(c)
        steps.append((i, a, b, c, fc, abs(b - a)))
        if abs(fc) < epsilon:
            break
        if f(a) * fc < 0:
            b = c
        else:
            a = c
    return c, steps

# Рішення методом Ньютона
x1_initial = -5 / 3
x1, newton_steps = newton_method(equation, derivative, x1_initial)

print("\nМетод Ньютона:")
print(f"{'n':<3}{'xn':<12}{'f(xn)':<12}{'f`(xn)':<12}{'|xn+1 - xn|':<12}")
for step in newton_steps:
    delta = '-' if step[4] is None else f"{step[4]:.8f}"
    print(f"{step[0]:<3}{step[1]:<12.6f}{step[2]:<12.6f}{step[3]:<12.6f}{delta:<12}")

# Рішення методом бісекції
a, b = 1 / 3, 4 / 3
x2, bisection_steps = bisection_method(equation, a, b)

print("\nМетод бісекції:")
print(f"{'n':<3}{'a':<12}{'b':<12}{'c':<12}{'f(c)':<12}{'|b - a|':<12}")
for step in bisection_steps:
    print(f"{step[0]:<3}{step[1]:<12.6f}{step[2]:<12.6f}{step[3]:<12.6f}{step[4]:<12.6f}{step[5]:<12.6f}")

# Виведення уточнених коренів
print("\nУточнені корені:")
print(f"x1 ≈ {x1:.6f}")
print(f"x2 ≈ {x2:.6f}")

# Побудова графіків
f_lambdified = lambdify(x, equation)
f_prime_lambdified = lambdify(x, derivative)
x_vals = np.linspace(-2, 2, 1000)
y_vals = f_lambdified(x_vals)
y_prime_vals = f_prime_lambdified(x_vals)

plt.figure(figsize=(10, 6))
plt.plot(x_vals, y_vals, label="f(x)")
plt.plot(x_vals, y_prime_vals, label="f'(x)", linestyle='--')
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.title("Графік функції f(x) та її похідної")
plt.legend()
plt.grid()
plt.show()
