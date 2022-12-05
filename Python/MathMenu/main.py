import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText
from tabulate import tabulate

def Lab7(funtionType):


  def f(x) -> float: 
    return 0.2 + 25 * x - 200 * (x**2) + 675 * (x**3) - 900 * (x**4) + 400 * (x**5)


  def simpson38(a, b, n):
    size = (float(b - a) / n)
    sum = f(a) + f(b)

    for i in range(1, n):
      if i % 3 == 0:
        sum = sum + 2 * f(a + i * size)
      else:
        sum = sum + 3 * f(a + i * size)

    return (float(3 * size) / 8) * sum


  def trapezoidal(a, b, n):
    h = (b - a) / n
    xi = a
    sum = f(xi)
    for i in range(1, n, 1):
      xi = xi + h
      sum = sum + 2 * f(xi)

    sum = sum + f(b)
    area = h * sum / 2
    return area


  def simpson13(a, b, n):
    h = (b - a) / n

    integration = f(a) + f(b)
    for i in range(1, n):
      k = a + i * h

      if i % 2 == 0:
        integration = integration + 2 * f(k)
      else:
        integration = integration + 4 * f(k)

    return integration * h / 3



  a = eval(input("Limite inferior (a): "))
  b = eval(input("Limite superior (b): "))
  n = eval(input("Numero de tramos:\n"))
  #a = 0
  #b = 0.8
  #n = 10
  if funtionType == "simpson38":
      simpson38_integration = simpson38(a, b, n)
      print(f"El área bajo la curva usando el método de simpson 3/8 es {simpson38_integration}")

  if funtionType == "simpson13":
      simpson13_integration = simpson13(a, b, n)
      print(
        f"El área bajo la curva usando el método de simpson 1/3 es {simpson13_integration}"
      )
  if funtionType == "trapezoidal":
      trapezoidal_integration = trapezoidal(a, b, n)
      print(
        f"El área bajo la curva usando el método de los trapecios es {trapezoidal_integration}"
      )

  # Graficas
  x = np.linspace(a, b, n * 100)
  y = f(x)

  fig, ax = plt.subplots()
  p = np.linspace(a, b, n + 1)
  fp = f(p)

  ax.plot(x, y)
  plt.plot(p, fp, color="orange", marker="o")
  plt.legend(["f(x)", "muestras"], loc="upper right")
  if funtionType == "trapezoidal":
      plt.text((b - a) / 2,
              0.6,
              "$\mathregular{I_{tr} = %.3f}$" % (trapezoidal_integration),
              fontsize=15,
              ha="center")
  if funtionType == "simpson38":
      plt.text((b - a) / 2,
           1,
           "$\mathregular{I_{38} = %.3f}$" % (simpson38_integration),
           fontsize=15,
           ha="center")
  if funtionType == "simpson13":
      plt.text((b - a) / 2,
           1.4,
           "$\mathregular{I_{13} = %.3f}$" % (simpson13_integration),
           fontsize=15,
           ha="center")

  for i in range(1, n + 1):
    ax.annotate("$\mathregular{T_{%d}}$" % (i), (p[i], 0.1))
    plt.vlines(x=p[i], ymin=0, ymax=fp[i], colors='white')

  plt.fill_between(p, 0, fp, color="#fefad2")
  plt.grid()
  plt.axvline(0, color="black")
  plt.axhline(0, color="black")
  plt.title("Integral: Regla de trapecios")
  plt.xlabel("x")
  plt.ylabel("f(x)")
  plt.show()
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

def Lab9():
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


def estimate_coef(x, y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)

    xy = np.sum(y * x) - n * m_y * m_x
    xx = np.sum(x * x) - n * m_x * m_x

    b = xy / xx
    m = m_y - b * m_x

    return (m, b)


def plot_regression_line(x, y, b):
    plt.scatter(x, y, color="#411C6C", marker="o", s=30)

    y_pred = b[1] * x + b[0] 

    plt.plot(x, y_pred, color="#B61148")
    plt.legend(["Puntos", "Curva resultante"], loc="upper left")


    plt.xlabel('x')
    plt.ylabel('y')
    plt.title("Regresión lineal")

    text_box = AnchoredText('$y = %.2fx + %.2f$' % (b[1], b[0]), frameon=True, loc=4, pad=0.5)
    plt.setp(text_box.patch, facecolor='#E2C4DC', alpha=0.5)
    plt.gca().add_artist(text_box)
    plt.show()



def RegresionLineal():
    x = np.array([1, 1, 2, 3, 4, 5, 6, 7])
    y = np.array([2, 4, 3, 6, 5, 7, 9, 8])

    b = estimate_coef(x, y)
    print("Coeficientes de la ecuación y=mx+b:\n\nm = {} \
		\nb = {}".format(b[1], b[0]))

    plot_regression_line(x, y, b)


types = {
    1: "trapezoidal",
    2: "simpson13",
    3: "simpson38",
    4: "regresionLineal",
    5: "RegresionPolinomial"
}


funcion = int(input("Elija el numero del metodo que quiere elegir\n1 Trapecio\n2 Simpson 1/3\n3 Simpson 3/8\n4 Regresion Lineal\n5 Regresion Polinomial (Saldram Regresion Cuadratica, Cubica y Hiperbolica\n"))


if funcion in [1,2,3]:
    Lab7(types[funcion])
if funcion == 4:
    RegresionLineal()
if funcion == 5:
    Lab9()

    
    


