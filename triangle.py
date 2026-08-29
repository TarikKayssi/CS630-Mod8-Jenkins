#triangle.py
#----------------------------------------------------------#
#A code library for CS630, week 8, Assignment 2, SNHU
#By Matthew Heusser M.Heusser@snhu.edu Jun 2025
#
# You'll include this in a flask API
# That you will stand up
# And test under continuous integration
#
#----------------------------------------------------------#


def classify_triangle(a: float, b: float, c: float) -> str:
    """
    Determines the type of triangle (or non-triangle) given three side lengths.

    Args:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.

    Returns:
        str: One of:
            - "equilateral"    (all three sides equal)
            - "isosceles"      (exactly two sides equal)
            - "scalene"        (all sides different)
            - "not a triangle" (fails triangle inequality or has non-positive side)
    """
    # First, check for valid (positive) side lengths
    if a <= 0 or b <= 0 or c <= 0:
        return "not a triangle"

    # Check triangle inequality
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "not a triangle"

    # All sides equal
    if a == b == c:
        return "equilateral"

    # Exactly two sides equal
    if a == b or a == c or b == c:
        return "isosceles"

    # All sides different
    return "scalene"
