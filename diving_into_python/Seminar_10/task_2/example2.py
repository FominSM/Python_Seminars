# 2. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.

from random import randint as ran

class Element:

    def __init__(self, initial_list):
        self._initial_list = initial_list
    
    def filter(self):
        self.result_list = []
        for self.number in self._initial_list:
            if self._initial_list.count(self.number) >= 2 and self.number not in self.result_list:
                self.result_list.append(self.number)

    def get_list(self):
        return self.result_list

example = Element([ran(9,21) for i in range(15)])
example.filter()
print(example.result_list)
