#Implement a Triangle Classifier
# 
# Write Unit Tests using Copilot
# One Acceptance test from a customer's requirements

import math

def is_valid_triangle(a,b,c) -> bool:
    """
    Check if the given sides form a valid triangle.

    Args:
        a : Length of the first side.
        b : Length of the second side.
        c : Length of the third side.

    Returns:
        bool: True if the sides form a valid triangle, False otherwise.
    """
    sides = (a, b, c)

    if any(not math.isfinite(side) or side <= 0 for side in sides):
        return False

    x, y, z = sorted(sides)
    return x > z - y

def classify_triangle(a, b, c) -> str:
    """
    Classify a triangle based on its side lengths.

    Args:
        a : Length of the first side.
        b : Length of the second side.
        c : Length of the third side.

    Returns:
        str: Type of the triangle ("Equilateral", "Isosceles", "Scalene", "Right Isosceles", "Right Scalene", or "Invalid").
    """
    if not is_valid_triangle(a, b, c):
        return "Invalid"

    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        shape = "Isosceles"
    else:
        shape = "Scalene"

    x, y, z = sorted((a, b, c))

    # Normalize before squaring to avoid overflow with large sides.
    if math.isclose((x / z) ** 2 + (y / z) ** 2, 1.0, rel_tol=1e-9):
        return f"Right {shape}"

    return shape


    