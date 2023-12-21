from functions.level_3.three_is_subscription import is_subscription

def test_is_subscription_false(any_expense):
    assert is_subscription(any_expense[0], any_expense) == False 

def test_is_subscription_true(any_expense_2):
    assert is_subscription(any_expense_2[0], any_expense_2) == True