from collections import namedtuple

Task = namedtuple('Task', 'id priority target_set read_set write_set')


class Scheduler:

    def extend(self, task_queue, target_set=frozenset()):

        try:
            self._task_queue += tuple(task_queue)
        except AttributeError as err:
            self.__setattr__('_task_queue', tuple(task_queue))
            self.__setattr__('_i', -1)

    def __bool__(self):

        if len(self._task_queue) !=0:
            return True

        return False

    def __iter__(self):
        return iter(self._task_queue)

    def __next__(self):

        if self._i < len(self._task_queue)-1:
            self._i +=1
            return self._task_queue[self._i]
        else:
            raise StopIteration

    def __call__(self, task):
        pass

