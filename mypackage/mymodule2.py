"""이것은 나의 2번째 모듈입니다. 곱하기와 나누기가 있습니다."""

def mul(x, y):
    """Multiplication function"""


    return  x*y

def div(x, y):
    """Division funciton"""

    return  x/y

class Arithme(object):
    """This is Arithme class

    :param int a: The first one.
    :param int b: The second one.
    """

    const = 42
    """This is class attribute"""

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, x, y=1):
        """add method"""

        return x+y

    def mul(self, x, y=1):
        """mul method"""

        return x*y

class Another(Arithme):
    """This is Another class

    :param int a: The first one.
    :param int b: The second one.
    """

    def sub(self, x, y=1):
        """sub method"""

        return x-y

    def div(self, x, y=1):
        """div method"""
        return x/y

__all__ = [
    "mul",
    "div",
    "Arithme",
    "Another",
]