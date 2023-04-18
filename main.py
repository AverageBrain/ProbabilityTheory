import itertools
import math
import random

NUMBER_EXPERIMENTS = 100000


def expected_task_1(n: float, r: float):
    return (n ** (2 * (2 ** r - 1))) / ((n + 1) ** (2 * (2 ** r - 1)))


def task_1(): #wrong
    rs = [1, 3, 5, 7, 10, 12]
    ns = [100, 1000, 10000]
    for n, r in itertools.product(ns, rs):
        cnt = 0
        for _ in range(NUMBER_EXPERIMENTS):
            was_pr = False
            for _ in range(2 ** (r + 1)):
                if random.randint(0, n) == 0:
                    was_pr = True
                    break
            if was_pr:
                cnt += 1
        print(f'n={n} | r={r} | {1 - cnt / NUMBER_EXPERIMENTS} | expected {expected_task_1(n, r)}')


def expected_task_2(n: int):
    return math.tan(math.pi / n) * math.tan(math.pi / 2 / n)


def dist_line_point(A: float, B: float, x: float, y: float):  # line: x/A + y/B = 1
    return math.fabs(1 / A * x + 1 / B * y - 1) / math.sqrt(1 / A ** 2 + 1 / B ** 2)


def triangle_n(n: int):
    cnt = 0
    for _ in range(NUMBER_EXPERIMENTS):
        x_point = random.random()
        max_y_point = (1 - x_point) / math.tan(math.pi / n)
        y_point = random.random() * max_y_point
        if y_point < dist_line_point(1, math.tan(math.pi / n), x_point, y_point):
            cnt += 1
    return cnt / NUMBER_EXPERIMENTS


def task_2():
    # generation random point in a triangle with angle pi/n
    for n in range(3, 20):
        print(f'n={n}: {triangle_n(n)} | expected={expected_task_2(n)}')


def expected_task_3(n: math, p: math, m: math, k: math):
    return math.comb(n, k) * math.comb(n, m - k) / math.comb(2 * n, m)


def task_3_extra():
    ns = [10]
    ps = [0.001, 0.01, 0.1, 0.25, 0.5]
    for n in ns:
        for p in ps:
            table = [[0] * 2 * n for _ in range(2 * n + 1)]
            sum_str = [0] * 2 * n
            for _ in range(NUMBER_EXPERIMENTS):
                cnt = [0, 0]
                for i in range(2):
                    for _ in range(n):
                        if random.random() < p:
                            cnt[i] += 1
                table[cnt[0] + cnt[1]][cnt[0]] += 1
                sum_str[cnt[0] + cnt[1]] += 1
            for i in range(n):
                for j in range(i + 1):
                    prob = None
                    if sum_str[i] != 0:
                        prob = table[i][j] / sum_str[i]
                    print(f'n = {n}, p = {p}, P(S₁={j}|S₁+S₂={i}) = {prob} | expected = {expected_task_3(n, p, i, j)}')


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
    # task_1()
    # task_2()
    task_3()
