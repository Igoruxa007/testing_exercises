from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense
import datetime


def test_parse_ineco_expense_normal_data():
    amount = 20
    card = 12345671234
    date = '15.11.23'
    time = '15:18'
    spent_in='ololo'
    sms = SmsMessage(f'10 {amount} 30, {card} {date} {time} {spent_in} authcode 456', 'Ivan', '2013-10-10')
    cards = [BankCard('1234', 'Ivan')]
    expense = Expense(amount=amount, card=cards[0], spent_in='ololo', spent_at=datetime.datetime(2023, 11, 15, 15, 18))
    assert parse_ineco_expense(sms, cards) == expense

def test_parse_ineco_expense_cards_with_same_number():
    amount = 20
    card = 12345671234
    date = '15.11.23'
    time = '15:18'
    spent_in='ololo'
    sms = SmsMessage(f'10 {amount} 30, {card} {date} {time} {spent_in} authcode 456', 'Ivan', '2013-10-10')
    cards = [BankCard('1234', 'Ivan'),BankCard('1234', 'Irina')]
    expense = Expense(amount=amount, card=cards[0], spent_in='ololo', spent_at=datetime.datetime(2023, 11, 15, 15, 18))
    assert parse_ineco_expense(sms, cards) == expense