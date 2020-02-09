from dao import gamestateDao
from ._util import _in_cards, _card_to_string
from constants import \
    LETTER_TO_POSITION_KEY, \
    GAME_STATE


def discard(position, cards):
    gamestate = gamestateDao.get_gamestate()

    for card in cards:
        hand_info = _in_cards(card, gamestate['player'][LETTER_TO_POSITION_KEY[position.upper()]]['hand'])
        if hand_info['found']:
            del gamestate['players'][LETTER_TO_POSITION_KEY[position.upper()]]['hand'][hand_info['location']]
        else:
            return {'error': True,
                    'message': "Card not in player's hand"}
    gamestate['status'] = GAME_STATE['in play']
    gamestateDao.set_gamestate(gamestate)
    return {'error': False,
            'position': position,
            'cards': [_card_to_string(card) for card in cards]}