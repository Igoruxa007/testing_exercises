import datetime

import pytest

from functions.level_1.four_bank_parser import SmsMessage, BankCard, Expense
from functions.level_3 import models

@pytest.fixture
def today_date_time():
    today = datetime.datetime.today()
    return datetime.datetime(today.year, today.month, today.day, hour=16, minute=45)

@pytest.fixture
def tomorrow_date_time(today_date_time):
    return today_date_time + datetime.timedelta(days=1)

@pytest.fixture
def expense(one_card):
    expense = Expense(amount=20, card=one_card[0], spent_in='ololo', spent_at=datetime.datetime(2023, 11, 15, 15, 18))
    return expense

@pytest.fixture
def sms():
    amount = 20
    card = 12345671234
    date = '15.11.23'
    time = '15:18'
    spent_in='ololo'
    sms = SmsMessage(f'10 {amount} 30, {card} {date} {time} {spent_in} authcode 456', 'Ivan', '2013-10-10')
    return sms

@pytest.fixture
def one_card():
    card = [BankCard('1234', 'Ivan')]
    return card

@pytest.fixture
def cards_with_same_number(one_card):
    one_card.append(BankCard('1234', 'Irina'))
    return one_card

@pytest.fixture
def any_expense():
    currency = models.Currency.RUB
    card_1 = models.BankCard(last_digits='1234', owner='Igor')
    card_2 = models.BankCard(last_digits='3456', owner='Ivan')
    spent_at_1 = datetime.datetime(2023, 11, 5, 10, 10)
    spent_at_2 = datetime.datetime(2023, 10, 5, 10, 10) 
    category_1 = models.ExpenseCategory.TRANSPORT
    category_2 = models.ExpenseCategory.BAR_RESTAURANT
    any_expense=[
        models.Expense(amount=10, currency=currency, card=card_1, spent_in='www.taxi.yandex.ru', spent_at=spent_at_1, category=category_1),
        models.Expense(amount=20, currency=currency, card=card_2, spent_in='olofdsfsdfsdflo', spent_at=spent_at_1, category=category_1),
        models.Expense(amount=20, currency=currency, card=card_2, spent_in='asdf-www.taxi.yandex.ru', spent_at=spent_at_2, category=category_1),
        models.Expense(amount=30, currency=currency, card=card_2, spent_in='julis', spent_at=spent_at_1, category=category_2),
        models.Expense(amount=40, currency=currency, card=card_2, spent_in='asd-set//lkj', spent_at=spent_at_2, category=category_2)
    ]
    return any_expense

@pytest.fixture
def category_transport():
    return models.ExpenseCategory.TRANSPORT

@pytest.fixture
def category_bar_rest():
    return models.ExpenseCategory.BAR_RESTAURANT

@pytest.fixture
def expense_with_different_dates(any_expense):
    currency = models.Currency.RUB
    card = models.BankCard(last_digits='1234', owner='Igor')
    spent_at = datetime.datetime(2023, 12, 5, 10, 10)
    category = models.ExpenseCategory.TRANSPORT
    for i in range(4):
        any_expense.append(models.Expense(amount=10, currency=currency, card=card, spent_in='www.taxi.yandex.ru', spent_at=(spent_at+ datetime.timedelta(days=35*i)), category=category))
    return any_expense

@pytest.fixture
def expense_with_same_elements(any_expense):
    for _ in range(2):
        any_expense.append(any_expense[0])
    for _ in range(3):
        any_expense.append(any_expense[1])
    return any_expense

@pytest.fixture
def expense_with_same_elements_result(any_expense):
    return [any_expense[0]]*3 + [any_expense[1]]*4