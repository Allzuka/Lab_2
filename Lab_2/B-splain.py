import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

xp = [0., 0.71428571, 1.42857143, 2.14285714, 2.85714286, 3.57142857, 4.28571429, 5.]
yp = [0., -0.86217009, -2.4457478, -2.19354839, -2.32844575, -0.48680352, -0.41055718, -3.]

length = len(xp)
t = np.linspace(0., xp[-1], length - 2, endpoint=True)
t = np.append([0, 0, 0], t)
t = np.append(t, [xp[-1], xp[-1], xp[-1]])

tck = [t, [xp, yp], 3]
u = np.linspace(0, 5., 1000, endpoint=True)
out = interpolate.splev(u, tck)

x_value_in_xp_domain = 4.
y_value_out = interpolate.splev(x_value_in_xp_domain, tck)

plt.plot(xp, yp, linestyle='--', marker='o', color='purple')
plt.plot(out[0], out[1], color = 'teal')
plt.plot(x_value_in_xp_domain, y_value_out[1], marker='o', color = 'orangered')
plt.plot(y_value_out[0], y_value_out[1], marker='o', color = 'black')
plt.axvline(x=x_value_in_xp_domain, color = 'orangered')
plt.show()
