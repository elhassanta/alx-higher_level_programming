#!/usr/bin/python3
"""our import models"""
from rectangle import Rectangle


class Square(Rectangle):
    """this is my class square"""
    def __init__(self, size, x=0, y=0, id=None):
        """this is constructor square method"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """this is str inter method to a class"""
        x = self.x
        y = self.y
        width = self.width
        id = self.id
        return "[Square] ({}) {}/{} - {}".format(id, x, y, width)

    @property
    def size(self):
        """this is the size getter method"""
        return self.width

    @size.setter
    def size(self, size):
        """this is the setter size method"""
        self.width = self.height = size

    def update(self, *args, **kwargs):
        """this method will update square instances"""
        for i in range(len(args)):
            if i == 0:
                self.id = args[0]
            elif i == 1:
                self.size = args[1]
            elif i == 2:
                self.x = args[2]
            elif i == 3:
                self.y = args[3]
            else:
                break
        if len(args) > 0:
            pass
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
                else:
                    pass

    def to_dictionary(self):
        """this method convert square in dictionary"""
        x = self.x
        y = self.y
        size = self.size
        id = self.id
        return {"id": id, "x": x, "size": size, "y": y}

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file(list_rectangles_input)

    list_rectangles_output = Rectangle.load_from_file()

    for rect in list_rectangles_input:
        print("[{}] {}".format(id(rect), rect))

    print("---")

    for rect in list_rectangles_output:
        print("[{}] {}".format(id(rect), rect))

    print("---")
    print("---")

    s1 = Square(5)
    s2 = Square(7, 9, 1)
    list_squares_input = [s1, s2]

    Square.save_to_file(list_squares_input)

    list_squares_output = Square.load_from_file()

    for square in list_squares_input:
        print("[{}] {}".format(id(square), square))

    print("---")

    for square in list_squares_output:
        print("[{}] {}".format(id(square), square))

