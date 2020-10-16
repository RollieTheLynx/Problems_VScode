# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:27:10 2020
@author: TN90072
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

graph, axes = plt.subplots() #Поле с графиком и поле со слайдерами
plt.subplots_adjust(left=0.25, bottom=0.4) #Tune the subplot layout.

t = np.linspace(0, 10, 500)

amp0 = 1
per0 = 1
phshift0 = 0
vershift0 = 0

y = amp0 * (np.sin(per0 * (t+phshift0)) + vershift0)
plt.title("Зависимость: Синусоида") # заголовок
plt.xlabel("Радианы")         # ось абсцисс
plt.ylabel("y")    # ось ординат
plt.grid()              # включение отображения сетки
l, = plt.plot(t, y, lw=2, color = 'red')  # lw = line width

axes.margins(x=0)

axescolor = 'Honeydew'
axfreq = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axescolor)
axamp = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axescolor)
axphshift = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axescolor)
axvershift = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axescolor)

sfreq = Slider(axfreq, 'Freq', 0.1, 10.0, valinit=per0)
samp = Slider(axamp, 'Amp', 0.1, 2.0, valinit=amp0)
sphshift = Slider(axphshift, 'Phase Shift', -10, 10.0, valinit=phshift0)
svershift = Slider(axvershift, 'Vertical Shift', -2, 2, valinit=vershift0)

def update(val):
    amp = samp.val
    per = sfreq.val
    phshift = sphshift.val
    vershift = svershift.val
    l.set_ydata(amp * (np.sin(per * (t+phshift)) + vershift))
    graph.canvas.draw_idle()

sfreq.on_changed(update)
samp.on_changed(update)
sphshift.on_changed(update)
svershift.on_changed(update)

resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = Button(resetax, 'Reset', color=axescolor, hovercolor='0.975')

def reset(event):
    sfreq.reset()
    samp.reset()
    sphshift.reset()
    svershift.reset()
button.on_clicked(reset)

rax = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=axescolor)
radio = RadioButtons(rax, ('red', 'blue', 'green'), active=0)

def colorfunc(label):
    l.set_color(label)
    graph.canvas.draw_idle()
radio.on_clicked(colorfunc)

plt.show()

# https://www.freecodecamp.org/news/how-to-embed-interactive-python-visualizations-on-your-website-with-python-and-matplotlib/
# html_str = mpld3.fig_to_html(fig)
# Html_file= open("graphs.html","w")
# Html_file.write(html_str)
# Html_file.close()