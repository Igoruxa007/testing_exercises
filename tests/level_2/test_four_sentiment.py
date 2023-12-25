from functions.level_2.four_sentiment import check_tweet_sentiment
import pytest

@pytest.mark.parametrize(
    "text, good, bad, expected_result",
    [
        ('a b c d e', ['f'], ['g'], None),
        ('a b c d e', [], [], None),
        ('', [], [], None),
        ('a b c d e', ['a'], ['b'], None),
        ('a b c d e', ['a'], ['a'], None),
        ('a b c d e', ['a', 'b'], ['c'], 'GOOD'),
        ('a b c d e', ['a'], ['b', 'c'], 'BAD'),
        ('A b c d e', ['a', 'b'], ['c'], 'GOOD'),
        ('a B c d e', ['a'], ['b', 'c'], 'BAD'),
        ('a b c d e', ['a', 'B'], ['c'], None),
        ('a b c d e', ['a'], ['B', 'c'], None)
    ]
)

def test__check_tweet_sentiment(text, good, bad, expected_result):
    assert check_tweet_sentiment(text, good, bad) == expected_result