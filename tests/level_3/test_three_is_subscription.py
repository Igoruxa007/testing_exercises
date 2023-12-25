from functions.level_3.three_is_subscription import is_subscription

def test_is_subscription_false(any_expense):
    assert is_subscription(any_expense[0], any_expense) is False 

def test_is_subscription_true(expense_with_different_dates):
    assert is_subscription(expense_with_different_dates[0], expense_with_different_dates) is True