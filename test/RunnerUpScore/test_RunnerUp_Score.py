import pytest
from src.RunnerUp_Score.util import runner_up_score

def test_normal_case():
    scores = [2, 3, 6, 6, 5]
    assert runner_up_score(scores) == 5


def test_sorted_scores():
    scores = [1, 2, 3, 4, 5]
    assert runner_up_score(scores) == 4


def test_unsorted_scores():
    scores = [10, 5, 20, 15]
    assert runner_up_score(scores) == 15


def test_negative_scores():
    scores = [-5, -2, -8, -1]
    assert runner_up_score(scores) == -2



def test_two_elements():
    scores = [10, 5]
    assert runner_up_score(scores) == 5


def test_all_same_scores():
    scores = [4, 4, 4, 4]
    assert runner_up_score(scores) == 4
