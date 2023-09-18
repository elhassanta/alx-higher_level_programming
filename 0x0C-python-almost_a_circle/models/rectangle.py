#!/usr/bin/python3
"""this is the discription model"""
from base import Base


class Rectangle(Base):
    """this is a tamplate to create rectangle object"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width, height, x=0, y=0, id=None):
        """this is the constroctor method"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        super().__init__(id)

    @property
    def x(self):
        """this is an abssis getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """this is x setter method"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """this is a getter y method"""
        return self.__y

    @y.setter
    def y(self, y):
        """this is y setter method"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    @property
    def height(self):
        """this the getter method of height"""
        return self.__height

    @height.setter
    def height(self, height):
        """this is the setter method of height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def width(self):
        """this the getter method of width"""
        return self.__width

    @width.setter
    def width(self, width):
        """this is the setter method of height"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    def perimeter(self):
        """this method calculate perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def area(self):
        """this method calculate the area of rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """this is the display method"""
        str1 = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        for k in range(self.y):
            str1 += "\n"
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                str1 = str1 + self.print_symbol
            if i < self.__height - 1:
                str1 = str1 + "\n"
        print(str1)

    def __str__(self):
        """this is the str method"""
        x = self.x
        y = self.y
        w = self.width
        h = self.height
        id = self.id
        return "[Rectangle] ({}) {}/{} - {}/{}".format(id, x, y, w, h)

    def __repr__(self):
        """ this method allow us to create a copy of an instance"""
        return f"Rectangle({self.width}, {self.height}, {self.x}, {self.y},\
    {self.id})"

    def update(self, *args, **kwargs):
        """this function will update instance of rectangle"""
        if len(args) >= 5:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        elif len(args) == 4:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
        elif len(args) == 3:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
        elif len(args) == 2:
            self.id = args[0]
            self.width = args[1]
        elif len(args) == 1:
            self.id = args[0]
        else:
            pass
        for k, v in kwargs.items():
            if k == "x":
                self.x = v
            elif k == "y":
                self.y = v
            elif k == "width":
                self.width = v
            elif k == "height":
                self.height = v
            elif k == "id":
                self.id = v
            else:
                pass

    def to_dictionary(self):
        """this method will convert object to a dictionary"""
        x = self.x
        y = self.y
        width = self.width
        height = self.height
        id = self.id
        return {"x": x, "y": y, "id": id, "height": height, "width": width}

    def bigger_or_equal(rectang1, rectang2):
        """this method compare two rectangles"""
        if not isinstance(rectang1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rectang2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rectang1.area() >= rectang2.area():
            return rectang1
        return rectang2
if __name__ == "__main__":

    r1 = Rectangle(3, 5, 1)
    r1_dictionary = r1.to_dictionary()
    r2 = Rectangle.create(**r1_dictionary)
    print(r1)
    print(r2)
    print(r1 is r2)
    print(r1 == r2)
