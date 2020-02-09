from dao import messageDao, playersDao, gamestateDao
from constants import COMMAND, GAME_STATE, INITIAL_GAME_STATE
from service import chatServiceWrapper
from service import actionService


# Assume the host is N


def add_message(player_name, message):
    messageDao.add_message(player_name, message)


def command(cmd, params, **kwargs):
    if cmd == COMMAND['join']:
        result = _join(params)
    elif cmd == COMMAND['reset']:
        result = _reset()
    elif cmd == COMMAND['host']:
        result = _host(params)
    elif cmd == COMMAND['rejoin']:
        result = _rejoin(params)
    elif cmd == COMMAND['start']:
        result = _start(params)
    # ACTIONS
    elif cmd == COMMAND['action']['draw']:
        result = _draw(params, player_name=kwargs['player_name'])
    elif cmd == COMMAND['action']['discard']:
        result = _discard(params, player_name=kwargs['player_name'])
    elif cmd == COMMAND['action']['play']:
        result = _play(params, player_name=kwargs['player_name'])
    elif cmd == COMMAND['action']['declare']:
        result = _declare(params, player_name=kwargs['player_name'])
    else:
        result = {'error': True,
                  'message': 'Unknown command'}

    result['type'] = "COMMAND"
    result['command'] = cmd.upper()
    return result


def get_next_messages(message_id):
    largest_id = messageDao.get_largest_id()
    if message_id != -1 and message_id < largest_id:
        return {
            'messages': messageDao.get_next_messages(message_id),
            'messageId': messageDao.get_largest_id()
        }
    else:
        return {
            'messages': [],
            'messageId': message_id
        }


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
                'playerName': player_name,
                'position': position,
                'messageId': messageDao.get_largest_id()}


def _reset():
    playersDao.reset()
    messageDao.reset()
    gamestateDao.reset()
    return {'error': False,
            'message': "You have reset the game"}


def _host(params):
    if len(params) != 1:
        return {'error': True,
                'message': "Incorrect number of arguments"}

    player_name = params[0]
    position = "N"

    if len(playersDao.get_names()) != 0:
        return {'error': True,
                'message': "Game already in progress"}
    else:
        playersDao.add_player(position, player_name)
        gamestateDao.set_gamestate({
            'status': GAME_STATE['not started']
        })
        return {'error': False,
                'message': "You are hosting a game",
                'playerName': player_name,
                'position': position,
                'messageId': messageDao.get_largest_id()}


def _rejoin(params):
    if len(params) != 1:
        return {'error': True,
                'message': "Incorrect number of arguments"}

    position = params[0].upper()

    if not playersDao.has_host():
        return {'error': True,
                'message': "There is no game to rejoin"}
    elif position not in playersDao.get_positions():
        return {'error': True,
                'message': "Position not already initially joined"}
    else:
        return {'error': False,
                'message': "You have rejoined the game",
                'playerName': playersDao.get_player_name(position),
                'position': position,
                'messageId': messageDao.get_largest_id()}


# @chatServiceWrapper.require_host
def _start(params):
    if len(params) != 0:
        return {'error': True,
                'message': "Incorrect number of arguments"}
    elif not all([position in playersDao.get_positions() for position in ["N", "E", "S", "W"]]):
        return {'error': True,
                'message': "Not enough players to start game"}
    elif gamestateDao.get_gamestate()['status'] != GAME_STATE['not started']:
        return {'error': True,
                'message': "Cannot start the game during a game"}
    else:
        gamestateDao.set_gamestate(INITIAL_GAME_STATE['drawing'])
        return {'error': False,
                'message': "You have started the game"}


@chatServiceWrapper.require_host
def _draw(params):
    if len(params) != 1:
        return {'error': True,
                'message': "Incorrect number of arguments"}

    position = params[0]

    return actionService.draw(position)


@chatServiceWrapper.require_host
def _discard(params):
    return {}


@chatServiceWrapper.require_host
def _play(params):
    return {}


@chatServiceWrapper.require_host
def _declare(params):
    return {}
