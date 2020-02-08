from .gamestate.drawingPhase import *
from ..constants import *


def in_hand(find, hand):
    for idx, card in enumerate(hand):
        if find['suit'] == card['suit'] and find['card']['val'] == card['card']['val']:
            return {'found': True,
                    'location': idx}
    return {'found': False,
            'location': -1}


def discard(posn, cards):
    gamestate = drawing_phase
    for card in cards:
        hand_info = in_hand(card, drawing_phase['player'][posn]['hand'])
        if hand_info['found']:
            drawing_phase['discard'].append(card)
            del drawing_phase['players'][posn]['hand'][hand_info['location']]
        else:
            return {'error': True,
                    'message': "Card not in player's hand"}
    return {'error': False,
            'message': "Cards have been added to discard pile"}


def draw(posn, card):
    gamestate = drawing_phase
    hand_info = in_hand(card, drawing_phase['deck'])
    if hand_info['found']:
        drawing_phase['player'][posn]['hand'].append(card)
        del drawing_phase['deck'][hand_info['location']]
        return {'error': False,
                'message': "Card removed from deck and added to player's hand"}
    else:
        return {'error': True,
                'message': "Card not in deck"}


def play(posn, cards):
    gamestate = None
