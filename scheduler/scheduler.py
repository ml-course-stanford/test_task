import queue, sys
from collections import namedtuple

Task = namedtuple('Task', 'id priority target_set read_set write_set')


class Scheduler:

    def extend(self, task_queue, target_set=frozenset()):

        try:
            self._intern_queue

        except AttributeError as err:

            self.__setattr__('_intern_queue', queue.PriorityQueue())
            self.__setattr__('_targeted_goals', set())

        for el in task_queue:

            task = el
            complete_target_set = set()

            if not isinstance(el, Task):
                task, complete_target_set = el

            if len(complete_target_set)> 0:
                [ self._targeted_goals.add(target_goal) for target_goal in complete_target_set ]

            already_targeted = [ target for target in task.target_set if target in self._targeted_goals ]
            if len(already_targeted)> 0:
                continue

            self._intern_queue.put(((sys.maxsize-task.priority), task))

    def __bool__(self):

        if self._intern_queue.empty():
            return False

        return True

    def __iter__(self):
        return self

    def __next__(self):

        while(True):
            try:
                priority, task = self._intern_queue.get(timeout=5)
                return task
            except Empty as err:
                raise StopIteration

    def __call__(self, task):

        pass

