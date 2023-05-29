import random
import time

import scipy.stats as ss
import scipy.special as ssp
import numpy as np
import math
from decimal import Decimal
from utils.util import dec_pow, hist_plot, hist_plot4
import matplotlib.pyplot as plt


def density(x):
    pwd = - dec_pow(Decimal(5) - dec_pow(x, 5), 2) / Decimal(2)
    exp = Decimal.exp(pwd)
    return Decimal(5) * dec_pow(x, 4) / Decimal.sqrt(2 * Decimal(math.pi)) * exp


class MyDistribution(ss.rv_continuous):
    def __init__(self):
        super().__init__(momtype=0, a=1, b=2)

    def _pdf(self, x, *args):
        return density(x)


def method_1(count_points=100):
    my = MyDistribution()
    rng = np.random.SeedSequence().entropy % (2 ** 32)
    return my.rvs(size=count_points, random_state=rng)


def method_2(count_points=100):
    def gen():
        rnd = random.uniform(0, 1)
        return (ssp.erfinv(2 * (rnd - 0.5)) * math.sqrt(2) + 5) ** (1 / 5)

    return [gen() for _ in range(count_points)]


def method_3(count_points=100):
    c = 10

    def approx(x):
        sigma = 0.2
        return 1 / math.sqrt(sigma * 2 * math.pi) * math.exp(- (x - 1.4) ** 2 / 2 / sigma ** 2)

    def gen():
        while True:
            x = random.normalvariate(1.4, 0.2)
            u = random.uniform(0, c * approx(x))
            if u <= density(x):
                return x

    def graph():
        xs = np.linspace(0.5, 2, 10000)
        plt.plot(xs, [approx(x) for x in xs], label=f'N[{1.4}, {0.2}^2]', color='thistle')
        plt.plot(xs, [density(x) for x in xs], label='density', color='orange')
        plt.plot(xs, [c * approx(x) for x in xs], label=f'c N[{1.4}, {0.2}^2]', color='slateblue')
        plt.legend()
        plt.savefig(f'img/approx.png')
        plt.show()

    # graph()
    return [gen() for _ in range(count_points)]


methods = [
    {'method': method_1, 'title': 'rv_continuous', 'color': 'khaki'},
    {'method': method_2, 'title': 'inverse function', 'color': 'orchid'},
    {'method': method_3, 'title': 'rejecting sampling', 'color': 'coral'}
]

counts = [100, 400, 1000, 10000]


def task3():
    for count in counts:
        for method in methods:
            start = time.time()
            points = method['method'](count_points=count)
            t = time.time() - start
            print(f'Method: {method["title"]}, with count: {count} time: {t}')
            hist_plot(points, density, title=f'{method["title"]}', clr=method['color'], postfix=f'{count}')


def plotting():
    for method in methods:
        points = []
        for count in counts:
            points.append(method['method'](count_points=count))
        hist_plot4(points, density, title=f'{method["title"]}', clr=method['color'])


if __name__ == '__main__':
    task3()
    # plotting()
