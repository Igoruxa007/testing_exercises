from functions.level_1.three_url_builder import build_url


def test_build_url_with_all_parametrs():
    assert build_url('host_1', 'host_2', {'a':1, 'b':2}) == 'host_1/host_2?a=1&b=2'

def test_build_url_without_get_params(): 
    assert build_url('host_1', 'host_2') == 'host_1/host_2'
    
def test_build_url_with_empty_get_params(): 
    assert build_url('host_1', 'host_2', {}) == 'host_1/host_2'