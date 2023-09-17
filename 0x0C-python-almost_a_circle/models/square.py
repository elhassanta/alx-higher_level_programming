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


if __name__ == "__main__":

    s1 = Square(5)
    print(s1)

    s1.update(10)
    print(s1)

    s1.update(1, 2)
    print(s1)

    s1.update(1, 2, 3)
    print(s1)

    s1.update(1, 2, 3, 4)
    print(s1)

    s1.update(x=12)
    print(s1)

    s1.update(size=7, y=1)
    print(s1)

    s1.update(size=7, id=89, y=1)
    print(s1)
