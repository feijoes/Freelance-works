import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText


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



def main():
    x = np.array([1, 1, 2, 3, 4, 5, 6, 7])
    y = np.array([2, 4, 3, 6, 5, 7, 9, 8])

    b = estimate_coef(x, y)
    print("Coeficientes de la ecuación y=mx+b:\n\nm = {} \
		\nb = {}".format(b[1], b[0]))

    plot_regression_line(x, y, b)


if __name__ == "__main__":
    main()