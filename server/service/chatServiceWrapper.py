from dao import playersDao


def require_host(func):
    def decorated(*args, **kwargs):
        if playersDao.get_position(kwargs['player_name']) != "N":
            return {'error': True,
                    'message': 'Must be host to execute command'}
        else:
            return func(*args)
    return decorated
