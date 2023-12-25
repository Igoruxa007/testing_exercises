from functions.level_2.five_replace_word import replace_word
import pytest

@pytest.mark.parametrize(
    "text, replace_from, replace_to, expected_result",
    [
        ('ab bc cd', 'bc', 'cb', 'ab cb cd'),
        ('ab bc cd', 'bc', '', 'ab  cd'),
        ('ab Bc cd', 'bC', 'cb', 'ab cb cd')
    ],
    ids=['success case', 'empty "replace_to"', 'upper symbols']
)

def test__replace_word(text, replace_from, replace_to, expected_result):
    assert replace_word(text, replace_from, replace_to) == expected_result