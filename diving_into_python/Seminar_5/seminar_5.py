# 1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из 
# трёх элементов: путь, имя файла, расширение файла.

# import os

# def parse_path(path_file:str) -> tuple:
#     *path, name = path_file.split('\\')
#     result = ['/'.join(path), name.split('.')[0], name.split('.')[1]]
#     return tuple(result)
    

# path_to_file = os.path.abspath('seminar_5.py')
# print(parse_path(path_to_file))



# 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с 
# именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная 
# на процент премии

# names = ['Ivan', 'Sergei', 'Sasha']
# rates = [44_000, 15_000, 34_000]
# premiums = ['10.25%', '22.26%', '33.27%']

# result_dict = {name : (rate * float(premium[:-1])/100) for name, rate, premium in zip(names, rates, premiums)}

# print(result_dict)



# 3. Создайте функцию генератор чисел Фибоначчи (см. Википедию).

# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield a
#         a, b = b, a + b
        

# SIZE = 10

# fib = iter(fibonacci())

# for _ in range(SIZE):
#     print(next(fib))
