from functions.level_1.one_gender import genderalize
import pytest

@pytest.mark.parametrize(
    "verb_male, verb_female, gender, expected_result",
    [
        ('a', 'b', 'male', 'a'),
        ('a', 'b', 'female', 'b'),
        ('a', 'b', 'abc', 'b'),
        ('', '', 'male', '')
    ],
    ids=['gender male', 'gender_female', 'gender_any_str', 'empty_verb']
)

def test_genderalize(verb_male, verb_female, gender, expected_result):
    assert genderalize(verb_male, verb_female, gender) == expected_result