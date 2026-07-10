import pytest
from src.MergeTheTools.util import merge_the_tools

def test_sample_case(capsys):
    merge_the_tools("AABCAAADA", 3)
    captured = capsys.readouterr()
    assert captured.out == "AB\nCA\nAD\n"


def test_unique_characters(capsys):
    merge_the_tools("ABCDEFGH", 2)
    captured = capsys.readouterr()
    assert captured.out == "AB\nCD\nEF\nGH\n"


def test_all_same_characters(capsys):
    merge_the_tools("AAAAAA", 2)
    captured = capsys.readouterr()
    assert captured.out == "A\nA\nA\n"


def test_single_character_chunks(capsys):
    merge_the_tools("ABC", 1)
    captured = capsys.readouterr()
    assert captured.out == "A\nB\nC\n"


def test_no_duplicates_in_chunk(capsys):
    merge_the_tools("ABCD", 4)
    captured = capsys.readouterr()
    assert captured.out == "ABCD\n"
