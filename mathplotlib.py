# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 15:00:42 2020

@author: TN90072

https://matplotlib.org/3.3.2/gallery/index.html
https://habr.com/ru/post/468295/
https://python-graph-gallery.com/matplotlib/

"""
import matplotlib.pyplot as plt
import numpy as np
# Generate a sequence of numbers from 0 to 10 with 50 steps in between
x = np.linspace(0, 10, 50)
y = x
# Построение графика
plt.title("Линейная зависимость y = x") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x, y)  # построение графика

plt.show()

#%%
# 2 линии на одной диаграмме

#Линейная зависимость
x = np.linspace(0, 10, 50)
y1 = x
# Квадратичная зависимость
y2 = [i**2 for i in x]
# Построение графика
plt.title("Зависимости: y1 = x, y2 = x^2") # заголовок
plt.xlabel("x")         # ось абсцисс"
plt.ylabel("y1, y2")    # ось ординат"
plt.grid()              # включение отображение сетки
plt.plot(x, y1, x, y2)  # построение графика"

#%%
# 3 диаграммы

 # Линейная зависимость
x = np.linspace(0, 10, 50)
y1 = x
# Квадратичная зависимость
y2 = [i**2 for i in x]
# Кубическая зависимость
y3 = [i**3 for i in x]
# Построение графиков
plt.figure(figsize=(9, 9))
plt.subplot(3, 1, 1)
plt.plot(x, y1)               # построение графика
plt.title("Зависимости: y1 = x, y2 = x^2") # заголовок
plt.ylabel("y1", fontsize=14) # ось ординат
plt.grid(True)                # включение отображение сетки
plt.subplot(3, 1, 2)
plt.plot(x, y2)               # построение графика
plt.xlabel("x", fontsize=14)  # ось абсцисс
plt.ylabel("y2", fontsize=14) # ось ординат
plt.grid(True)                # включение отображение сетки
plt.subplot(3, 1, 3),
plt.plot(x, y3)               # построение графика
plt.xlabel("x", fontsize=14)  # ось абсцисс,
plt.ylabel("y3", fontsize=14) # ось ординат
plt.grid(True)                # включение отображение сетки"

#%%
# синусоида

import math
x = np.linspace(0, 10, 500)

#https://www.mathsisfun.com/algebra/amplitude-period-frequency-phase-shift.html
A = 1
B = 1
C = 0
D = 0

#    amplitude is A
#    period is 2π/B
#    phase shift is C (positive is to the left)
#    vertical shift is D

y = [A * math.sin(B * (i + C)) + D for i in x]

plt.title("Зависимость: Синусоида") # заголовок
plt.xlabel("x")         # ось абсцисс
plt.ylabel("y")    # ось ординат
plt.grid()              # включение отображение сетки
plt.plot(x, y)  # построение графика"
plt.savefig("sine.png")

#%%
# гипербола

x1 = np.linspace(-10, 0, 50)
x2 = np.linspace(0, 10, 50)
x1 = np.delete(x1, 0)
x2 = np.delete(x2, 0)

k = 1

# Квадратичная зависимость
y1 = [k/i for i in x1]
y2 = [k/i for i in x2]

# Построение графика
plt.title("Зависимость y = 1/x") # заголовок
plt.xlabel("x")         # ось абсцисс",
plt.ylabel("y")    # ось ординат",
plt.grid()              # включение отображение сетки
plt.plot(x1, y1, x2, y2)  # построение графика"

#%%

# парабола

x = np.linspace(-5, 5, 50)

a = 1 # расхождение
b = 2 # смещение x ??????? не работает
c = 0 # смещение y

# Квадратичная зависимость
y1 = [a*((i**2)-b)+c for i in x]
y2 = [a*((i**3)-b)+c for i in x]

# Построение графика
plt.title("Парабола") # заголовок
plt.xlabel("x")         # ось абсцисс
plt.ylabel("y")    # ось ординат",
plt.grid()              # включение отображение сетки
plt.ylim(-5, 5)     # set the ylim to bottom, top
plt.plot(x, y1, x, y2)  # построение графика

#%%
x = np.random.random_sample(size=5000) 
y = np.random.random_sample(size=5000)

# Построение графика
plt.title("Случайный массив") # заголовок
plt.xlabel("x")         # ось абсцисс
plt.ylabel("y")    # ось ординат
plt.grid()              # включение отображение сетки
plt.plot(x, y, 'o', color='black', markersize = 0.7)

#%%
rng = np.random.RandomState(0)
for marker in ['o', '.', ',', 'x', '+', 'v', '^', '<', '>', 's', 'd']:
    plt.plot(rng.rand(5), rng.rand(5), marker,
             label="marker='{0}'".format(marker))
plt.legend(numpoints=1)
plt.xlim(0, 1.8)

#%%
from sklearn.datasets import load_iris
iris = load_iris()
features = iris.data.T

plt.scatter(features[0], features[1], alpha=0.2,
            s=100*features[3], c=iris.target, cmap='viridis')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])

#%%
# https://www.freecodecamp.org/news/how-to-embed-interactive-python-visualizations-on-your-website-with-python-and-matplotlib/
# синусоида с управлением

import math
x = np.linspace(0, 10, 500)

#https://www.mathsisfun.com/algebra/amplitude-period-frequency-phase-shift.html
A = 1
B = 1
C = 0
D = 0

#    amplitude is A
#    period is 2π/B
#    phase shift is C (positive is to the left)
#    vertical shift is D

y = [A * math.sin(B * (i + C)) + D for i in x]

plt.title("Зависимость: Синусоида") # заголовок
plt.xlabel("x")         # ось абсцисс
plt.ylabel("y")    # ось ординат
plt.grid()              # включение отображение сетки
plt.plot(x, y)  # построение графика"
plt.savefig("sine.png")

#%%
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, ax = plt.subplots()
plt.subplots_adjust(left=0.25, bottom=0.25)
t = np.arange(0.0, 1.0, 0.001)
a0 = 5
f0 = 3
delta_f = 5.0
s = a0 * np.sin(2 * np.pi * f0 * t)
l, = plt.plot(t, s, lw=2)
ax.margins(x=0)

axcolor = 'lightgoldenrodyellow'
axfreq = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
axamp = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 30.0, valinit=f0, valstep=delta_f)
samp = Slider(axamp, 'Amp', 0.1, 10.0, valinit=a0)


def update(val):
    amp = samp.val
    freq = sfreq.val
    l.set_ydata(amp*np.sin(2*np.pi*freq*t))
    fig.canvas.draw_idle()


sfreq.on_changed(update)
samp.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axcolor, hovercolor='0.975')


def reset(event):
    sfreq.reset()
    samp.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axcolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)


def colorfunc(label):
    l.set_color(label)
    fig.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()

#%%
def mandelbrot(n_rows, n_columns, iterations):
    x_cor = np.linspace(-2,1,n_rows)
    y_cor = np.linspace(-2,1,n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    for i in range(x_len):
        for j in range(y_len):
            c = complex(x_cor[i],y_cor[j])
            z = complex(0, 0)
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
            print((i/x_len)*100,"% completed")
    print(output)
    plt.imshow(output.T, cmap = "hot")
    plt.axis("off")
    plt.show()
mandelbrot(1000,1000,150)
            
#%%
def mandelbrot(n_rows, n_columns, iterations, cx, cy):
    x_cor = np.linspace(-2, 2, n_rows)
    y_cor = np.linspace(-2, 2, n_columns)
    x_len = len(x_cor)
    y_len = len(y_cor)
    output = np.zeros((x_len,y_len))
    c = complex(cx, cy)
    for i in range(x_len):
        for j in range(y_len):
            z = complex(x_cor[i], y_cor[j])
            count = 0
            for k in range(iterations):
                z = (z * z) + c
                count = count + 1
                if (abs(z) > 4):
                    break
            output[i,j] = count
        print(int((i/x_len)*100),"% completed")
    print(output)
    plt.imshow(output.T, cmap='hot')
    plt.axis("off")
    plt.show()
mandelbrot(1000,1000,150,0.1,0.1)