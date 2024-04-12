# Завдання 3
# Створіть клас для представлення відомостей про
# замовлення. Забезпечте, щоб номер замовлення був
# тільки для читання за допомогою керованих атрибутів,
# але його можна було переглядати.
class Order:
    def __init__(self, order_number, details):
        self._order_number = order_number
        self._details = details

    @property
    def order_number(self):
        return self._order_number


    def details(self):
        return self._details

    @order_number.getter
    def order_number(self):
        return self._order_number

    @details.getter
    def detalist(self):
        return self._details



order = Order("12345", "245")
print(order.order_number)
print(order.detalist)



# class ImageResizer:
#     def __init__(self, width, height, max_widht=1000, max_height=1000):
#         self._width = width
#         self._height = height
#         self._max_widht = max_widht
#         self._max_height = max_height
#
#     @property
#     def width(self):
#         print("propetry from width")
#         return self._width
#     @width.getter
#     def width(self):
#         print("with.getter")
#         return self._width
#
#     @width.setter
#     def width(self, value):
#         print("with.setter")
#         if value <= self._max_widht:
#            self._width = value
#         else:
#             raise ValueError("bad value")
#
#     @property
#     def height(self):
#         print("propetry from height")
#         return self._height
#
#     @height.getter
#     def height(self):
#         print("height getter")
#         return self._height
#
#     @height.setter
#     def height(self, value):
#         print("height setter")
#         if value <= self._max_height:
#             self._height = value
#         else:
#             raise ValueError("bad value")
#     @height.deleter
#     def height(self):
#         print("hight from deleter")
#         def self._height
#         self._height = None #замовчування
#
# resizer = ImageResizer(0, 0, 1200, 1600)
# resizer.width = 100
# print(resizer.width)
# # resizer.height = 300
# # print(resizer.height)
# del resizer.height

#чому в мене не працює deleter??



