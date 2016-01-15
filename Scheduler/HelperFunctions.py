from sys import stderr

def check_parameters(src_params, man_params=[], opt_params=[]):
    intersect = set(src_params) & set(man_params)
    man_check = intersect == set(man_params)
    if not man_check:
        print >>stderr, 'Mandatory parameters cannot be specified correctly'
        print >>stderr, 'List of mandatory parameters:'
        print >>stderr, man_params
        return False

    diff = set(src_params) - set(man_params)
    opt_check = not (diff - set(opt_params))
    if not opt_check:
        print >>stderr, 'Optional parameters cannot be specified correctly'
        print >>stderr, 'List of optional parameters:'
        print >>stderr, opt_params
        return False

    return True

def valid_parameter(src_params, dest_params):
    return not (set(src_params) - set(dest_params))


def