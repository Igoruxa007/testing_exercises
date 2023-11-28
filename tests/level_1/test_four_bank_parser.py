from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime


def test_parse_ineco_expense():
    sms = SmsMessage('10 20 30, 12345671234 15.11.23 15:18 ololo authcode 456', 'Ivan', '2013-10-10')
    cards = [BankCard('1234', 'Ivan')]
    expense = Expense(amount=20, card=BankCard('1234', 'Ivan'), spent_in='ololo', spent_at=datetime.datetime(2023, 11, 15, 15, 18))
    assert parse_ineco_expense(sms, cards) == expense
