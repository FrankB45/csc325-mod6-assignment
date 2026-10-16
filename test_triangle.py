import math
import pytest

from triangle import classify_triangle


@pytest.mark.parametrize("sides", [
    (0, 4, 5),       # Zero-length side
    (4, -1, 5),      # Negative side
    (1, 2, 4),       # Triangle inequality fails
    (1, 2, 3),       # Degenerate: two sides sum to the third
    (3, 1, 2),       # Same boundary, different side order
    (1, 3, 2),
])
def test_invalid_triangles(sides):
    assert classify_triangle(*sides) == "Invalid"


@pytest.mark.parametrize("sides", [
    (5, 5, 5),
    (0.5, 0.5, 0.5),
])
def test_equilateral_triangles(sides):
    assert classify_triangle(*sides) == "Equilateral"


@pytest.mark.parametrize("sides", [
    (5, 5, 6),
    (5, 6, 5),
    (6, 5, 5),
])
def test_isosceles_triangles(sides):
    assert classify_triangle(*sides) == "Isosceles"


@pytest.mark.parametrize("sides", [
    (4, 5, 6),
    (6, 4, 5),
    (2, 3, 4),
])
def test_scalene_triangles(sides):
    assert classify_triangle(*sides) == "Scalene"


@pytest.mark.parametrize("sides, expected", [
    ((3, 4, 5), "Right Scalene"),
    ((5, 3, 4), "Right Scalene"),
    ((4, 5, 3), "Right Scalene"),
    ((5, 5, 5 * math.sqrt(2)), "Right Isosceles"),
])
def test_right_triangles(sides, expected):
    assert classify_triangle(*sides) == expected