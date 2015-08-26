import queue, sys
from collections import namedtuple


Task = namedtuple('Task', 'id priority target_set read_set write_set')


class Scheduler:

    def extend(self, task_queue, target_set=frozenset()):

        try:
            self._intern_queue

        except AttributeError as err:

            self.__setattr__('_intern_queue', queue.PriorityQueue())

        [ self._intern_queue.put(((sys.maxsize-t.priority), t)) for t in tuple(task_queue) ]

    def __bool__(self):

        if self._intern_queue.empty():
            return False

        return True

    def __iter__(self):
        return self

    def __next__(self):

        while(True):
            try:
                priority, task = self._intern_queue.get(block=False)
                return task
            except Empty as err:
                raise StopIteration

    def __call__(self, task):
        pass

