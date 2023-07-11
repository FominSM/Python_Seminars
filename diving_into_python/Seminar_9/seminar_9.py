# Напишите следующие функции:
# - Нахождение корней квадратного уравнения
# - Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# - Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# - Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import json
import random
import csv
from typing import Callable
"""Для корректной работы программы в начале надо запустить csv_writer для записи значений в файл"""

# функция для записи csv файла


def csv_writer():
    with open('number_for_decorator.csv', 'a', newline='') as csvfile:
        writer_csv = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in range(100, 1000):
            list_for_csv = [i for i in range(1, 100)]
            random.shuffle(list_for_csv)  # перемешиваем список
            csv_list = random.sample(list_for_csv, k=3)  # выбираем здесь три случайных числа из списка
            writer_csv.writerow(csv_list)


def csv_reader():
    with open('number_for_decorator.csv', newline='') as csvfile:
        reader_csv = csv.reader(csvfile, delimiter=' ', quotechar='|')
        when_stop = random.randint(1, 900)  # с какой строчки взять 3 числа
        count = 0
        for row in reader_csv:
            count += 1
            if count == when_stop:
                return row


def main(func: Callable):
    def wrapper(*args, **kwargs):
        csv_reader()  # эта функция возвращает список из 3-ех чисел
        result = func(int(csv_reader()[0]), int(csv_reader()[1]), int(csv_reader()[2]))
        print(f'Результат функции {func.__name__}: {result}')
        # запись в csv файл
        with open("sqrt.csv", mode="a", encoding='utf-8') as w_file:
            file_writer = csv.writer(w_file, delimiter=" ", lineterminator="\r")
            file_writer.writerow(result)
        # запись в JSON файл
        to_json = {"Roots": result}
        with open('to_json.json', 'a', encoding='utf-8') as f:
            json.dump(to_json, f, sort_keys=True, indent=2)

        return result

    return wrapper


def factorial(n: int) -> int:
    f = 1
    for i in range(2, n + 1):
        f *= i
        return f


@main
def find_sqrt(a: int = None, b: int = None, c: int = None):
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return f'No roots {d =}'
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x2, x1


if __name__ == '__main__':
    find_sqrt()