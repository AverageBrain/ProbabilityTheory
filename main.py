import itertools
import math
import random
from statistics import NormalDist
from decimal import Decimal
NUMBER_EXPERIMENTS = 10000


def expected_task_1(n: int, r: int):
    dp = [[0] * 2 ** (r + 1) for _ in range(r + 1)]
    dp[0][1] = 1
    for i in range(1, r + 1):
        for j in range(1, 2 ** i):
            for k in range(1, 2 * j + 1):
                if n - j > 0 and 2 * k >= j:
                    dp[i][j] += dp[i - 1][k] * (n - j + 1) / (n + 1)
    return sum(dp[r])


def experiments(cur_n: int, n: int, cur_r: int, r: int):
    if cur_r == r + 1:
        return 1
    people = set()
    for i in range(cur_n):
        first = random.randint(0, n)
        second = random.randint(0, n)
        while first == second:
            second = random.randint(0, n)
        people.add(first)
        people.add(second)
        if first == 0 or second == 0:
            return 0
    return experiments(len(people), n, cur_r + 1, r)


def task_1():
    rs = [1, 3, 5, 7, 10, 12]
    ns = [100, 1000, 10000]
    for n, r in itertools.product(ns, rs):
        cnt = 0
        for _ in range(NUMBER_EXPERIMENTS):
            if experiments(1, n, 0, r):
               cnt += 1
        print(f'n={n} | r={r} | {cnt / NUMBER_EXPERIMENTS} | exp={expected_task_1(n, r)}')


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


def dec_factorial(n: int):
    res = Decimal(1)
    for i in range(1, n + 1):
        res = res * Decimal(i)
    return res


def dec_comb(n, k):
    return (dec_factorial(n) / dec_factorial(k)) / dec_factorial(n - k)


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
    task_1()
    # task_2()
    # task_3()
    # task_4()
