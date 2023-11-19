import Polygon_area_calculator
from unittest import main
rect = Polygon_area_calculator.Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)

sq = Polygon_area_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)

main(module='test_module',exit=False)