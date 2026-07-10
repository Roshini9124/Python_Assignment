from src.WordOrder.util import word_order
def test_word_order(capsys):
    words = ["bcdef", "abcdefg", "bcde", "bcdef"]

    word_order(words)

    captured = capsys.readouterr()
    assert captured.out == "3\n2 1 1\n"
