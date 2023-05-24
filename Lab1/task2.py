import math
import random

NUMBER_EXPERIMENTS = 10000


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


if __name__ == '__main__':
    task_2()
