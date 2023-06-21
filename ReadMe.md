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

3. Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки.