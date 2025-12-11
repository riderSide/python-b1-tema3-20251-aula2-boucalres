# geometry.py


def square_area(side_length: float) -> float:
    """
    Calculate the area of a square.

    Args:
    - side_length (float): the length of one side of the square.

    Returns:
    - float: the area of the square.
    """
    if side_length < 0:
        raise ValueError("La longitud del costat no pot ser negativa.")
    return side_length * side_length


def rectangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    Args:
    - base_length (float): the length of the base of the rectangle.
    - height (float): the height of the rectangle.

    Returns:
    - float: the area of the rectangle.
    """
    if base_length < 0 or height < 0:
        raise ValueError("La longitud de la base i l'alçada han de ser positives.")
    return base_length * height


def triangle_area(base_length: float, height: float) -> float:
    """
    Calculate the area of a triangle.

    Args:
    - base_length (float): the length of the base of the triangle.
    - height (float): the height of the triangle.

    Returns:
    - float: the area of the triangle.
    """
    if base_length < 0 or height < 0:
        raise ValueError("La longitud de la base i l'alçada han de ser positives.")
    return (base_length * height) / 2


def circle_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Args:
    - radius (float): the radius of the circle.

    Returns:
    - float: the area of the circle
    """
    if radius < 0:
        raise ValueError("El radi no pot ser negatiu.")
    
    import math
    return math.pi * (radius * radius)
