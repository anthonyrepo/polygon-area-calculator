from shape_calculator import Rectangle, Square
import pytest

@pytest.fixture
def rect():
    rect = Rectangle(3, 6)
    return rect

@pytest.fixture
def sq():
    sq = Square(5)
    return sq

def test_subclass():
    """Expected Square class to be a subclass of the Rectangle class."""
    assert issubclass(Square, Rectangle) == True

def test_distinct_classes():
    """Expected Square class to be a distinct class from the Rectangle class."""
    assert (Square is not Rectangle) == True

def test_is_square_and_rectangle(sq):
    """Expected square object to be an instance of the Square class and the Rectangle class."""
    assert (isinstance(sq, Square) and isinstance(sq, Rectangle)) == True

def test_rectangle_string(rect):
    """Expected string representation of rectangle to be "Rectangle(width=3, height=6)" """
    assert str(rect) == "Rectangle(width=3, height=6)"

def test_square_string(sq):
    """Expected string representation of square to be "Square(side=5)" """
    assert str(sq) == "Square(side=5)"

def test_area(rect, sq):
    """
    Expected area of rectangle to be 18
    Expected area of square to be 25
    """
    assert rect.get_area() == 18
    assert sq.get_area() == 25

def test_perimeter(rect, sq):
    """
    Expected perimeter of rectangle to be 18
    Expected perimeter of square to be 20
    """
    assert rect.get_perimeter() == 18
    assert sq.get_perimeter() == 20

def test_diagonal(rect, sq):
    """
    Expected diagonal of rectangle to be 6.708203932499369
    Expected diagonal of square to be 7.0710678118654755
    """
    assert rect.get_diagonal() == 6.708203932499369
    assert sq.get_diagonal() == 7.0710678118654755

def test_set_attributes(rect, sq):
    """
    Expected string representation of rectangle after setting new values to be "Rectangle(width=7, height=8)"
    Expected string representation of square after setting new values to be "Square(side=2)"
    Expected string representation of square after setting width to be "Square(side=4)"
    """
    rect.set_width(7)
    rect.set_height(8)
    sq.set_side(2)
    assert str(rect) == "Rectangle(width=7, height=8)"
    assert str(sq) == "Square(side=2)"
    sq.set_width(4)
    assert str(sq) == "Square(side=4)"

def test_rectangle_picture(rect):
    """Expected rectangle picture to be different."""
    rect.set_width(7)
    rect.set_height(3)
    assert rect.get_picture() == "*******\n*******\n*******\n"

def test_square_picture(sq):
    """Expected square picture to be different."""
    sq.set_side(2)
    assert sq.get_picture() == "**\n**\n"

def test_big_picture(rect):
    """Expected message: "Too big for picture." """
    rect.set_width(51)
    rect.set_height(3)
    assert rect.get_picture() == "Too big for picture."

def test_get_amount_inside(rect, sq):
    """Expected `get_amount_inside` to return 6."""
    rect.set_height(10)
    rect.set_width(15)
    assert rect.get_amount_inside(sq) == 6

def test_get_amount_inside_two_rectangles(rect):
    """Expected `get_amount_inside` to return 1."""
    rect2 = Rectangle(4, 8)
    assert rect2.get_amount_inside(rect) == 1

def test_get_amount_inside_none(rect):
    """Expected `get_amount_inside` to return 0."""
    rect2 = Rectangle(2, 3)
    assert rect2.get_amount_inside(rect) == 0