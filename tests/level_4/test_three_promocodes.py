from unittest.mock import patch

from functions.level_4.three_promocodes import generate_promocode


def test_generate_promocode_success_case():
    with patch('functions.level_4.three_promocodes.random.choice') as random_choice_stub:
        random_choice_stub.return_value = 'a'
        assert generate_promocode() == 'aaaaaaaa'

def test_generate_promocode_success_case_with_len():
    with patch('functions.level_4.three_promocodes.random.choice') as random_choice_stub:
        random_choice_stub.return_value = 'a'
        assert generate_promocode(4) == 'aaaa'