class Rectangle:
    _width,_height=0,0
    def __init__(self,width,height):
        self._width=width
        self._height=height
    #setter
    def set_width(self,width):
        self._width=width
    def set_height(self,height):
        self._height=height
    #getter
    def get_area(self):
        return self._width*self._height
    def get_perimeter(self):
        return (2*self._width+2*self._height)
    def get_diagonal(self):
        return ((self._width ** 2 + self._height ** 2) ** .5)
    def get_picture(self):
        if (self._width>50 or self._height>50):
            return "Too big for picture."
        else:
            return (("*"*self._width+"\n")*self._height)
    def get_amount_inside(self,shape):
        return int(self.get_area()/shape.get_area())
    #str
    def __str__(self):
        return f"Rectangle(width={self._width}, height={self._height})"
class Square(Rectangle):
    _side=0
    def __init__(self,side):
        self._width=side
        self._height=side
    #setter
    def set_side(self,side):
        self._width=side
        self._height=side
    #str
    def __str__(self):
        return f"Square(side={self._width})"