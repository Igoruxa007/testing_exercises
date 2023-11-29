from functions.level_1.two_date_parser import compose_datetime_from
import datetime


def test_compose_datetime_from_date_is_tomorrow():
    today = datetime.datetime.today() + datetime.timedelta(days=1)
    assert compose_datetime_from('tomorrow', '16:45') == datetime.datetime(today.year, today.month, today.day, hour=16, minute=45)

def test_compose_datetime_from_date_is_not_tommorow():
    today = datetime.datetime.today()  
    assert compose_datetime_from('sadf', '16:45') == datetime.datetime(today.year, today.month, today.day, hour=16, minute=45)
    assert compose_datetime_from('2023-11-30', '16:45') == datetime.datetime(today.year, today.month, today.day, hour=16, minute=45)

def test_compose_datetime_from_date_is_empty():
    today = datetime.datetime.today()  
    assert compose_datetime_from('', '16:45') == datetime.datetime(today.year, today.month, today.day, hour=16, minute=45)