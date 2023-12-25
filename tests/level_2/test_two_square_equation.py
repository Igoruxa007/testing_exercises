from functions.level_2.two_square_equation import solve_square_equation
import pytest


@pytest.mark.parametrize(
    "square_coefficient, linear_coefficient, const_coefficient, expected_result",
    [
        (1, 4, 3, (-3.0, -1.0)),
        (1, 3, 3, (None, None)),
        (0, 4, 3, (-0.75, None)),
        (0, 0, 3, (None, None)),
    ]
)

def test__solve_square_equation(square_coefficient, linear_coefficient, const_coefficient, expected_result):
    assert solve_square_equation(square_coefficient, linear_coefficient, const_coefficient) == expected_result