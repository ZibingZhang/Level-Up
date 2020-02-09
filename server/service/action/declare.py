from dao import gamestateDao
from ._util import _card_to_string
from constants import \
    PLAYER_TO_TEAM


def declare(position, card):
    gamestate = gamestateDao.get_gamestate()
    if card['suit'] == "NONE":
        return {'error': True,
                'message': "Cannot declare card with NONE suit"}
    elif gamestate['team level'][PLAYER_TO_TEAM[position]] != card['value']['rank']:
        return {'error': True,
                'message': "Cannot declare card with value your team is not on"}
    else:
        gamestate['trump']['suit'] = card['suit']
        gamestate['trump']['value'] = gamestate['team level'][PLAYER_TO_TEAM[position]]
        gamestateDao.set_gamestate(gamestate)
        return {'error': False,
                'position': position,
                'card': _card_to_string(card)}