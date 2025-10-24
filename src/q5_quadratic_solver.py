import math


def solve_quadratic(a: float, b: float, c: float):
    # TODO: 返回实根列表或 'No real roots'
    ...


if __name__ == "__main__":
    a, b, c = map(float, input().split())
    result = solve_quadratic(a, b, c)
    if isinstance(result, str):
        print(result)
    else:
        print(*result)
