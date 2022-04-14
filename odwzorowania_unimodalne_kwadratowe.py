import numpy as np
import matplotlib.pyplot as plt

# Naciśnięcie "n" rysuje kolejne linie
# Naciśnięcie "p" rysuje podstawową parabolę
# Naciśnięcie "r" usuwa narysowane linie


# Parametry, które trzeba ręcznie wybrać
r = 3  # parametr kontolny
x0 = 0.61  # punkt początkowy
rzad = 1  # rząd złożenia


#  Odkomentuj odwzorowanie, które cię interesuje
# def y(xx): return r * xx * (1 - xx)  # Odwzorowanie logistyczne
# def y(xx): return 1 - 2 * np.abs(xx - 1 / 2)  # TentMap
# def y(xx): return 2 * xx % 1  # ModMap


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
    global text_x0
    x0 = x00
    ax.plot(x, zl(x))

    ax.plot(x, x, ls='--', alpha=0.4)
    ax.set_ylim(0)
    ax.grid(ls='--')
    ax.plot([x0, x0], [0, zl(x0)], color='green')

    text = ax.text(1, 1, f'n = {n}')
    text_x0 = ax.text(1, 0.5, f'xn = {x0}')


ploty()


def update(event):
    global x0
    global n
    if event.key == "n":

        n += 1
        text.set_text(f'n = {n}')
        text_x0.set_text(f'xn = {x0}')

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
