from dao import gamestateDao
from ._util import \
    _card_to_string, \
    _in_cards, \
    _check_style, \
    _check_suits, \
    _round_over
from constants import GAME_STATE


def play(position, cards):
    gamestate = gamestateDao.get_gamestate()
    if len(cards) > 2:
        return {'error': True,
                'message': "More than two cards cannot be played (currently)"}
    sorted_cards = sorted(cards, key=lambda k: k['val'])
    for card in cards:
        hand_info = _in_cards(card, gamestate['player'][position]['hand'])
        if hand_info['found']:
            gamestate['discard'].append(card)
            del gamestate['players'][position]['hand'][hand_info['location']]
        else:
            return {'error': True,
                    'message': "Card not in player's hand"}
    if _check_suits(gamestate, position, cards)['error']:
        return _check_suits(gamestate, cards)
    else:
        if _check_style(gamestate, sorted_cards)['error']:
            return _check_style(gamestate, sorted_cards)
    if _round_over(gamestate):
        gamestate['status'] = GAME_STATE['between rounds']
        gamestateDao.set_gamestate(gamestate)
        return {'error': False,
                'message': "Round is over, waiting for players to ready up",
                'cards': [_card_to_string(card) for card in cards]}
    else:
        gamestateDao.set_gamestate(gamestate)
        return {'error': False,
                'message': "Cards have been played",
                'cards': [_card_to_string(card) for card in cards]}