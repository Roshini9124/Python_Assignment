from src.TextAlign.util import text_aligning
import pytest


def test_returns_list():
    result = text_aligning(5)
    assert isinstance(result, list)
    


def test_number_of_lines():
    thickness = 5
    result = text_aligning(thickness)
    expected = (
        thickness
        + (thickness + 1)
        + (thickness + 1) // 2
        + (thickness + 1)
        + thickness
    )
    assert len(result) == expected


def test_top_cone():
    result = text_aligning(5)
    assert result[0].strip() == "H"
    assert result[1].strip() == "HHH"
    assert result[2].strip() == "HHHHH"


def test_middle_belt():
    result = text_aligning(5)
    assert "HHHHHHHHHHHHHHHHHHHHHHHHH" in result[11]


def test_bottom_cone():
    result = text_aligning(5)
    assert result[-1].strip() == "H"


def test_invalid_even_thickness():
    with pytest.raises(ValueError):
        text_aligning(4)


def test_invalid_zero_thickness():
    with pytest.raises(ValueError):
        text_aligning(0)