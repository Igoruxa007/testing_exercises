from functions.level_3.two_expense_categorizer import guess_expense_category

def test_guess_expense_category_success(any_expense, category_transport):
    assert guess_expense_category(any_expense[0]) == category_transport

def test_guess_expense_category_out_of_category(any_expense):
    assert guess_expense_category(any_expense[1]) == None

def test_guess_expense_category_start_with_delimiter(any_expense, category_transport):
    assert guess_expense_category(any_expense[2]) == category_transport

def test_guess_expense_category_another_category(any_expense, category_bar_rest):
    assert guess_expense_category(any_expense[3]) == category_bar_rest

def test_guess_expense_category_end_with_delimiter(any_expense, category_bar_rest):
    assert guess_expense_category(any_expense[4]) == category_bar_rest