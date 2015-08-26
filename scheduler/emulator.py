from collections import namedtuple, deque


EmulatorTask = namedtuple(
    'EmulatorTask',
    'task duration complete_target_set additional_task_id_queue'
)

from .scheduler import Scheduler


class Emulator:
    def __init__(self, config, initial_task_id_queue, thread_count):
        assert thread_count > 0
        self._scheduler = Scheduler()
        self._thread_count = thread_count

        self._config = config
        self._queue = deque()

        self._time = 0

        self._scheduler.extend([(self._config[initial_task_id].task, self._config[initial_task_id].complete_target_set) \
                                for initial_task_id in initial_task_id_queue])
        self._print('initial')

    def loop(self):
        while self._scheduler or self._queue:
            self._extend_queue()

            if self._queue:
                self._process_next_unit()

    def _extend_queue(self):

        while len(self._queue) < self._thread_count:
            if not self._scheduler:
                break

            self._add_unit()

    def _add_unit(self):
        task = next(self._scheduler)

        self._print('started task'.upper(), task.id)

        end_time = self._time + self._config[task.id].duration

        unit = end_time, task

        self._queue.append(unit)

    def _process_next_unit(self):

        end_time, task = self._queue.pop()

        self._print('finished task'.upper(), task.id)

        self._time = end_time
        self._scheduler(task)

        self._scheduler.extend(
            tuple(
                self._config[additional_task_id].task
                for additional_task_id
                in self._config[task.id].additional_task_id_queue
            ),
            self._config[task.id].complete_target_set
        )

    def _get_next_unit(self):
        result = min(self._queue, key=lambda unit: unit[0])

        self._queue.remove(result)

        return result

    def _print(self, *args):
        print('time', self._time, *args)
