import pytest
from gcd_algorithm import great_circle_distance


def test_great_circle_distance():
    calculated_distance = great_circle_distance(
        52.2296756, 21.0122287, 41.8919300, 12.5113300)
    assert calculated_distance == pytest.approx(1317.11, rel=1e-2)
