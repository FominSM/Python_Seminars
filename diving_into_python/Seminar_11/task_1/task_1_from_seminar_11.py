# Задание №1
# Создайте класс Моя Строка, где: будут доступны все возможности str дополнительно
# хранятся имя автора строки и время создания (time.time)

import datetime


class MyString(str):
    """Документация класса, наследуемого от класса str и храняшего атрибуты имени и времени создания"""

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.date = datetime.datetime.now()
        return instance

    def __main__(self):
        return """Документация класса, наследуемого от класса str и храняшего атрибуты имени и времени создания"""

    def __str__(self):
        return f'Имя - {self.name}  Дата создания - {self.date}'


string1 = MyString('test1', 'author1')
print(string1.date)
help(MyString)