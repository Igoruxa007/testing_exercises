from functions.level_2.three_first import first
import pytest

@pytest.mark.parametrize(
    "items, default, expected_result",
    [
        ([1,2], 5, 1),
        (None, None, None),
    ]
)

def test__first(items, default, expected_result):
    assert first(items, default) == expected_result

def test__first__defaul_not_set():
    with pytest.raises(AttributeError):
        assert first(items=None, default="NOT_SET")