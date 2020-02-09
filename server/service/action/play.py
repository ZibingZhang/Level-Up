from dao import gamestateDao
from ._util import \
    _card_to_string, \
    _in_cards, \
    _check_style, \
    _check_suits, \
    _round_over, \
    _trick_over, \
    _assign_points, \
    _check_valid
from constants import \
    GAME_STATE, \
    LETTER_TO_POSITION_KEY


def play(position, cards):
    gamestate = gamestateDao.get_gamestate()
    player_current_play = gamestate['trick']['current_play'][LETTER_TO_POSITION_KEY[position.upper()]]['cards']
    if len(cards) > 2:
        return {'error': True,
                'message': "More than two cards cannot be played (currently)"}
    for card in cards:
        hand_info = _in_cards(card, gamestate['player'][position]['hand'])
        if hand_info != -1:
            player_current_play.append(card)
            del gamestate['players'][position]['hand'][hand_info]
        else:
            return {'error': True,
                    'message': "Card not in player's hand"}
    validity = _check_valid(gamestate, position, cards)
    if validity['error']:
        gamestate['players'][LETTER_TO_POSITION_KEY[position.upper()]]['cards'].extend(cards)  # need to copy cards?
        return validity
    if _trick_over(gamestate):
        _assign_points(gamestate)
        gamestateDao.set_gamestate(gamestate)
        return {'error': False,
                'message': gamestate['trick']['starter'] + " has won the trick!",
                'cards': [_card_to_string(card) for card in cards]}
    if _round_over(gamestate):
        gamestate['status'] = GAME_STATE['between rounds']
        gamestateDao.set_gamestate(gamestate)
        return {'error': False,
                'message': "Round is over, waiting for players to ready up",
                'cards': [_card_to_string(card) for card in cards]}
    else:
        gamestateDao.set_gamestate(gamestate)
        return {'error': False,
                'message': "Card(s) have been played",
                'cards': [_card_to_string(card) for card in cards]}