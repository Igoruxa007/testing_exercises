from functions.level_1.two_date_parser import compose_datetime_from
import datetime


def test_compose_datetime_from():
    today = datetime.datetime.today()
    assert compose_datetime_from('sadf', '16:45') == datetime.datetime(today.year, today.month, today.day, hour=16, minute=45)
    assert compose_datetime_from('tomorrow', '16:45') == datetime.datetime(today.year, today.month, today.day+1, hour=16, minute=45)
