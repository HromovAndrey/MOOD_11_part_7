#Завдання 1
#Створіть клас Calculator, який може виконувати
#операції додавання, віднімання, множення та ділення.
#Кожна операція буде реалізована як метод класу.
#Об'єкт класу Calculator буде функтором, що може
#викликатися для виконання обраної операці
class Calculator:
    @classmethod
    def add(cls, x, y):
        return x + y

    @classmethod
    def subtract(cls, x, y):
        return x - y

    @classmethod
    def multiply(cls, x, y):
        return x * y

    @classmethod
    def divide(cls, x, y):
        if y == 0:
            raise ValueError("На нуль дилити не можна")
        return x / y

    @classmethod
    def sum(cls, x, y):
        return cls.add(x, y)
result = Calculator.sum(10, 5)
print(result)

