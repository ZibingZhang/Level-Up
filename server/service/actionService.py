from .gamestate.drawingPhase import *
from .gamestate.inPlay import *
from ..dao import gamestateDao
from ..constants import LETTER_TO_POSITION_KEY


def _in_cards(find, hand):
    for idx, card in enumerate(hand):
        if find['suit'] == card['suit'] and find['card']['val'] == card['card']['val']:
            return {'found': True,
                    'location': idx}
    return {'found': False,
            'location': -1}


def _card_to_string(card):
    SUIT_TO_STRING[card['suit']] + VAL_TO_STRING[card['value']['rank']]


def _round_over(gamestate):
    for player in gamestate['players'].keys():
        if len(gamestate['players'][player]['cards']) != 0:
            return False
    return True

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


def draw(position):
    gamestate = gamestateDao.get_gamestate()

    if position != gamestate['draw next']:
        return {'error': True,
                'message': "Not your turn to draw"}
    else:
        card = gamestate['deck'].pop(len(gamestate['deck'])) # replace with random card choosing
        gamestate['players'][LETTER_TO_POSITION_KEY[position.upper()]]['hand'].append(card)
        if len(gamestate['deck']) == 8:
            gamestate['status'] = GAME_STATE['discarding']
            gamestateDao.set_gamestate(gamestate)
            return {'error': False,
                    'message': "Now waiting for discarding",
                    'position': position,
                    'card': _card_to_string(card)}  # to replace
        else:
            gamestate['draw next'] = POSITION[DRAW_ORDER[gamestate['draw next']]]
            gamestateDao.set_gamestate(gamestate)
            return {'error': False,
                    'position': position,
                    'card': _card_to_string(card)}  # to replace


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
        gamestate['trump']['value'] = card['value']
        gamestateDao.set_gamestate(gamestate)
        return {'error': False,
                'position': position,
                'card': _card_to_string(card)}


def check_suits(gamestate, posn, cards):
    suit = cards[0]['suit']
    if gamestate['players'][posn]['leading']:
        gamestate['trick']['suit'] = suit
    for card in cards:
        if card['suit'] != suit:
            return {'error': True,
                    'message': "Different suits within play"}
        if card['suit'] != gamestate['trick']['suit']:
            return {'error': True,
                    'message': "Different suit from leading suit"}
    return {'error': False,
            'message': "All suits match"}


def check_style(gamestate, cards):
    # if len(cards) == 6:
    #     if cards[0]['val'] == cards[1]['val'] and cards[2]['val'] == cards[3]['val'] \
    #             and cards[4]['val'] == cards[5]['val'] and cards[1]['val'] + 1 == cards[2]['val'] \
    #             and cards[3]['val'] + 1 == cards[4]['val']:
    #         return {'error': False,
    #                 'message': "Three consecutive pairs played"}
    #     else:
    #         return {'error': True,
    #                 'message': "Invalid play with six cards"}
    # elif len(cards) == 4:
    #     if cards[0]['val'] == cards[1]['val'] and cards[2]['val'] == cards[3]['val'] \
    #             and cards[1]['val'] + 1 == cards[2]['val']:
    #         return {'error': False,
    #                 'message': "Two consecutive pairs played"}
    #     else:
    #         return {'error': True,
    #                 'message': "Invalid play with four cards"}
    if len(cards) == 2:
        if cards[0]['val'] == cards[1]['val']:
            return {'error': False,
                    'message': "Pair played"}
        else:
            return {'error': True,
                    'message': "Invalid play with two cards"}
    else:
        return {'error': False,
                'message': "Single played"}


def play(posn, cards):
    gamestate = gamestateDao.get_gamestate()
    if len(cards) > 2:
        return {'error': True,
                'message': "More than two cards cannot be played (currently)"}
    sorted_cards = sorted(cards, key=lambda k: k['val'])
    for card in cards:
        hand_info = _in_cards(card, gamestate['player'][posn]['hand'])
        if hand_info['found']:
            gamestate['discard'].append(card)
            del gamestate['players'][posn]['hand'][hand_info['location']]
        else:
            return {'error': True,
                    'message': "Card not in player's hand"}
    if check_suits(gamestate, posn, cards)['error']:
        return check_suits(gamestate, cards)
    else:
        if check_style(gamestate, sorted_cards)['error']:
            return check_style(gamestate, sorted_cards)
    return {'error': False,
            'message': "Cards have been played"}
