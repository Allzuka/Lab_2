import numpy as np
import scipy as sp
import pylab as pl 
from scipy.optimize import leastsq # Ввести функцию наименьших квадратов
 
n = 9 # степень полинома
 
 
 # Целевая функция
def real_func(x):
    return np.sin(2 * np.pi * x)
 
 
 # Полиномиальная функция
def fit_func(p, x):
    f = np.poly1d(p)
    return f(x)
 
 
 # Остаточная функция
def residuals_func(p, y, x):
    ret = fit_func(p, x) - y
    return ret
 
 
x = np.linspace (0, 1, 9) # случайным образом выбираем 9 точек как x
x_points = np.linspace (0, 1, 1000) # Последовательные точки, необходимые для рисования
 
y0 = real_func (x) # целевая функция
y1 = [np.random.normal (0, 0.1) + y for y in y0] # Функция после добавления шума нормального распределения
 
p_init = np.random.randn (n) # Инициализировать параметры полинома случайным образом
 
plsq = leastsq(residuals_func, p_init, args=(y1, x))
 
print ('Fitting Parameters: ', plsq [0]) # Вывести параметры подгонки
 
pl.plot(x_points, real_func(x_points), label='real')
pl.plot(x_points, fit_func(plsq[0], x_points), label='fitted curve')
pl.plot(x, y1, 'bo', label='with noise')
pl.legend()
pl.show()