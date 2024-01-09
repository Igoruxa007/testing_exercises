from functions.level_4.one_brackets import delete_remove_brackets_quotes
from unittest.mock import patch

def test_delete_remove_brackets_quotes_str_with_brackets():
    assert delete_remove_brackets_quotes('{ asdf }') == 'asdf'

def test_delete_remove_brackets_quotes_str_without_brackets():
    assert delete_remove_brackets_quotes('asdf') == 'asdf'