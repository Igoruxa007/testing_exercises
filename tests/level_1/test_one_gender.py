from functions.level_1.one_gender import genderalize


def test_genderalize_gender_male():
    assert genderalize('a', 'b', 'male') == 'a'

def test_genderalize_gender_female():
    assert genderalize('a', 'b', 'female') == 'b'

def test_genderalize_gender_any_str():
    assert genderalize('a', 'b', 'abc') == 'b'

def test_genderalize_empty_verb():
    assert genderalize('', '', 'male') == ''
