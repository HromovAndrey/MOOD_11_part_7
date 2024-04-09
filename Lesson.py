#Завдання 2
#Створіть дескриптор для атрибуту, що зберігає
#розмір файлу. Додайте можливість зберігати розмір
#файлу в байтах, але представляти його у зручному для
#читання форматі (наприклад, КБ або МБ).
class FileSizeDescriptor:
    def __init__(self, size_bytes=0):
        self.size_bytes = size_bytes

    def __get__(self, instance, owner):
        return self.size_bytes

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Розмір файлу не може бути від'ємним")
        self.size_bytes = value

    def formatted_size(self):
        if self.size_bytes < 1024:
            return f"{self.size_bytes} B"
        elif self.size_bytes < 1024 * 1024:
            return f"{self.size_bytes / 1024:.2f} KB"
        else:
            return f"{self.size_bytes / (1024 * 1024):.2f} MB"

class File:
    size = FileSizeDescriptor()

file = File()
file.size = 2048
print("Розмір файлу:", file.size)
print("Форматований розмір файлу:", file.size.formatted_size())
