x = 20

class Add:
    x = 10

    def __init__(self, value):
        self.x = value

    @staticmethod
    def add_static(y):
        print(f"Static: {x+y}")

    @classmethod
    def add_class(cls, y):
        print(f"Class: {cls.x+y}")

    def add_method(self, y):
        print(f"Method: {self.x+y}")


a = Add(4)
a.add_static(10)
a.add_class(10)
a.add_method(10)
print(Add.x)
print(a.x)
