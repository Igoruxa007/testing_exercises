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
def expense(one_card):
    expense = Expense(amount=20, card=one_card[0], spent_in='ololo', spent_at=datetime.datetime(2023, 11, 15, 15, 18))
    return expense

@pytest.fixture
def any_expense():
    currency = models.Currency.RUB
    card_1 = models.BankCard(last_digits='1234', owner='Igor')
    card_2 = models.BankCard(last_digits='3456', owner='Ivan')
    spent_at_1 = datetime.datetime(2023, 11, 5, 10, 10)
    spent_at_2 = datetime.datetime(2023, 10, 5, 10, 10) 
    category = models.ExpenseCategory.SUPERMARKET
    any_expense=[
        models.Expense(amount=10, currency=currency, card=card_1, spent_in='magaz', spent_at=spent_at_1, category=category),
        models.Expense(amount=20, currency=currency, card=card_2, spent_in='magaz', spent_at=spent_at_1, category=category),
        models.Expense(amount=20, currency=currency, card=card_2, spent_in='magaz', spent_at=spent_at_2, category=category),
    ]
    return any_expense