# Курс по Python

### Задания 1 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_1)
1. Решить задачи, которые не успели решить на семинаре:
- Написать программу, которая будет выводить в консоль ёлочку заданной высоты
- Написать порграмму, которая выодит в консоль таблицу умножения "как на тетрадках"

2. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать «больше» или «меньше» после каждой попытки.



### Задания 2 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_2)
1. Напишите программу банкомат.
- Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти
- Сумма пополнения и снятия кратны 50 у.е.
- Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
- После каждой третей операции пополнения или снятия начисляются проценты - 3%
- Нельзя снять больше, чем на счёте
- При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
- Любое действие выводит сумму денег

2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. Функцию hex используйтe для проверки своего результата.

3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.



### Задания 3 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_3)
1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
- Какие вещи взяли все три друга
- Какие вещи уникальны, есть только у одного друга
- Какие вещи есть у всех друзей кроме одного
- имя того, у кого данная вещь отсутствует
- Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

3. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.



### Задания 4 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_4)
1. Напишите функцию для транспонирования матрицы

2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
используйте его строковое представление.

3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.



### Задания 5 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_5)
1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из 
трёх элементов: путь, имя файла, расширение файла.

2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида «10.25%». В результате получаем словарь с 
именем в качестве ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная 
на процент премии

3. Создайте функцию генератор чисел Фибоначчи.



### Задания 6 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_6)
1. В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

2. Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на 
доске, определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел, каждое число от
1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.

* Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.



### Задания 7 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_7)
1. Напишите функцию группового переименования файлов. Она должна:
- принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
- принимать параметр количество цифр в порядковом номере.
- принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
- принимать параметр расширение конечного файла.
- принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.



### Задания 8 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_8)
1. Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
- Для дочерних объектов указывайте родительскую директорию.
- Для каждого объекта укажите файл это или директория.
- Для файлов сохраните его размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.



### Задания 9 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_9)
1. Напишите следующие функции:
- Нахождение корней квадратного уравнения
- Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
- Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
- Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.



### Задания 10 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_10)
1. Доработаем задачи 5-6. Создайте класс-фабрику.
- Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
- Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.

2. Возьмите 1-3 любые задачи из прошлых семинаров которые вы уже решали. Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра. 



### Задания 11 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_11)
1. Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.

2. Создайте класс Матрица. Добавьте методы для: 
- вывода на печать
- сравнения
- сложения
- умножения матриц



### Задания 12 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_12)

1. Cоздайте класс студента. 
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.



### Задания 13 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_13)

1. Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. Напишите к ним классы исключения с выводом подробной информации. Поднимайте исключения внутри основного кода. Например нельзя создавать прямоугольник со сторонами отрицательной длины.



### Задания 14 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_14)

1. Взять класс Матрица (написанный ранее) и написать для него по 3-4 теста каждого вида (PyTest, UnitTest, DocTest)



### Задания 15 [семинара](https://github.com/kremlik144/Python_Seminars/tree/main/diving_into_python/Seminar_15)

1. Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
- Преобразуйте его в дату в текущем году.
- Логируйте ошибки, если текст не соответсвует формату.
- Добавьте возможность запуска из командной строки.
- При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, текущий день недели и/или текущий месяц.
- Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.


2. Возьмите любые 1-3 задачи из прошлых домашних заданий. Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.