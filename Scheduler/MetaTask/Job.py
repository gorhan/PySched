
class Job:
    opt_params = [
    ]
    man_params = [
        'release_time',
        'deadline',
        'parent'
    ]
    int_params = [
    ]

    def __init__(self, *args, **kwargs):
        from Scheduler.HelperFunctions import check_parameters
        if not check_parameters(kwargs.keys(), self.__class__.man_params, self.__class__.opt_params):
            self.__valid = False
            return None

        self.__params = dict()
        for param, value in kwargs.items():
            self.__params[param] = value

