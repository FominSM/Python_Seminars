# Задание №2
# Создайте класс Архив, который хранит пару свойств. Например, число и строку. При нового экземпляра класса, 
# старые данные из ранее созданных экземпляров сохраняются в пару списков архивов list-архивы также являются свойствами экземпляра

class Archive:
    """Документация класса 'Архив', который хранит пару свойств и старые данные из ранее созданных экземпляров сохраняются
       в список-атрибут экземпляра класса"""

    _instance = None
    _archive = []

    def __new__(cls, name: str, age: int):
        instance = super().__new__(cls)
        if cls._instance:
            cls._archive.append(cls._instance)
        cls._instance = instance
        instance.archive = cls._archive.copy()
        return instance

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.age}'

    def __str__(self):
        return f'Пример - {self.name}\nданные в архиве - {self.archive}'



example1 = Archive('test1', 10)
example2 = Archive('test2', 20)
example3 = Archive('test3', 30)

print(example3.archive)
print(example2)
help(Archive)