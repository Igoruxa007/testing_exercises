from functions.level_1.four_bank_parser import BankCard, SmsMessage, Expense, parse_ineco_expense


def test_parse_ineco_expense_normal_data(sms, one_card, expense):
    assert parse_ineco_expense(sms, one_card) == expense

def test_parse_ineco_expense_cards_with_same_number(sms, cards_with_same_number, expense):
    assert parse_ineco_expense(sms, cards_with_same_number) == expense