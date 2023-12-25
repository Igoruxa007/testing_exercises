from functions.level_3.four_fraud import find_fraud_expenses

def test_find_fraud_expenses_with_fraud(expense_with_same_elements, expense_with_same_elements_result):
    assert find_fraud_expenses(expense_with_same_elements) == expense_with_same_elements_result

def test_find_fraud_expenses_without_fraud(any_expense):
    assert find_fraud_expenses(any_expense) == []