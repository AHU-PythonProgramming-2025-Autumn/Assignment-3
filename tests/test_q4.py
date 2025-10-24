import os
from src.q4_guess_number import play


def test_guess_game_with_injected_target(monkeypatch):
    # 通过环境变量指定目标数，便于可重复测试
    monkeypatch.setenv("TARGET", "62")

    # 依次输入 50, 75, 62
    inputs = iter(["50", "75", "62"])
    outputs = []

    def fake_input(prompt=""):
        outputs.append(prompt)  # 记录提示文本出现次数
        return next(inputs)

    def fake_print(*args, **kwargs):
        outputs.append(" ".join(map(str, args)))

    play(input_fn=fake_input, print_fn=fake_print)

    # 应包含 Too low -> Too high -> Congratulations
    assert any("Too low!" in s for s in outputs)
    assert any("Too high!" in s for s in outputs)
    ok_lines = [s for s in outputs if "Congratulations!" in s]
    assert ok_lines and "3 tries" in ok_lines[0]
