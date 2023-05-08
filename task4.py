from utils.util import *

import math
import itertools
from statistics import NormalDist


def accurate_result(n, p):
    q = (1 - p)
    left_bound = math.ceil(n / 2 - math.sqrt(n * p * q))
    right_bound = math.floor(n / 2 + math.sqrt(n * p * q))
    prob = Decimal(0)
    for i in range(left_bound, right_bound + 1):
        prob += dec_comb(n, i) * Decimal(p) ** i * Decimal(q) ** (n - i)
    return prob


def approximate_result(n, p):
    c = (math.sqrt(n) * (1 - 2 * p)) / (2 * math.sqrt(p * (1 - p)))
    x1 = c - 1
    x2 = c + 1
    return NormalDist().cdf(x2) - NormalDist().cdf(x1)


def task_4():
    ns = [10, 100, 1000, 10000]
    ps = [0.001, 0.01, 0.1, 0.25, 0.5]
    for n, p in itertools.product(ns, ps):
        acc = accurate_result(n, p)
        app = approximate_result(n, p)
        print(f'n={n}, p={p}')
        print(f'Is npq > 10? {n * p * (1 - p) > 10}')
        print(f'Expected={acc} | Approximate={app}')
        err = abs(acc - Decimal(app))
        print(f'Error: {err}')
        print()


if __name__ == '__main__':
    task_4()
