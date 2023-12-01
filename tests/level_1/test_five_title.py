from functions.level_1.five_title import change_copy_item


def test_change_copy_item_title_len_equals_92():
    text = 'a'*92
    assert change_copy_item(text) == text

def test_change_copy_item_title_len_les_92():
    text = 'a'*91
    assert change_copy_item(text) == f'Copy of {text}'

def test_change_copy_item_change_max_title_len_equal():
    max = 10
    text = 'a'*max
    assert change_copy_item(text, max) == text

def test_change_copy_item_change_max_title_len_less():
    max = 20
    text = 'a'* (max-9)
    assert change_copy_item(text, max) == f'Copy of {text}'

def test_change_copy_item_text_with_template():
    assert change_copy_item('Copy of abcd') == 'Copy of abcd (2)'

def test_change_copy_item_text_with_template_and_number():    
    assert change_copy_item('Copy of abcd (1)') == 'Copy of abcd (2)'
    assert change_copy_item('Copy of abcd (4)') == 'Copy of abcd (5)'

def test_change_copy_item_title_template_len_max():
    text = 'Copy of' + 'a'*92
    assert change_copy_item(text) == text
