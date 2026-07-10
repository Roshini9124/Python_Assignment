import pytest
from src.StringFormatting.util import print_formatted

def test_number_1(capsys):
    print_formatted(1)
    captured = capsys.readouterr()
    assert captured.out == "1 1 1 1\n"


def test_number_2(capsys):
    print_formatted(2)
    captured = capsys.readouterr()
    expected = (
        "1 1 1 1\n"
        "2 2 2 10\n"
    )
    assert captured.out == expected


def test_number_5(capsys):
    print_formatted(5)
    captured = capsys.readouterr()
    expected = (
        "  1   1   1   1\n"
        "  2   2   2  10\n"
        "  3   3   3  11\n"
        "  4   4   4 100\n"
        "  5   5   5 101\n"
    )
    assert captured.out == expected


def test_number_10(capsys):
    print_formatted(10)
    captured = capsys.readouterr()
    lines = captured.out.strip().split("\n")
    assert len(lines) == 10
