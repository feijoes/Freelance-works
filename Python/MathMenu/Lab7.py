
import matplotlib.pyplot as plt
import numpy as np


def f(x):
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

simpson38_integration = simpson38(a, b, n)
print(
  f"El área bajo la curva usando el método de simpson 3/8 es {simpson38_integration}"
)

simpson13_integration = simpson13(a, b, n)
print(
  f"El área bajo la curva usando el método de simpson 1/3 es {simpson13_integration}"
)

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
plt.text((b - a) / 2,
         0.6,
         "$\mathregular{I_{tr} = %.3f}$" % (trapezoidal_integration),
         fontsize=15,
         ha="center")
plt.text((b - a) / 2,
         1,
         "$\mathregular{I_{38} = %.3f}$" % (simpson38_integration),
         fontsize=15,
         ha="center")
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