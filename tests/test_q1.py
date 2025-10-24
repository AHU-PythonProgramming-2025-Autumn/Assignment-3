from src.q1_number_classify import classify


def test_q1_number_classify_task_1():
    assert classify(-10) == "Even"


def test_q1_number_classify_task_2():
    assert classify(0) == "Even"


def test_q1_number_classify_task_3():
    assert classify(10) == "Even"


def test_q1_number_classify_task_4():
    assert classify(9) == "Odd and multiple of 3"


def test_q1_number_classify_task_5():
    assert classify(27) == "Odd and multiple of 3"


def test_q1_number_classify_task_6():
    assert classify(17) == "Odd"


def test_q1_number_classify_task_7():
    assert classify(59) == "Odd"


def test_q1_number_classify_task_8():
    assert classify(91) == "Odd"


def test_q1_number_classify_task_9():
    assert classify(103) == "Odd"


def test_q1_number_classify_task_10():
    assert classify(-107) == "Odd"
