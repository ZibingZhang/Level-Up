from dao import messageDao, playersDao
from constants import COMMAND


# Assume the host is N


def add_message(player_name, message):
    messageDao.add_message(player_name, message)


def command(cmd, params):
    if cmd == COMMAND['join']:
        result = _join(params)
    elif cmd == COMMAND['reset']:
        result = _reset()
    elif cmd == COMMAND['host']:
        result = _host(params)
    else:
        result = {'error': True,
                  'message': 'Unknown command'}

    result['type'] = "COMMAND"
    result['command'] = cmd.upper()
    return result


def _join(params):
    if len(params) != 2:
        return {'error': True,
                'message': "Incorrect number of arguments"}

    position = params[0].upper()
    player_name = params[1]

    if not playersDao.has_host():
        return {'error': True,
                'message': 'There is no game to join'}
    elif position in playersDao.get_positions():
        return {'error': True,
                'message': 'Position already taken'}
    elif player_name.upper() in [player_name.upper() for player_name in playersDao.get_names()]:
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
        return {'error': False,
                'message': "You have joined the game",
                'playerName': player_name}


def _reset():
    playersDao.reset()
    messageDao.reset()
    return {'error': False,
            'message': 'You have reset the game'}


def _host(params):
    if len(params) != 1:
        return {'error': True,
                'message': "Incorrect number of arguments"}
    player_name = params[0]

    if len(playersDao.get_names()) != 0:
        return {'error': True,
                'message': "Game already in progress"}
    else:
        playersDao.add_player("N", player_name)
        return {'error': False,
                'message': "You are hosting a game",
                'playerName': player_name}

