# 1. Доработаем задачи 5-6. Создайте класс-фабрику.
# - Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# - Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.


class Animal:
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def print_specific(self):
        return f'Специфические данные'


class Dog(Animal):
    def __init__(self, name:str=None, breed:str='unknown', age:int=1, commands: list[str] = 'unknown'):
        super().__init__(name, breed, age)
        self.commands = commands

    def print_specific(self):
        return f'{self.commands}'


class Fish(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', age:int=1, count_fins: int = 0):
        super().__init__(name, breed, age)
        self.count_fins = count_fins

    def print_specific(self):
        return f'{self.count_fins}'


class Bird(Animal):
    def __init__(self, name: str = None, breed: str = 'unknown', age:int=1, count_flights: int = 0):
        super().__init__(name, breed, age)
        self.count_flights = count_flights

    def print_specific(self):
        return f'{self.count_flights}'


class Animal_factory:
    def __init__(self, name):
        self.name = name

    def add_animal(self):
        while True:
            choice = input('Введите тип животного "Dog, Fish, Bird": ')
            if choice == 'Dog':
                name = input('Введите имя собаки: ')
                dog = Dog(name)
                print(dog.name)
            elif choice == 'Fish':
                name = input('Введите имя рыбки: ')
                fish = Fish(name)
                print(fish.name)
            elif choice == 'Bird':
                name = input('Введите имя птички: ')
                bird = Bird(name)
                print(bird.name)
            else:
                print('Мы не можем создать такое животное, попробуйте еще раз')


if __name__ == '__main__':
    example1 = Animal_factory('test')
    example1.add_animal()
  