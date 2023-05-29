import itertools
import typing
import numpy as np
import matplotlib.pyplot as plt

from decimal import Decimal


def hist_plot(points, density: typing.Callable, title: str = '', postfix: str = '', clr='blue', l=1, r=1.6):
    xs = np.linspace(l, r, 100)
    fig = plt.figure(figsize=(19, 6), layout='tight')
    ax = fig.subplots(1, 1)
    ax.hist(points, bins=30, density=True, label=f'{title}', rwidth=0.9, color=clr)
    ax.plot(xs, [density(x) for x in xs], label='density(x)', color='black')
    ax.legend()
    plt.savefig(f'img/{title}{postfix}.svg')
    fig.show()


def hist_plot4(points, density: typing.Callable, title: str = '', clr='blue', l=1, r=1.6):
    xs = np.linspace(l, r, 100)
    fig = plt.figure(figsize=(19, 10), layout='tight')
    axs = fig.subplots(2, 2)
    for x, y in itertools.product(range(2), range(2)):
        items = points[2 * x + y]
        axs[x, y].hist(items, bins=30, density=True, label=f'{len(items)}', rwidth=0.9, color=clr)
        axs[x, y].plot(xs, [density(x) for x in xs], color='black')
        axs[x, y].legend()
    plt.suptitle(title)
    plt.savefig(f'img/{title}.svg')
    fig.show()


def dec_pow(n, k):
    if k <= 0:
        return Decimal(1)
    if k % 2 == 0:
        m = dec_pow(n, k / 2)
        return Decimal(m) * Decimal(m)
    else:
        return Decimal(n) * dec_pow(n, k - 1)


def dec_factorial(n: int):
    res = Decimal(1)
    for i in range(1, n + 1):
        res = res * Decimal(i)
    return res


def dec_comb(n, k):
    return (dec_factorial(n) / dec_factorial(k)) / dec_factorial(n - k)
