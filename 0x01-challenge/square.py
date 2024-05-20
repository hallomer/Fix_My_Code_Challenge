#!/usr/bin/python3
""" Square class. """


class Square():
    """ Square class """
    def __init__(self, width=0, height=0):
        """Initialize the attributes of an object"""
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """Area of the square"""
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Permiter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
