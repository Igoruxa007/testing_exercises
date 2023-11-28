from functions.level_1.three_url_builder import build_url


def test_build_url():
    assert build_url('host_1', 'host_2', {'a':1, 'b':2}) == 'host_1/host_2?a=1&b=2'
    assert build_url('host_1', 'host_2') == 'host_1/host_2'
