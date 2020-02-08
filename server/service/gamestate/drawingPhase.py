from ...constants import *

drawing_phase = {"status": "DRAWING PHASE", "deck": DECK, "discard": {}, "players": {}, "trump": ()}


def create_discard():
    if len(drawing_phase['deck']) == 8:
        drawing_phase['discard'] = drawing_phase['deck']
        drawing_phase['deck'].clear()
        return True
    else:
        return False


def create(players):
    drawing_phase['players'] = players

