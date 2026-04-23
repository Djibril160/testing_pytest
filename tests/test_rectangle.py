import pytest
import source.shapes as shapes

# the data/import are in function my_rectangle the conftest 
def test_area(my_rectangle):
    # sinon: ok rectangle = shapes.Rectangle(5, 3)
    assert my_rectangle.area() == 50

def test_perimeter(my_rectangle):
    # perimeter = shapes.Rectangle.perimeter(5, 3)
    assert my_rectangle.perimeter() == 30

    rect1 = my_rectangle.perimeter()
    rect2 = my_rectangle.perimeter()

    assert rect1 ==   rect2
