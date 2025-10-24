def special_sum(n: int) -> int:
    # 1..n 中 (被3或5整除) 且 (不是同时被两者整除) 的和
    ...


if __name__ == "__main__":
    n = int(input().strip())
    print(special_sum(n))
