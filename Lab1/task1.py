from utils.util import *
import random

NUMBER_EXPERIMENTS = 10000


def stirling(n, k):
    if k > n:
        return 0
    res = Decimal(0)
    for i in range(k):
        res += dec_pow(-1, i) * dec_comb(k, i) * dec_pow(k - i, n)
    return res


def expected_task_1(n: int, r: int):
    dp = [[Decimal(0)] * (n + 1) for _ in range(r + 1)]
    dp[0][1] = Decimal(1)
    for k in range(1, r + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dp[k][i] += dp[k - 1][j] / dec_pow(n * (n + 1), j) * stirling(2 * j, i)
            dp[k][i] *= dec_comb(n, i)
    return [sum(dp[k]) for k in range(r + 1)]


def experiments(cur_n: int, n: int, cur_r: int, r: int):
    if cur_r == r:
        return 1
    people = set()
    for i in range(cur_n):
        first = random.randint(0, n)
        second = random.randint(0, n)
        people.add(first)
        people.add(second)
        if first == 0 or second == 0:
            return 0
    return experiments(len(people), n, cur_r + 1, r)


def task_1():
    rs = [1, 3, 5, 7, 8, 10, 12]
    ns = [10, 50, 100]
    for n in ns:
        anss_for_n = expected_task_1(n, max(rs))
        for r in rs:
            cnt = 0
            for _ in range(NUMBER_EXPERIMENTS):
                cnt += experiments(1, n, 0, r)
            print(f'n={n} | r={r} | {cnt / NUMBER_EXPERIMENTS} | exp={anss_for_n[r]}')


if __name__ == '__main__':
    task_1()
