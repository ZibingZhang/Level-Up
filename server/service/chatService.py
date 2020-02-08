from dao import messageDao, playersDao


def add_message(player_name, message):
    messageDao.add_message(player_name, message)


def command(cmd, params):
    if cmd == "join":
        result = _join(params)
    elif cmd == "reset":
        result = _reset()
    else:
        result = {}

    result['type'] = "command"
    result['command'] = cmd
    if 'error' not in result:
        result['error'] = False
    return result


def _join(params):
    if len(params) != 2:
        return {'error': True,
                'message': 'Incorrect number of arguments'}

    position = params[0].upper()
    player_name = params[1]

    if player_name.upper() in [player_name.upper() for player_name in playersDao.get_player_names()]:
        return {'error': True,
                'message': "Player name already taken"}
    elif position not in ["N", "E", "S", "W"]:
        return {'error': True,
                'message': "Invalid position"}
    elif len(player_name) < 3:
        return {'error': True,
                'message': "Player name must be at least 3 characters long"}
    else:
        playersDao.add_player(position, player_name)
        return {'message': "You have joined the game"}


def _reset():
    playersDao.reset()
    return {'message': 'You have reset the game'}

