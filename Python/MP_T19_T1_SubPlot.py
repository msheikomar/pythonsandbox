import random
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.pyplot import figure

figure(num=None, figsize=(60, 6), dpi=80, facecolor='#000006', edgecolor='r')

style.use('fivethirtyeight')
fig = plt.figure()


# print(plt.style.available)
def creat_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys


ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

x, y = creat_plots()
ax1.plot(x, y)

x, y = creat_plots()
ax2.plot(x, y)

plt.show() 