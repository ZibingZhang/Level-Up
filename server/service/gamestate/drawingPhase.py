from ...constants import *

drawing_phase = {'status': "DRAWING PHASE", 'deck': DECK, 'discard': {}, 'players': {}, 'trump': {}}


def create(players):
    drawing_phase['players'] = players

