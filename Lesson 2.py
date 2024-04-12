
# class DiscountCalculator:
#     def __init__(self, discount):
#         self._discount = discount/100
#
#
#
#     def __call__(self, price):
#         new_price = price - (price * self._discount)
#         #new_price = price * (1 - self._discount)
#         return new_price
# calculator = DiscountCalculator(20)
# print(calculator(50))

# class Discount:
#     def __init__(self, discount):
#         self._discount = discount/100
#
#     def __call__(self, price):
#         new_price = price - (price * self._discount)
#         return new_price
#
# calculator = Discount(45)
# print(calculator(10))


# class Person:
#     def __init__(self, Boy):
#         self._Boy = Boy
#
#     def __call__(self, x):
#         return self._Boy * x
# functor = Person(10)
# result = functor
#
# class Demo:
#     def __init__(self, value):
#         self._value = value
#
#     def __call__(self):
#         self.func()
#         print("Привыт пайтон")
#
# @Demo
# def decor(*args):
#     print("Текст декоратора" *args)
#
# #decor = Demo(decor)
#
# decor()
# print(type(decor))

class ImageResizer:
    def __init__(self, width, height, max_widht=1000, max_height=1000):
        self._width = width
        self._height = height
        self._max_widht = max_widht
        self._max_height = max_height

    @property
    def width(self):
        print("propetry from width")
        return self._width
    @width.getter
    def width(self):
        print("with.getter")
        return self._width

    @width.setter
    def width(self, value):
        print("with.setter")
        if value <= self._max_widht:
           self._width = value
        else:
            raise ValueError("bad value")

    @property
    def height(self):
        print("propetry from height")
        return self._height

    @height.getter
    def height(self):
        print("height getter")
        return self._height

    @height.setter
    def height(self, value):
        print("height setter")
        if value <= self._max_height:
            self._height = value
        else:
            raise ValueError("bad value")
    @height.deleter
    def height(self):
        print("hight from deleter")
        def self._height
        self._height = None #замовчування

resizer = ImageResizer(0, 0, 1200, 1600)
resizer.width = 100
print(resizer.width)
# resizer.height = 300
# print(resizer.height)
del resizer.height


class MyDescriptor:
    def __get__(self, instance, owner):
        print("Getting the attribute")
        print(self)
        print(instance)
        print(owner)

    def __set__(self, instance, value):
        print("setting the attribyte")

class MyClass:
    attr = MyDescriptor()

obj = MyClass:
obj.attr
obj.attr = 20