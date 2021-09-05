import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque
import random

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

x = deque(maxlen=50)
y = deque(maxlen=50)
line, = ax1.plot(x, y)
plt.xlabel('Value')
plt.ylabel('Time')
plt.title('Live Graph')

def animate(frame, x, y):
    x.append(x[-1] + 1 if len(y) > 0 else 1)
    y.append(y[-1] + random.randint(-5, 5) if len(y) > 0 else 0)
    line.set_xdata(x)
    line.set_ydata(y)
    ax1.set_xlim(min(x)-1, max(x)+1)
    ax1.set_ylim(min(y)-1, max(y)+1)
    ax1.set_xticks(list(range(min(x), max(x)+1)))
    return line


ani = animation.FuncAnimation(fig, animate, fargs=(x, y), interval=2000)
plt.show()
