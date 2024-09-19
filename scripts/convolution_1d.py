import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def rect(x):
    return 1.0 * ((x >= -0.5) * (x < 0.5))


def exp(x, a=1):
    return a * np.exp(-a * x) * (x > 0)


if __name__ == "__main__":
    y, dy = np.linspace(-2.5, 6, 1000, retstep=True)

    f = exp
    # g = rect
    g = exp

    x_arr = np.linspace(-1, 5, 200)

    def _update_animation(i):
        fg = f(y) * g(x_arr[i] - y)
        h[i] = fg.sum() * dy
        l1[0].set_ydata(g(x_arr[i] - y))
        ax[1, 1].clear()
        l2 = ax[1, 1].plot(y, fg)
        l3 = ax[1, 1].fill_between(y, fg, alpha=0.5)
        ax[1, 1].set_ylim(0, 1.05)
        ax[1, 1].set_xlabel("y")

        ax[1, 2].clear()
        l4 = ax[1, 2].plot(x_arr[: (i + 1)], h[: (i + 1)])
        ax[1, 2].set_ylim(0, 1.05)
        ax[1, 2].set_xlim(y.min(), y.max())
        ax[1, 2].set_xlabel("x")

        ax[1, 0].set_title(f"f(y), g(x={x_arr[i]:.2f}-y)")
        ax[1, 1].set_title(f"f(y)g(x={x_arr[i]:.2f}-y)")
        ax[1, 2].set_title(r"$f(x) \ast g(x)$")

        return (l1, l2)

    fig, ax = plt.subplots(2, 3, figsize=(9, 6), tight_layout=True)

    ax[0, 0].plot(y, f(y))
    ax[0, 1].plot(y, g(y))
    ax[1, 0].plot(y, f(y))

    i = 0
    x = x_arr[i]
    h = np.zeros(x_arr.size)
    fg = f(y) * g(x - y)
    h[i] = fg.sum() * dy
    l1 = ax[1, 0].plot(y, g(x - y))
    l2 = ax[1, 1].plot(y, fg)
    l3 = ax[1, 1].fill_between(y, fg, alpha=0.5)
    l4 = ax[1, 2].plot(x_arr[: (i + 1)], h[: (i + 1)])

    for axx in ax.ravel():
        axx.set_xlim(y.min(), y.max())
        axx.set_ylim(0, 1.05)

    ax[0, 0].set_title("f(x)")
    ax[0, 1].set_title("g(x)")
    ax[0, 2].set_axis_off()

    ax[1, 0].set_title(f"f(y), g(x={x_arr[i]:.2f}-y)")
    ax[1, 1].set_title(f"f(y)g(x={x_arr[i]:.2f}-y)")
    ax[1, 2].set_title(r"$f(x) \ast g(x)$")

    ax[0, 0].set_xlabel("x")
    ax[0, 1].set_xlabel("x")
    ax[1, 0].set_xlabel("y")
    ax[1, 1].set_xlabel("y")
    ax[1, 2].set_xlabel("x")

    ani = animation.FuncAnimation(
        fig, _update_animation, x_arr.size, interval=5, blit=False, repeat=False
    )

    ani.save("../figs/convolution.mp4", writer=animation.FFMpegWriter(fps=20))
    fig.show()
