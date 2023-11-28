from functions.level_1.five_title import change_copy_item


def test_change_copy_item():
    text = 'a'*100
    assert change_copy_item(text) == 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    text = 'a'*10
    assert change_copy_item(text, 10) == 'aaaaaaaaaa'
    assert change_copy_item(text) == 'Copy of aaaaaaaaaa'
    
    assert change_copy_item('Copy of abcd (1)') == 'Copy of abcd (2)'
    assert change_copy_item('Copy of abcd') == 'Copy of abcd (2)'