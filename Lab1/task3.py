import math
import random
import itertools

NUMBER_EXPERIMENTS = 10000


def expected_task_3(n: math, p: math, m: math, k: math):
    return math.comb(n, k) * math.comb(n, m - k) / math.comb(2 * n, m)


def task_3():
    ns = [10]
    ps = [0.001, 0.1, 0.5]
    ms = [1, 3, 5, 10, 15, 20]
    for n, p, m in itertools.product(ns, ps, ms):
        a = [1] * m + [0] * (2 * n - m)
        success = [0] * 2 * n
        for _ in range(NUMBER_EXPERIMENTS):
            random.shuffle(a)
            cnt = sum(a[i] for i in range(n))
            success[cnt] += 1
        for k in range(m):
            print(f'n={n}, p={p}, m={m} P(S₁={k}|S₁+S₂={m}) = {success[k] / NUMBER_EXPERIMENTS} '
                  f'| expected = {expected_task_3(n, p, m, k)}')


if __name__ == '__main__':
    task_3()
