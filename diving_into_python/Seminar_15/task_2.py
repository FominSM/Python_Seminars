# 2. Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

import logging
import argparse


def abs_path(abs_path: str) -> tuple:
    result = []
    result.append(abs_path)
    for_result = abs_path.split('\\')
    result.append(for_result[-1])
    for_result2 = for_result[-1].split('.')
    result.append(for_result2[-1])
    logging.basicConfig(filename='path.log', filemode='a', encoding='utf-8', level=logging.DEBUG)
    logging.info(str(result))
    return tuple(result)


my_string = r"C:\\Users\Star\PycharmProjects\Education_Python\Homework\test.py"

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Парсер для определения пути к файлу, файла и его расширения')
    parser.add_argument('path', metavar='path for file', type=str, nargs='+', help='Enter path')
    args = parser.parse_args()
    print(abs_path(*args.path))