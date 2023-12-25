from functions.level_1.five_title import change_copy_item
import pytest

@pytest.mark.parametrize(
        "text, expected_result",
        [
            ('a'*92, 'a'*92),
            ('a'*91, f'Copy of {'a'*91}'),
            ('Copy of abcd', 'Copy of abcd (2)'),
            ('Copy of abcd (1)', 'Copy of abcd (2)')
        ]
)

def test_change_copy_item_title_len_equals_92(text, expected_result):
    assert change_copy_item(text) == expected_result

@pytest.mark.parametrize(
        "text, max, expected_result",
        [
            ('a'*10, 10,  'a'*10),
            ('a'*11, 20,  f'Copy of {'a'*11}'),
            ('Copy of abcd', 30, 'Copy of abcd (2)')
        ]
)

def test_change_copy_item_title_len_equals_92(text, max, expected_result):
    assert change_copy_item(text, max) == expected_result