from decimal import Decimal


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
