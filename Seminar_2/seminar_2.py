
# 1. Напишите программу банкомат.
# - Начальная сумма равна нулю. Допустимые действия: пополнить, снять, выйти
# - Сумма пополнения и снятия кратны 50 у.е.
# - Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# - После каждой третей операции пополнения или снятия начисляются проценты - 3%
# - Нельзя снять больше, чем на счёте
# - При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# - Любое действие выводит сумму денег


# def refill_withdraw(balance, count, mode, commission):
#     money_commission = 0 + commission

#     while True:
#         money = int(input('Введите сумму пополнения (кратную 50): '))
#         if money % 50 == 0:
#             break
#         else:
#             print('Повторите попытку')

#     if count == 3: 
#         money_commission += 0.03

#     match mode:
#         case 1:
#             balance += (money - (money * money_commission))
#         case 2:
#             if money > balance:
#                 print('Ошибочная операция!')
#                 return balance
#             if money * (0.015 + money_commission) <= 30:
#                 balance -= (money + 30)
#             elif money * (0.015 + money_commission) >= 600:
#                 balance -= (money + 600)
#             else:
#                 balance -= (money + (money * (0.015 + money_commission)))

#     return balance



# balance = 0
# number_operations = 0
# money_commission = 0

# while True:
#     print(f'\nВведите номер операции:\n'
#       '1. Пополнить счет\n'
#       '2. Снять деньги\n'
#       '3. Показать баланс\n'
#       '4. Выйти\n')
    
#     mode = int(input('Введите номер операции: ')) 

#     if balance >= 5_000_000:
#         money_commission = 10

#     match mode:
#         case 1:
#             balance = refill_withdraw(balance, number_operations, mode, money_commission)
#             number_operations += 1
#         case 2:
#             if balance != 0:
#                 balance = refill_withdraw(balance, number_operations, mode, money_commission)
#                 number_operations += 1
#             else:
#                 print('Нулевой баланс!')
#         case 3:
#             print(f'Ваш баланс: {balance}')
#         case 4:
#             break



# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйтe для проверки своего результата.

# def recalculation_number_system(number):
#     string_to_translate = '0123456789ABCDEF'
#     result = ''
#     notation = 16

#     while number > 0:
#         result = string_to_translate[number % notation] + result
#         number //= notation

#     return result
    
# print('Итог - ', recalculation_number_system(int(input('Введите число для перевода в 16-ю систему счисления: '))))



# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. 
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

# def fraction_conversion(number):
#     numerator, denominator = number.split('/')
#     return int(numerator), int(denominator)


# def reduction(nom, den):
#     def all_devs(number):
#         all_dev = set()
#         for dev in range(1, number // 1 + 1):
#             if not number % dev:
#                 all_dev.add(dev)
#         return all_dev 
    
#     nom_dev = all_devs(nom)
#     den_dev = all_devs(den)
#     reduct = max(nom_dev.intersection(den_dev))

#     return str(nom // reduct), str(den // reduct)


# def summ(first_number, second_number):
#     first, second = fraction_conversion(first_number), fraction_conversion(second_number)
    
#     if first[1] == second[1]:
#         nom = first[0] + second[0]
#         den = first[1]
#         return '/'.join(reduction(num, den))
#     else:
#         nom = first[0] * second[1] + first[1] * second[0]
#         den = first[1] * second[1]
#         return '/'.join(reduction(nom, den))


# def multi(first_number, second_number):
#     first, second = fraction_conversion(first_number), fraction_conversion(second_number)
#     nom = first[0] * second[0]
#     den = first[1] * second[1]
#     return '/'.join(reduction(nom, den))


# first_number = input('Введите первую дробь в формате a/b: ')
# second_number = input('Введите вторую дробь в формате a/b: ')

# print(f'Summa: {summ(first_number, second_number)}')
# print(f'Multiplication: {multi(first_number, second_number)}')
