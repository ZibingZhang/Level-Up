import os
import yaml
from mysql import connector

CARD = {
    'two': {'val': 2, 'points': 0, 'name': "TWO"},
    'three': {'val': 3, 'points': 0, 'name': "THREE"},
    'four': {'val': 4, 'points': 0, 'name': "FOUR"},
    'five': {'val': 5, 'points': 5, 'name': "FIVE"},
    'six': {'val': 6, 'points': 0, 'name': "SIX"},
    'seven': {'val': 7, 'points': 0, 'name': "SEVEN"},
    'eight': {'val': 8, 'points': 0, 'name': "EIGHT"},
    'nine': {'val': 9, 'points': 0, 'name': "NINE"},
    'ten': {'val': 10, 'points': 10, 'name': "TEN"},
    'jack': {'val': 11, 'points': 0, 'name': "JACK"},
    'queen': {'val': 12, 'points': 0, 'name': "QUEEN"},
    'king': {'val': 13, 'points': 10, 'name': "KING"},
    'ace': {'val': 14, 'points': 0, 'name': "ACE"},
    'small joker': {'val': 15, 'points': 0, 'name': "SMALL_JOKER"},
    'big joker': {'val': 16, 'points': 0, 'name': "BIG_JOKER"}
}

SUIT = {
    'heart': "HEART",
    'spade': "SPADE",
    'club': "CLUB",
    'diamond': "DIAMOND",
    'none': "NONE"
}

COMMAND = {
    'join': "JOIN",
    'reset': "RESET",
    'rejoin': "REJOIN",
    'host': "HOST",
    'start': "START",
    'action': {
        'draw': "DRAW",
        'discard': "DISCARD",
        'play': "PLAY",
        'declare': "DECLARE"
    }
}

GAME_STATE = {
    'not_started': "NOT_STARTED",
    'drawing': "DRAWING",
    'discarding': "DISCARDING",
    'in play': "IN_PLAY",
    'between rounds': "BETWEEN_ROUNDS",
    'game over': "GAME_OVER"
}

POSITION = {
    'north': "NORTH",
    'east': "EAST",
    'south': "SOUTH",
    'west': "WEST"
}

POSITION_TO_WORD = {
    'N': "north",
    'N': "north",
    'N': "north",
    'N': "north"
}

