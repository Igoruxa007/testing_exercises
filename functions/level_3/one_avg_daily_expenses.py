import collections
import decimal
from statistics import mean

from functions.level_3.models import Expense

from functions.level_3 import models
import datetime


def calculate_average_daily_expenses(expenses: list[Expense]) -> decimal.Decimal:
    total_expenses_dy_day = collections.defaultdict(decimal.Decimal)
    for expense in expenses:
        total_expenses_dy_day[expense.spent_at.date()] += expense.amount
    return mean(total_expenses_dy_day.values())


if __name__ == '__main__':
    currency = models.Currency.RUB
    card_1 = models.BankCard(last_digits='1234', owner='Igor')
    card_2 = models.BankCard(last_digits='3456', owner='Ivan')
    spent_at = datetime.datetime(2023, 11, 5, 10, 10) 
    category = models.ExpenseCategory.SUPERMARKET
    any_expense=[
        models.Expense(amount=10, currency=currency, card=card_1, spent_in='magaz', spent_at=spent_at, category=category),
        models.Expense(amount=20, currency=currency, card=card_2, spent_in='magaz', spent_at=spent_at, category=category)
    ]
    print(calculate_average_daily_expenses(any_expense))
