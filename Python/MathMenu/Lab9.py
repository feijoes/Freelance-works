import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

def estimate_coef(x, y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)

    SS_xy = np.sum(y * x) - n * m_y * m_x
    SS_xx = np.sum(x * x) - n * m_x * m_x

    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1 * m_x

    return (b_1, b_0)


def gaussElimin(A, B):
    rows, columns = np.shape(A)
    if rows != columns:
        return np.array((), dtype=float)


    augmented_mat = np.column_stack((A, B))
    augmented_mat = augmented_mat.astype("float64")


    for row in range(rows - 1):
        pivot = augmented_mat[row, row]
        for col in range(row + 1, columns):
            factor = augmented_mat[col, row] / pivot
            augmented_mat[col, :] -= factor * augmented_mat[row, :]

    coefficients, vector = augmented_mat[:, 0:columns], augmented_mat[:, columns: columns + 1]
    x = np.zeros((rows, 1), dtype=float)
    for row in reversed(range(rows)):
        total = 0
        for col in range(row + 1, columns):
            total += coefficients[row, col] * x[col]

        x[row, 0] = (vector[row] - total) / coefficients[row, row]
    return np.squeeze(x)


def estimate_coef_cuadratic(xi, yi):
    xi_power_2 = np.power(xi, 2)
    xi_power_3 = np.power(xi, 3)
    xi_power_4 = np.power(xi, 4)
    n = np.size(xi)
    yi_m = np.mean(yi)

    a = np.array([[np.sum(xi_power_4), np.sum(xi_power_3), np.sum(xi_power_2)],
                  [np.sum(xi_power_3), np.sum(xi_power_2), np.sum(xi)],
                  [np.sum(xi_power_2), np.sum(xi), n]])

    b = np.array([np.sum(xi_power_2 * yi), np.sum(xi * yi), np.sum(yi)])

    coefficients = gaussElimin(a, b)
    yi_e = coefficients[0] * xi_power_2 + coefficients[1] * xi + coefficients[2]

    print(f'y = {coefficients[0]}x^2 + {coefficients[1]}x + {coefficients[2]}\n')

    table = np.column_stack((range(1, n + 1), xi, yi, xi_power_2, xi_power_3, xi_power_4, xi * yi, xi_power_2 * yi,
                             np.power(yi - yi_m, 2), np.power(yi - yi_e, 2)))
    print(tabulate(table, headers=["m", "xi", "yi", "xi^2", "xi^3", "xi^4", "xi*yi", "xi^2*yi", "(yi - yi_m)^2",
                                   "(yi-yi_e)^2"]), end="\n\n")
    return coefficients


def estimate_coef_cubic(xi, yi):
    xi_power_2 = np.power(xi, 2)
    xi_power_3 = np.power(xi, 3)
    xi_power_4 = np.power(xi, 4)
    xi_power_5 = np.power(xi, 5)
    xi_power_6 = np.power(xi, 6)
    n = np.size(xi)
    yi_m = np.mean(yi)

    a = np.array([[np.sum(xi_power_6), np.sum(xi_power_5), np.sum(xi_power_4), np.sum(xi_power_3)],
                  [np.sum(xi_power_5), np.sum(xi_power_4), np.sum(xi_power_3), np.sum(xi_power_2)],
                  [np.sum(xi_power_4), np.sum(xi_power_3), np.sum(xi_power_2), np.sum(xi)],
                  [np.sum(xi_power_3), np.sum(xi_power_2), np.sum(xi), n]])

    b = np.array([np.sum(xi_power_3 * yi), np.sum(xi_power_2 * yi), np.sum(xi * yi), np.sum(yi)])

    coefficients = gaussElimin(a, b)
    yi_e = coefficients[0] * xi_power_3 + coefficients[1] * xi_power_2 + coefficients[2] * xi + coefficients[3]
    print(f'y = {coefficients[0]}x^3 + {coefficients[1]}x^2 + {coefficients[2]}x + {coefficients[3]}\n')

    table = np.column_stack((range(1, n + 1), xi, yi, xi_power_2, xi_power_3, xi_power_4, xi_power_5, xi_power_6,
                             xi * yi, xi_power_2 * yi, xi_power_3 * yi, np.power(yi - yi_m, 2), np.power(yi - yi_e, 2)))
    print(tabulate(table, headers=["m", "xi", "yi", "xi^2", "xi^3", "xi^4", "x^5", "x^6", "xi*yi", "xi^2*yi", "xi^3*yi",
                                   "(yi - yi_m)^2", "(yi-yi_e)^2"]), end="\n\n")

    return coefficients


def estimate_coef_hiperbolic(xi, yi):
    xi_power_2 = np.power(xi, 2)
    xi_inv = np.divide(1, xi)
    xi_inv_pow_2 = np.divide(1, np.power(xi, 2))
    n = np.size(xi)
    yi_m = np.mean(yi)

    b = (n * np.sum(np.divide(yi, xi)) - np.sum(xi_inv) * np.sum(yi)) / (n * np.sum(xi_inv_pow_2) - np.power(np.sum(xi_inv), 2))

    a = np.sum(yi) / n - b * np.sum(xi_inv) / n

    yi_e = a + np.divide(b, xi)
    print(f'y = {a} + {b} / x')
    table = np.column_stack((range(1, n + 1), xi, yi, xi_power_2, xi_inv, xi_inv_pow_2, xi_inv * yi,
                             np.power(yi - yi_m, 2), np.power(yi - yi_e, 2)))
    print(tabulate(table,
                   headers=["m", "xi", "yi", "xi^2", "xi^-1", "xi^-2", "xi^-1*yi", "(yi - yi_m)^2", "(yi-yi_e)^2"]), end="\n\n")

    return [a, b]


def plot_polynomial_regression(x, y, coeff):
    x_interval = np.linspace(min(x), max(x), 100)
    model = np.poly1d(coeff)
    ax = plt.gca()
    ax.plot(x_interval, model(x_interval))

def plot_hiperbolic_regression(x, y, coeff):
    x_interval = np.linspace(min(x), max(x), 100)
    yi_e = coeff[0] + np.divide(coeff[1], x_interval)
    ax = plt.gca()
    ax.plot(x_interval, yi_e, label="$a + b / x$")

def main():
    x = np.array([1, 1, 2, 3, 4, 5, 6, 7])
    y = np.array([2, 4, 3, 6, 5, 7, 9, 8])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Regresiones')

    ax = plt.gca()
    ax.scatter(x, y, color="m", marker="o", s=10, label="Puntos")

    coeff = estimate_coef(x, y)
    plot_polynomial_regression(x, y, coeff)

    print("\nRegresión Cuadrática")
    coeff = estimate_coef_cuadratic(x, y)
    plot_polynomial_regression(x, y, coeff)

    print("\nRegresión Cúbica")
    coeff = estimate_coef_cubic(x, y)
    plot_polynomial_regression(x, y, coeff)

    print("\nRegresión Hiperbólica")
    coeff = estimate_coef_hiperbolic(x, y)
    plot_hiperbolic_regression(x, y, coeff)

    plt.legend(["Puntos", "Lineal", "Cuadrática", "Cúbica", "Hiperbólica"], loc="lower right")

    ax.grid()
    plt.show()

