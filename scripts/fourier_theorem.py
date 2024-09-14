# script to visualize the fourier slice theorem

import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage import map_coordinates
from utils import demo_radon_object


def interpolate_along_line(image, alpha):

    n = image.shape[0]

    # Image shape and center
    center_x, center_y = n // 2, n // 2

    # Calculate the start and end points of the line
    r = min(center_x, center_y)  # Half diagonal length for line bounds

    # Start point (extending from center)
    start_x = center_x - r * np.cos(alpha)
    start_y = center_y + r * np.sin(alpha)

    # End point (extending to the other side of the center)
    end_x = center_x + r * np.cos(alpha)
    end_y = center_y - r * np.sin(alpha)

    # Create linearly spaced points along the line
    x_coords = np.linspace(start_x, end_x, n)
    y_coords = np.linspace(start_y, end_y, n)

    # Interpolate values along the line
    interpolated_values = map_coordinates(image, [y_coords, x_coords], order=1)

    return interpolated_values


dev = "cpu"

num_rad = 511

radon_obj = demo_radon_object()

s_arr, ds = np.linspace(-30, 30, num_rad, retstep=True)
theta_arr = np.array([0.0, 25.0, 50.0, 75.0]) * np.pi / 180

img = radon_obj.values(*np.meshgrid(s_arr, s_arr)) * ds

radon_transform = radon_obj.radon_transform(*np.meshgrid(s_arr, theta_arr))

nu = np.fft.fftshift(np.fft.fftfreq(num_rad, d=ds))
img_ft2d = np.fft.fftshift(np.fft.fft2(img))

for i, theta in enumerate(theta_arr):
    p = radon_transform[i, :]
    kspace_line = interpolate_along_line(img_ft2d, theta)

    fig, ax = plt.subplots(1, 4, figsize=(12, 3), tight_layout=True)
    ax[0].imshow(
        img,
        cmap="Greys",
        extent=[s_arr.min(), s_arr.max(), s_arr.min(), s_arr.max()],
        aspect="equal",
    )
    ax[0].plot(s_arr * np.cos(theta), s_arr * np.sin(theta), "r:")

    ax[1].plot(s_arr, p)
    ax[1].set_ylim(0, 1.1 * radon_transform.max())
    p_ft1d = np.fft.fftshift(np.fft.fft(p))

    ax[2].imshow(
        np.log(np.abs(img_ft2d)),
        cmap="Greys",
        extent=[nu.min(), nu.max(), nu.min(), nu.max()],
    )
    ax[2].plot(
        nu * np.cos(theta),
        nu * np.sin(theta),
        "r:",
    )

    ax[3].semilogy(nu, np.abs(p_ft1d), label=r"$\hat{p}_\theta(\nu)$")
    ax[3].semilogy(
        nu, np.abs(kspace_line), ":", label=r"$\hat{f}(\cos\theta \nu, \sin\theta \nu)$"
    )
    ax[3].set_ylim(1e-3, 2 * np.abs(img_ft2d).max())

    ax[0].set_xlabel(r"$x$")
    ax[0].set_ylabel(r"$y$")

    ax[1].set_xlabel(r"$s$")

    ax[2].set_xlabel(r"$\nu_x$")
    ax[2].set_ylabel(r"$\nu_y$")

    ax[3].set_xlabel(r"$\nu$")

    arr = []
    ann = []
    L = 15.0

    for s in np.linspace(0.7 * s_arr.min(), 0.7 * s_arr.max(), 5):
        ax[1].axvline(s, color="r", lw=0.5)
        d0 = s * np.cos(theta)
        d1 = s * np.sin(theta)
        arr.append(
            ax[0].arrow(
                L * np.sin(theta) + d0,
                -L * np.cos(theta) + d1,
                -2 * L * np.sin(theta),
                2 * L * np.cos(theta),
                color="r",
                width=0.01,
                head_width=1.0,
            )
        )

        ann.append(
            ax[0].annotate(
                f"{s:.1f}",
                (
                    1.2 * L * np.sin(theta) + d0,
                    -1.2 * L * np.cos(theta) + d1,
                ),
                color="r",
                fontsize="small",
                ha="center",
                va="center",
                annotation_clip=True,
            )
        )

    ax[0].set_title(r"image $f(x,y)$", fontsize="medium")
    ax[1].set_title(r"projection profile $p_\theta(s)$", fontsize="medium")
    ax[2].set_title(r"2D FT of image $\hat{f}(\nu_x,\nu_y)$", fontsize="medium")

    ax[3].legend(fontsize="small", ncols=2)

    fig.savefig(f"fourier_slice_theorem_{i}.png")
    fig.show()
