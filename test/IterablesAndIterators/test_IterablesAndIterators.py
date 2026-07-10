from src.IterablesAndIterators.util import calculate_probability


def test_sample_case():
    letters = ["a", "a", "c", "d"]
    k = 2
    assert round(calculate_probability(letters, k), 4) == 0.8333


def test_all_a():
    letters = ["a", "a", "a"]
    k = 2
    assert calculate_probability(letters, k) == 1.0


def test_no_a():
    letters = ["b", "c", "d"]
    k = 2
    assert calculate_probability(letters, k) == 0.0


def test_single_selection():
    letters = ["a", "b", "c", "d"]
    k = 1
    assert calculate_probability(letters, k) == 0.25


def test_select_all():
    letters = ["a", "b", "c"]
    k = 3
    assert calculate_probability(letters, k) == 1.0