import math

import pytest

from soft_estruturas.section import rectangular_area, rectangular_second_moment


def test_rectangular_area() -> None:
    assert rectangular_area(0.05, 0.15) == pytest.approx(0.0075)


def test_rectangular_second_moment() -> None:
    assert rectangular_second_moment(0.05, 0.15) == pytest.approx(0.05 * 0.15**3 / 12)


@pytest.mark.parametrize("width,height", [(0, 1), (1, 0), (-1, 2), (2, -1), (math.inf, 1), (1, math.nan)])
def test_invalid_dimensions_raise_value_error(width: float, height: float) -> None:
    with pytest.raises(ValueError):
        rectangular_area(width, height)
    with pytest.raises(ValueError):
        rectangular_second_moment(width, height)
