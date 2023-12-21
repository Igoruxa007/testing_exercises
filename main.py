from functions.level_3 import models
from functions.level_3.one_avg_daily_expenses import calculate_average_daily_expenses
from functions.level_3.two_expense_categorizer import guess_expense_category

import datetime


def one():
    currency = models.Currency.RUB
    card = models.BankCard(last_digits='1234', owner='Igor')
    spent_at = datetime.datetime(2023, 11, 5, 10, 10) 
    category = models.ExpenseCategory.SUPERMARKET
    any_expense=[
        models.Expense(amount=10, currency=currency, card=card, spent_in='magaz', spent_at=spent_at, category=category),
    ]
    print(calculate_average_daily_expenses(any_expense))

def two():
    card = [models.BankCard(last_digits='1234', owner='Ivan')]
    expense = models.Expense(amount=20, currency=20, card=card, spent_in='julis', spent_at=datetime.datetime(2023, 11, 15, 15, 18), category=models.ExpenseCategory.TRANSPORT)
    print(guess_expense_category(expense=expense))

if __name__ == '__main__':
    two()


