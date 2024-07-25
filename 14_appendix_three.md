---
title: Appendix - demo plots
---

# random plots

```{code-cell}python
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import HTML
import matplotlib.animation as animation

t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t

fig2, ax2 = plt.subplots()
ax2.plot(t,z)
ax2.grid(ls = ':')
ax2.set_xlabel('t')
ax2.set_ylabel('z')
```


```{code-cell}python
:tag: remove-output
v02 = 5
z2 = g * t**2 / 2 + v02 * t

fig, ax = plt.subplots()

scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
ax.legend()

def update(frame):
    # for each frame, update the data stored on each artist.
    x = t[:frame]
    y = z[:frame]
    # update the scatter plot:
    data = np.stack([x, y]).T
    scat.set_offsets(data)
    # update the line plot:
    line2.set_xdata(t[:frame])
    line2.set_ydata(z2[:frame])
    return (scat, line2)
```

```{code-cell}python
:tag:
ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
HTML(ani.to_jshtml())
```