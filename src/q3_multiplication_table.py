def table_lines() -> list[str]:
    # 返回9行字符串列表，每行形如 "1*3=3\t2*3=6\t3*3=9"。（九九乘法表）
    ...


if __name__ == "__main__":
    for line in table_lines():
        print(line)
