import datetime

import pytest

from functions.level_1.four_bank_parser import SmsMessage, BankCard, Expense

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
def expense(one_card):
    expense = Expense(amount=20, card=one_card[0], spent_in='ololo', spent_at=datetime.datetime(2023, 11, 15, 15, 18))
    return expense