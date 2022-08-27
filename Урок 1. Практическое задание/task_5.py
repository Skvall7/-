"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""


class Plates:
    def __init__(self):
        self.lst = [[]]
        self.stack = 3

    # def __str__(self):
    #     return str(self.lst)

    def is_empty(self):
        return self.lst == []

    def push_in(self, ls):
        if len(self.lst[len(self.lst) - 1]) < self.stack:
            self.lst[len(self.lst) - 1].append(ls)
        else:
            self.lst.append([])
            self.lst[len(self.lst) - 1].append(ls)

    def pop_out(self):
        out = self.lst[len(self.lst) - 1].pop()
        if len(self.lst[len(self.lst) - 1]) == 0:
            self.lst.pop()
        return out

    def get_val(self):
        return self.lst[len(self.lst) - 1]

    def stack_size(self):
        return len(self.lst)


if __name__ == '__main__':
    plates = Plates()
    for n in range(100):
        plates.push_in(n)

    print(plates.stack_size())
    print(plates.get_val())
    print(plates.pop_out())
    print(plates.pop_out())
