from functions.level_3.four_fraud import find_fraud_expenses

def test_find_fraud_expenses_with_fraud(any_expense_3, any_expense_3_result):
    assert find_fraud_expenses(any_expense_3) == any_expense_3_result

def test_find_fraud_expenses_without_fraud(any_expense):
    assert find_fraud_expenses(any_expense) == []