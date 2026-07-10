from src.Calendar.util import get_day_name
import pytest

def test_monday():
    assert get_day_name(7, 10, 2023) == "MONDAY"


def test_tuesday():
    assert get_day_name(7, 11, 2023) == "TUESDAY"


def test_wednesday():
    assert get_day_name(7, 12, 2023) == "WEDNESDAY"


def test_thursday():
    assert get_day_name(7, 13, 2023) == "THURSDAY"


def test_friday():
    assert get_day_name(7, 14, 2023) == "FRIDAY"


def test_saturday():
    assert get_day_name(7, 15, 2023) == "SATURDAY"


def test_sunday():
    assert get_day_name(7, 16, 2023) == "SUNDAY"


def test_invalid_month():
    with pytest.raises(ValueError):
        get_day_name(13, 10, 2023)


def test_invalid_date():
    with pytest.raises(ValueError):
        get_day_name(2, 30, 2023)
