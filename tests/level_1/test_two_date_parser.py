from functions.level_1.two_date_parser import compose_datetime_from
import pytest


def test_compose_datetime_from_date_is_tomorrow(tomorrow_date_time):
    assert compose_datetime_from('tomorrow', '16:45') == tomorrow_date_time

@pytest.mark.parametrize(
    "date_str, time_str",
    [
        ('sadf', '16:45'),
        ('2023-11-30', '16:45'),
        ('', '16:45')
    ],
    ids=['date is symbols', 'date is any date', 'empty date']
)

def test_compose_datetime_from_date(date_str, time_str, today_date_time):
    assert compose_datetime_from(date_str, time_str) == today_date_time