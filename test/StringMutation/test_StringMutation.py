import pytest
from src.StringMutation.util import mutate_string

def test_replace_middle_character():
    assert mutate_string("abracadabra", 5, "k") == "abrackdabra"


def test_replace_first_character():
    assert mutate_string("hello", 0, "H") == "Hello"


def test_replace_last_character():
    assert mutate_string("world", 4, "!") == "worl!"


def test_single_character_string():
    assert mutate_string("a", 0, "b") == "b"


def test_replace_with_same_character():
    assert mutate_string("python", 2, "t") == "python"


def test_replace_with_digit():
    assert mutate_string("abcde", 2, "1") == "ab1de"


def test_replace_with_special_character():
    assert mutate_string("hello", 1, "@") == "h@llo"
