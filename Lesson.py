# Завдання 5
#  Створіть клас Multiplier, який при ініціалізації
# отримує множник. Забезпечте можливість викликати
# цей об'єкт з аргументом та повертати множене
# значення.

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        new_value = value - (value * self.factor)
        return  new_value

multiplier = Multiplier(5)

result = multiplier(10)
print("Result:", result)

result = multiplier(7)
print("Result:", result)


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