---
title: Appendix - demo plots
---

# Filtered backprojection

```{code-cell} python
:tag: remove-output
import array_api_compat.numpy as np
import matplotlib.pyplot as plt
from utils import demo_phantom_and_projector
```

```{code-cell} python
# choose number of radial elements, number of views and angular coverage
num_rad = 301
phi_max = np.pi
num_phi = (int(0.5 * num_rad * np.pi * (phi_max / np.pi)) + 1) // 1
```

```{code-cell} python
# setup 1D arrays containing the radial and angular coordinates
r = np.linspace(-30, 30, num_rad, dtype=np.float32)
phi = np.linspace(0, phi_max, num_phi, endpoint=False, dtype=np.float32)

# get: - a demo radon object (an test image where we can calculate the radon transform analytically)
#      - a sinogram (discrete radon transform) of the object
#      - get a projector (line integral calculator) that allows us to reconstruct
radon_object, sino, proj = demo_phantom_and_projector(r, phi)
```

```{code-cell} python
# back project the sinogram
# the back projection is the adjoint of the forward projection
back_proj = proj.adjoint(sino)
```

```{code-cell} python
# setup a discrete ramp filter
n_filter = r.shape[0]
r_shift = np.arange(n_filter, dtype=np.float64) - n_filter // 2
f = np.zeros(n_filter, dtype=np.float64)
f[r_shift != 0] = -1 / (np.pi**2 * r_shift[r_shift != 0] ** 2)
f[(r_shift % 2) == 0] = 0
f[r_shift == 0] = 0.25
```

```{code-cell} python
# visualize the dicretized ramp filter
figr, axr = plt.subplots(1, 2, figsize = (9,4.5))
axr[0].plot(np.arange(num_rad) - num_rad//2, f)
axr[1].plot(np.arange(num_rad) - num_rad//2, f, ".-")
axr[1].set_xlim(-6,6)
axr[0].set_title("discretized ramp filter", fontsize = "small")
axr[1].set_title("discretized ramp filter (zoom)", fontsize = "small")
axr[0].grid(ls=':')
axr[1].grid(ls=':')
```

```{code-cell} python
# ramp filter the sinogram in the radial direction - view by view
filtered_sino = np.zeros_like(sino)

for i in range(num_phi):
    filtered_sino[:, i] = np.convolve(sino[:, i], f, mode="same")
```

```{code-cell} python
# back project the ramp filtered sinogram
filtered_back_proj = proj.adjoint(filtered_sino)
```


```{code-cell} python
# visualize images

# generate a high-resolution discrete ground truth image
x = np.linspace(float(np.min(r)), float(np.max(r)), 1001, dtype=np.float32)
X0hr, X1hr = np.meshgrid(x, x, indexing="ij")
high_res_ground_truth = radon_object.values(X0hr, X1hr)

ext_img = [float(np.min(r)), float(np.max(r)), float(np.min(r)), float(np.max(r))]
ext_sino = [float(np.min(r)), float(np.max(r)), float(np.min(phi)), float(np.max(phi))]

fig, ax = plt.subplots(2, 3, figsize=(9, 6), tight_layout=True)
ax[0, 0].imshow(
    high_res_ground_truth.T,
    cmap="Greys",
    extent=ext_img,
    origin="lower",
)

ax[1, 1].imshow(
    sino.T,
    cmap="Greys",
    aspect=20,
    extent=ext_sino,
    origin="lower",
)

ax[1, 2].imshow(
    filtered_sino.T,
    cmap="Greys",
    aspect=20,
    extent=ext_sino,
    origin="lower",
)

ax[0, 1].imshow(
    back_proj.T,
    cmap="Greys",
    extent=ext_img,
    origin="lower",
)

ax[0, 2].imshow(
    filtered_back_proj.T,
    cmap="Greys",
    extent=ext_img,
    origin="lower",
)

for axx in ax[0, :].ravel():
    axx.set_xlabel(r"$x_0$")
    axx.set_ylabel(r"$x_1$")
for axx in ax[1, 1:].ravel():
    axx.set_xlabel(r"$s$")
    axx.set_ylabel(r"$\phi$")

ax[1, 0].set_axis_off()

ax[0, 0].set_title("object", fontsize="small")
ax[0, 1].set_title("back projection of sinogram", fontsize="small")
ax[0, 2].set_title("filtered back projection of sinogram", fontsize="small")

ax[1, 1].set_title("radon transform of object - sinogram", fontsize="small")
ax[1, 2].set_title("ramp filtered sinogram", fontsize="small")
```


# Demo animated plot

```{code-cell}python
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import HTML
import matplotlib.animation as animation

t = np.linspace(0, 3, 40)
g = -9.81
v0 = 12
z = g * t**2 / 2 + v0 * t
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