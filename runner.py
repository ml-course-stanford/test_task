import yaml

from scheduler.emulator import EmulatorTask, Emulator
from scheduler.scheduler import Task


def load_config(data):
    return {
        task_id: EmulatorTask(
            Task(
                task_id,
                config.get('priority', 0),
                frozenset(config.get('target_set', [])),
                frozenset(config.get('read_set', [])),
                frozenset(config.get('write_set', []))
            ),
            config.get('duration', 0),
            frozenset(config.get('complete_target_set', [])),
            tuple(config.get('additional_task_id_queue', []))
        )
        for task_id, config in data.items()
    }


CASE_ID = 1

with open('case_{}.yaml'.format(CASE_ID)) as file:
    case = yaml.load(file)

emulator = Emulator(
    load_config(case['config']),
    tuple(case['initial_task_id_queue']),
    case.get('thread_count', 1)
)

emulator.loop()
