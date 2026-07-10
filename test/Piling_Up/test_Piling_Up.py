from src.Piling_Up.util import can_stack


def test_can_stack_yes():
    assert can_stack([4, 3, 2, 1, 3, 4]) == "Yes"


def test_can_stack_no():
    assert can_stack([1, 3, 2]) == "No"