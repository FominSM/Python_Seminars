# 1. Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# - Преобразуйте его в дату в текущем году.
# - Логируйте ошибки, если текст не соответсвует формату.
# - Добавьте возможность запуска из командной строки.
# - Научите функцию распознавать не только текстовое названия дня недели и месяца, но и числовые, т.е не мая, а 5.

# * При этом значение любого параметра можно опустить. В этом случае берётся первый в месяце день недели, 
#   текущий день недели и/или текущий месяц.


import argparse, logging
from datetime import datetime, timedelta

FORMAT = '{levelname} - {asctime}. В модуле "{name}" в строке {lineno:03d} функция "{funcName}()", сообщение: {msg}'
logging.basicConfig(filename='parsing_and_date_translation.log', format= FORMAT, level=logging.INFO , filemode='a', encoding='utf-8', style='{')
logger = logging.getLogger(__name__)

def command_line_data_parser():
    parser = argparse.ArgumentParser(description='Argument parser')
    parser.add_argument('line_str', metavar='L', type=str, nargs='*', help='enter a line of text - 1 четверг ноября \\ 1 4 11')
    args = parser.parse_args()

    mode_work = 0
    
    for item_ in args.line_str:
        if item_.isdigit():
            mode_work += 1
        else:
            mode_work = 0

    if len(args.line_str) == 3:
        num, day, month = args.line_str
        result = date_parser(num, day, month, mode_work)
        print(f'{num} {day} {month} - это {result}')
    else:
        logger.error('Неккоректное количество входных данных')


def date_parser(num, day, month, mode):
    
    days_of_the_week = {'понедельник':0,
                        'вторник':1,
                        'среда':2,
                        'четверг':3,
                        'пятница':4,
                        'суббота':5,
                        'воскресенье':6}
    
    months = {'янв': 1, 
              'фев': 2,
              'мар': 3,
              'апр': 4,
              'мая': 5,
              'июн': 6,
              'июл': 7,
              'авг': 8,
              'сен': 9,
              'окт': 10,
              'ноя': 11,
              'дек': 12}
    
    if 1 <= int(num) <= 4:
        day_week_number = int(num)
    else:
        logger.error('Неккоректное значение порядкового номера дня недели')
        return 'Error'
    
    match mode:
        case 0:
            if day in days_of_the_week.keys():
                day_of_week = days_of_the_week[day]
            else:
                logger.error('Неккоректное значение дня недели')
                return 'Error'
            if month[:3] in months.keys():
                month_ = months[month[:3]]
            else:
                logger.error('Неккоректное значение месяца')
                return 'Error'
        case 3:
            if 1 <= int(day) <= 7:
                day_of_week = int(day) - 1
            else:
                logger.error('Неккоректное значение дня недели')
                return 'Error'
            if 1 <= int(month) <= 12:
                month_ = int(month)
            else:
                logger.error('Неккоректное значение месяца')
                return 'Error'

        
    working_date = datetime(year=2023, month=month_, day=1)
    date_difference = timedelta(days=1)
    COUNT = 30
    working_day_week = 0
    
    while COUNT != 0:
        if working_date.weekday() == day_of_week:
            working_day_week +=1
            if working_day_week == day_week_number:
                result_txt = f'Успешная работа функции - "{num} {day} {month}" - {working_date}' 
                logger.info(result_txt) 
                return working_date
            COUNT -= 1
            working_date += date_difference   
        else:
            working_date += date_difference
            COUNT -= 1
    logger.error('Неккоректные данные')

    

if __name__ == '__main__':
    command_line_data_parser()
    