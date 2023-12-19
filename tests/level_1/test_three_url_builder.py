from functions.level_1.three_url_builder import build_url
import pytest

@pytest.mark.parametrize(
        "host_name, relative_url, get_params, expected_result",
        [
           ('host_1', 'host_2', {'a':1, 'b':2}, 'host_1/host_2?a=1&b=2'),
           ('host_1', 'host_2', {}, 'host_1/host_2'),
           ('host_1', 'host_2', None, 'host_1/host_2')
        ]
)

def test_build_url_with_all_parametrs(host_name, relative_url, get_params, expected_result):
    assert build_url(host_name, relative_url, get_params) == expected_result