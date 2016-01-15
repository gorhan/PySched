from Job import Job

class Task:
    opt_params = [
        'id',
        'pre_conditions',
        'post_conditions'
    ]
    man_params = [
        'activation_time',
        'wcet',
        'life_cycle',
        'period',
    ]
    int_params = [
        'active_job'
        'parent'
    ]

    def __init__(self, *args, **kwargs):
        from Scheduler.HelperFunctions import check_parameters
        if not check_parameters(kwargs.keys(), self.__class__.man_params, self.__class__.opt_params):
            self.__valid = False
            return None

        self.__params = dict()
        for param, value in kwargs.items():
            self.__params[param] = value

        self.__params['active_job'] = Job(release_time=self.__params['activation_time'], deadline=self.__params['activation_time'] + self.__params['life_cycle'], parent=self)
        self.__params['parent'] = None
        self.__valid = True

    def valid_instance(self):
        return self.__valid

    def get_parameters(self, request):
        from Scheduler.HelperFunctions import valid_parameter
        if valid_parameter(request, self.__class__.opt_params+self.__class__.man_params):
            if type(request) is list:
                ret_params = dict()
                for param in request:
                    ret_params[param] = self.__params[param]
                return ret_params
            else:
                return self.__params[request]
        elif not self.__params['parent']:
            return self.__params['parent'].get_parameters(request)

        return False

    def next_look(self, relative_offset=None):
        period = self.get_parameters('period')
        life_cycle = self.get_parameters('life_cycle')
        release_time = None

        if relative_offset:
            release_time = relative_offset
        else:
            release_time = self.__params['active_job'].get_parameters('release_time')

        new_release_time = release_time + period
        new_dealine_time = new_release_time + life_cycle
        self.__params['active_job'] = Job(release_time=new_release_time, deadline=new_dealine_time, parent=self)