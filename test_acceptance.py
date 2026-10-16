import math
from triangle import classify_triangle

def test_customer_requirements():
    #AC 1 
    assert classify_triangle(1,2,3) == "Invalid"

    #AC 2
    assert classify_triangle(3, 4, 5) == "Right Scalene"

    #AC 3
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"
