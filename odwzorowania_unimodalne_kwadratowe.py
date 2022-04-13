import numpy as np
import matplotlib.pyplot as plt

# Naciśnięcie "n" rysuje kolejne linie
# Naciśnięcie "p" rysuje podstawową parabolę
# Naciśnięcie "r" usuwa narysowane linie


# Parametry, które trzeba ręcznie wybrać
r = 2.3  # parametr kontolny
x0 = 0.4  # punkt początkowy
rzad = 1  # rząd złożenia


def y(xx): return r * xx * (1 - xx)


def zl(iks):
    for i in range(rzad):
        yy = y(iks)
        iks = yy
    return iks


x = np.linspace(0, 1, 1000)

x00 = x0
n = 0

fig, ax = plt.subplots(1)


def ploty():
    global x0
    global text
    x0 = x00
    ax.plot(x, zl(x))

    ax.plot(x, x, ls='--', alpha=0.4)
    ax.set_ylim(0)
    ax.grid(ls='--')
    ax.plot([x0, x0], [0, zl(x0)], color='green')

    text = ax.text(1, 1, f'n = {n}')


ploty()


def update(event):
    global x0
    global n
    if event.key == "n":

        n += 1
        text.set_text(f'n = {n}')

        ax.plot([x0, zl(x0)], [zl(x0), zl(x0)], color='green')  # kreska pozioma
        ax.plot([zl(x0), zl(x0)], [zl(x0), zl(zl(x0))], color='green')  # kreska pionowa
        x0 = zl(x0)

        fig.canvas.draw_idle()

    elif event.key == "p":
        ax.plot(x, y(x))
        fig.canvas.draw_idle()

    elif event.key == "r":
        ax.cla()
        ploty()
        n = 0
        text.set_text(f'n = {n}')
        fig.canvas.draw_idle()

    return x0


fig.canvas.mpl_connect("key_press_event", update)
plt.show()
