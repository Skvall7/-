"""
Задание 6. На закрепление навыков работы с очередью

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте класс-структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются
на корректировку решения
3) список решенных задач, куда задачи перемещаются из базовой очереди или
очереди на доработку

После реализации структуры, проверьте ее работу на различных сценариях

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""


class QueueClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def to_queue(self, item):
        self.elems.insert(0, item)

    def from_queue(self):
        return self.elems.pop()

    def size(self):
        return len(self.elems)


class TaskBoard:
    def __init__(self):
        self.main_qu = QueueClass()
        self.second_qu = QueueClass()
        self.complete = []

    def complete_task(self):
        task = self.main_qu.from_queue()
        self.complete.append(task)
        return

    def for_revision_task(self):
        task = self.main_qu.from_queue()
        self.second_qu.to_queue(task)
        return

    def add_queue(self, item):
        self.main_qu.to_queue(item)
        return

    def from_revision(self):
        tusk = self.second_qu.from_queue()
        self.main_qu.to_queue(tusk)
        return

    def current_tusk(self):
        if not self.main_qu.elems:
            return None
        return self.main_qu.elems[len(self.main_qu.elems) - 1]

    def current_revision_tusk(self):
        if not self.second_qu.elems:
            return None
        return self.second_qu.elems[len(self.second_qu.elems) - 1]


if __name__ == '__main__':
    board = TaskBoard()
    board.add_queue('первая')
    board.add_queue('вторая')
    board.for_revision_task()
    print(board.current_revision_tusk())
    print(board.current_tusk())
    board.complete_task()
    print(board.current_tusk())
    print(board.complete)
    board.from_revision()
    print(board.current_tusk())
    print(board.current_revision_tusk())
    print(board.complete)


