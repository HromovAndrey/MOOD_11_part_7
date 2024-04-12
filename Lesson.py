# Завдання 4
# Створіть клас для представлення користувача з
# атрибутами: ім'я та вік. Додайте властивості для
# валідації віку користувача. Наприклад, вік повинен
# бути у межах від 0 до 120.
class User:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")
        if value < 0 or value > 120:
            raise ValueError("Age must be between 0 and 120")
        self._age = value


user = User("John", 25)
print("Name:", user.name)
print("Age:", user.age)
user.age = 30
print("New Age:", user.age)

user.age = 150

# s_strok = " "
# s_list = []
# s_number = 0
# a = [5, 3, "hello", [3,4], "world", [5], 10.5]
# for i in a:
#     if isinstance(i,str):
#         s_strok = s_strok + i
#     elif isinstance(i, list):
#         s_list = s_list + i
#     elif isinstance((i, (int, float))):
#         s_number = s_number + i
#
# print(s_strok)
# print(s_list)
# print(s_number)