from collections import namedtuple


Task = namedtuple('Task', 'id priority target_set read_set write_set')


class Scheduler:
    def extend(self, task_queue, target_set=frozenset()):
        pass

    def __bool__(self):
        pass

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def __call__(self, task):
        pass
