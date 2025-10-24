from src.q3_multiplication_table import table_lines


def test_lines_count_and_content():
    lines = table_lines()
    assert isinstance(lines, list)
    assert len(lines) == 9

    # 第 3 行（i=3）
    assert lines[2] == "1*3=3\t2*3=6\t3*3=9"

    # 最后一行（i=9）应以 9*9=81 结尾
    assert lines[-1].endswith("9*9=81")
