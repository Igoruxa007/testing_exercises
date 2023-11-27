from functions.level_1.one_gender import genderalize


def test_genderalize():
    assert genderalize('a', 'b', 'male') == 'a'
    assert genderalize('a', 'b', 'female') == 'b'
