from ...constants import *

in_play = {'status': "IN PLAY", 'deck': {}, 'discard': {}, 'players': {},
           'trump': {},
           'trick': {'suit': "", 'style': []}}


def create(discard, players, trump):
    in_play['discard'] = discard
    in_play['players'] = players
    for player in in_play['players'].keys():
        in_play['players'][player]['points'] = 0
        in_play['players'][player]['current play'] = []
    in_play['trump'] = trump
