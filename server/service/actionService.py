from .gamestate.drawingPhase import *
from .gamestate.inPlay import *
from ..constants import *
from dao import gamestateDao


def in_hand(find, hand):
    for idx, card in enumerate(hand):
        if find['suit'] == card['suit'] and find['card']['val'] == card['card']['val']:
            return {'found': True,
                    'location': idx}
    return {'found': False,
            'location': -1}


def discard(position, cards):
    gamestate = gamestateDao.get_gamestate()
    for card in cards:
        hand_info = in_hand(card, gamestate['player'][position]['hand'])
        if hand_info['found']:
            gamestate['discard'].append(card)
            del gamestate['players'][position]['hand'][hand_info['location']]
        else:
            return {'error': True,
                    'message': "Card not in player's hand"}
    return {'error': False,
            'message': "Cards have been added to discard pile"}


def draw(posn, card):
    gamestate = drawing_phase
    hand_info = in_hand(card, gamestate['deck'])
    if hand_info['found']:
        gamestate['player'][posn]['hand'].append(card)
        del gamestate['deck'][hand_info['location']]
        return {'error': False,
                'message': "Card removed from deck and added to player's hand"}
    else:
        return {'error': True,
                'message': "Card not in deck"}


def declare(card):
    gamestate = drawing_phase
    if card['suit'] == "NONE":
        return {'error': True,
                'message': "Cannot declare card with NONE suit"}
    elif gamestate['trump']['val'] != card['val']:
        return {'error': True,
                'message': "Cannot declare non-trump valued card"}
    else:
        gamestate['trump']['suit'] = card['suit']
        return {'error': False,
                'message': "A suit has been declared for the round"}


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
    gamestate = in_play
    sorted_cards = sorted(cards, key=lambda k: k['val'])
    for card in cards:
        hand_info = in_hand(card, gamestate['player'][posn]['hand'])
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
