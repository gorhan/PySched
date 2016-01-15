import Task

class TaskGenerator(type):
    def __call__(self, *args, **kwargs):
        task = Task(*args, **kwargs)
        if not task.instance_valid():
            return None
        return task

class MetaTask:
    __metaclass__ = TaskGenerator
    def __init__(self, *args, **kwargs):
        self.__valid = True