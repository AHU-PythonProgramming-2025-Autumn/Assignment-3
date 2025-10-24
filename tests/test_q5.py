from src.q5_quadratic_solver import solve_quadratic


def test_two_real_roots():
    # x^2 - 3x + 2 = 0  -> x = 1, 2
    assert solve_quadratic(1, -3, 2) == [1.0, 2.0]


def test_one_real_root():
    # x^2 + 2x + 1 = 0 -> x = -1
    assert solve_quadratic(1, 2, 1) == [-1.0]


def test_no_real_roots():
    # x^2 + x + 1 = 0 -> 无实根
    assert solve_quadratic(1, 1, 1) == "No real roots"


def test_float_coefficients():
    # 0.5x^2 - 3x + 2 = 0 -> roots ≈ [0.7, 5.3]
    result = solve_quadratic(0.5, -3, 2)
    assert all(isinstance(x, float) for x in result)
    assert result[0] < result[1]


def test_non_quadratic_behavior():
    # 虽然不要求处理 a=0，但如果出现，程序应避免崩溃
    result = solve_quadratic(0, 2, 1)
    pass