DECK = {
    1: {'suit': SUIT['heart'], 'card': CARD['two']},
    2: {'suit': SUIT['heart'], 'card': CARD['three']},
    3: {'suit': SUIT['heart'], 'card': CARD['four']},
    4: {'suit': SUIT['heart'], 'card': CARD['five']},
    5: {'suit': SUIT['heart'], 'card': CARD['six']},
    6: {'suit': SUIT['heart'], 'card': CARD['seven']},
    7: {'suit': SUIT['heart'], 'card': CARD['eight']},
    8: {'suit': SUIT['heart'], 'card': CARD['nine']},
    9: {'suit': SUIT['heart'], 'card': CARD['ten']},
    10: {'suit': SUIT['heart'], 'card': CARD['jack']},
    11: {'suit': SUIT['heart'], 'card': CARD['queen']},
    12: {'suit': SUIT['heart'], 'card': CARD['king']},
    13: {'suit': SUIT['heart'], 'card': CARD['ace']},
    14: {'suit': SUIT['heart'], 'card': CARD['two']},
    15: {'suit': SUIT['heart'], 'card': CARD['three']},
    16: {'suit': SUIT['heart'], 'card': CARD['four']},
    17: {'suit': SUIT['heart'], 'card': CARD['five']},
    18: {'suit': SUIT['heart'], 'card': CARD['six']},
    19: {'suit': SUIT['heart'], 'card': CARD['seven']},
    20: {'suit': SUIT['heart'], 'card': CARD['eight']},
    21: {'suit': SUIT['heart'], 'card': CARD['nine']},
    22: {'suit': SUIT['heart'], 'card': CARD['ten']},
    23: {'suit': SUIT['heart'], 'card': CARD['jack']},
    24: {'suit': SUIT['heart'], 'card': CARD['queen']},
    25: {'suit': SUIT['heart'], 'card': CARD['king']},
    26: {'suit': SUIT['heart'], 'card': CARD['ace']},
    27: {'suit': SUIT['spade'], 'card': CARD['two']},
    28: {'suit': SUIT['spade'], 'card': CARD['three']},
    29: {'suit': SUIT['spade'], 'card': CARD['four']},
    30: {'suit': SUIT['spade'], 'card': CARD['five']},
    31: {'suit': SUIT['spade'], 'card': CARD['six']},
    32: {'suit': SUIT['spade'], 'card': CARD['seven']},
    33: {'suit': SUIT['spade'], 'card': CARD['eight']},
    34: {'suit': SUIT['spade'], 'card': CARD['nine']},
    35: {'suit': SUIT['spade'], 'card': CARD['ten']},
    36: {'suit': SUIT['spade'], 'card': CARD['jack']},
    37: {'suit': SUIT['spade'], 'card': CARD['queen']},
    38: {'suit': SUIT['spade'], 'card': CARD['king']},
    39: {'suit': SUIT['spade'], 'card': CARD['ace']},
    40: {'suit': SUIT['spade'], 'card': CARD['two']},
    41: {'suit': SUIT['spade'], 'card': CARD['three']},
    42: {'suit': SUIT['spade'], 'card': CARD['four']},
    43: {'suit': SUIT['spade'], 'card': CARD['five']},
    44: {'suit': SUIT['spade'], 'card': CARD['six']},
    45: {'suit': SUIT['spade'], 'card': CARD['seven']},
    46: {'suit': SUIT['spade'], 'card': CARD['eight']},
    47: {'suit': SUIT['spade'], 'card': CARD['nine']},
    48: {'suit': SUIT['spade'], 'card': CARD['ten']},
    49: {'suit': SUIT['spade'], 'card': CARD['jack']},
    50: {'suit': SUIT['spade'], 'card': CARD['queen']},
    51: {'suit': SUIT['spade'], 'card': CARD['king']},
    52: {'suit': SUIT['spade'], 'card': CARD['ace']},
    53: {'suit': SUIT['club'], 'card': CARD['two']},
    54: {'suit': SUIT['club'], 'card': CARD['three']},
    55: {'suit': SUIT['club'], 'card': CARD['four']},
    56: {'suit': SUIT['club'], 'card': CARD['five']},
    57: {'suit': SUIT['club'], 'card': CARD['six']},
    58: {'suit': SUIT['club'], 'card': CARD['seven']},
    59: {'suit': SUIT['club'], 'card': CARD['eight']},
    60: {'suit': SUIT['club'], 'card': CARD['nine']},
    61: {'suit': SUIT['club'], 'card': CARD['ten']},
    62: {'suit': SUIT['club'], 'card': CARD['jack']},
    63: {'suit': SUIT['club'], 'card': CARD['queen']},
    64: {'suit': SUIT['club'], 'card': CARD['king']},
    65: {'suit': SUIT['club'], 'card': CARD['ace']},
    66: {'suit': SUIT['club'], 'card': CARD['two']},
    67: {'suit': SUIT['club'], 'card': CARD['three']},
    68: {'suit': SUIT['club'], 'card': CARD['four']},
    69: {'suit': SUIT['club'], 'card': CARD['five']},
    70: {'suit': SUIT['club'], 'card': CARD['six']},
    71: {'suit': SUIT['club'], 'card': CARD['seven']},
    72: {'suit': SUIT['club'], 'card': CARD['eight']},
    73: {'suit': SUIT['club'], 'card': CARD['nine']},
    74: {'suit': SUIT['club'], 'card': CARD['ten']},
    75: {'suit': SUIT['club'], 'card': CARD['jack']},
    76: {'suit': SUIT['club'], 'card': CARD['queen']},
    77: {'suit': SUIT['club'], 'card': CARD['king']},
    78: {'suit': SUIT['club'], 'card': CARD['ace']},
    79: {'suit': SUIT['diamond'], 'card': CARD['two']},
    80: {'suit': SUIT['diamond'], 'card': CARD['three']},
    81: {'suit': SUIT['diamond'], 'card': CARD['four']},
    82: {'suit': SUIT['diamond'], 'card': CARD['five']},
    83: {'suit': SUIT['diamond'], 'card': CARD['six']},
    84: {'suit': SUIT['diamond'], 'card': CARD['seven']},
    85: {'suit': SUIT['diamond'], 'card': CARD['eight']},
    86: {'suit': SUIT['diamond'], 'card': CARD['nine']},
    87: {'suit': SUIT['diamond'], 'card': CARD['ten']},
    88: {'suit': SUIT['diamond'], 'card': CARD['jack']},
    89: {'suit': SUIT['diamond'], 'card': CARD['queen']},
    90: {'suit': SUIT['diamond'], 'card': CARD['king']},
    91: {'suit': SUIT['diamond'], 'card': CARD['ace']},
    92: {'suit': SUIT['diamond'], 'card': CARD['two']},
    93: {'suit': SUIT['diamond'], 'card': CARD['three']},
    94: {'suit': SUIT['diamond'], 'card': CARD['four']},
    95: {'suit': SUIT['diamond'], 'card': CARD['five']},
    96: {'suit': SUIT['diamond'], 'card': CARD['six']},
    97: {'suit': SUIT['diamond'], 'card': CARD['seven']},
    98: {'suit': SUIT['diamond'], 'card': CARD['eight']},
    99: {'suit': SUIT['diamond'], 'card': CARD['nine']},
    100: {'suit': SUIT['diamond'], 'card': CARD['ten']},
    101: {'suit': SUIT['diamond'], 'card': CARD['jack']},
    102: {'suit': SUIT['diamond'], 'card': CARD['queen']},
    103: {'suit': SUIT['diamond'], 'card': CARD['king']},
    104: {'suit': SUIT['diamond'], 'card': CARD['ace']},
    105: {'suit': SUIT['none'], 'card': CARD['small joker']},
    106: {'suit': SUIT['none'], 'card': CARD['big joker']},
    107: {'suit': SUIT['none'], 'card': CARD['small joker']},
    108: {'suit': SUIT['none'], 'card': CARD['big joker']}
}

_config_path = os.path.join(os.getcwd(), 'config.yml')
with open(_config_path) as file:
    _config = yaml.load(file, Loader=yaml.SafeLoader)

cnx = connector.connect(user=_config['database']['user'],
                        password=_config['database']['password'],
                        host=_config['database']['host'],
                        database=_config['database']['database'])
cnx.autocommit = True
cursor = cnx.cursor()
