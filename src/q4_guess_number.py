import os, random


def decide_target() -> int:
    t = int(os.getenv("TARGET", "0"))
    return t if t else random.randint(1, 100)


def play(input_fn=input, print_fn=print):
    target = decide_target()
    tries = 0
    # TODO: 完成猜数字的循环逻辑
    ...


if __name__ == "__main__":
    play()
