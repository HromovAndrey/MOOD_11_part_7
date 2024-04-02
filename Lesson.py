#Завдання 1
#Створіть клас Calculator, який може виконувати
#операції додавання, віднімання, множення та ділення.
#Кожна операція буде реалізована як метод класу.
#Об'єкт класу Calculator буде функтором, що може
#викликатися для виконання обраної операці
class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def not_divide(self, x, y):
        if y == 0:
            raise ValueError("Неможливо поділити на нуль")
        return x / y


print("Addition:", Calculator.add(6, 4))
print("Subtraction:", Calculator.subtract(8, 2))
print("Multiplication:", Calculator.multiply(7, 1))
print("Division:", Calculator.divide(5, 9))