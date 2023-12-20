from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses

def test__calculate_average_daily_expenses__success_case(any_expense):
    assert calculate_average_daily_expenses(any_expense) == 25