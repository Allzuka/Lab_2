import numpy as np
import matplotlib.pyplot as plt

#  Точки интерполируемой функции:
xp = np.linspace(-np.pi, np.pi, 49)
fp = np.sinc(xp)

#  Вычисленные точки интерполяции:
x = np.linspace(-np.pi, np.pi, 94)
y = np.interp(x, xp, fp)

fig, ax = plt.subplots()

ax.plot(xp, fp,
        marker = 'o',
        label = 'sinc(x)')
ax.plot(x, y,
        marker = 'x',
        label = 'interp')

ax.set_title('Линейная интерполяция точек')

plt.show()