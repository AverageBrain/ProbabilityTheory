import math
import typing

import numpy as np

NUMBER_EXPERIMENTS = 100

eps = 0.01
delta = 0.05
theta = 5  # value in [1, 5]
inv_lapalas = 1.96


def chebyshev():
    return 1 / eps ** 2 / delta / theta ** 2


def CLT():
    return (inv_lapalas / theta / eps) ** 2


def experiment(method: typing.Callable):
    cnt = 0
    for _ in range(NUMBER_EXPERIMENTS):
        n = math.ceil(method())
        values = np.random.exponential(scale=1 / theta, size=n)
        if math.fabs(sum(values) / n - 1 / theta) <= eps:
            cnt += 1
    return cnt


def task4():
    cnt_with_cond_chebyshev = experiment(chebyshev)
    cnt_with_cond_CLT = experiment(CLT)
    print(f'Chebyshev count: {cnt_with_cond_chebyshev}, fraction: {cnt_with_cond_chebyshev / NUMBER_EXPERIMENTS}')
    print(f'CLT count: {cnt_with_cond_CLT}, fraction: {cnt_with_cond_CLT / NUMBER_EXPERIMENTS}')


if __name__ == '__main__':
    task4()
