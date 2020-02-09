import os
import yaml
from mysql import connector

VALUE = {
    'two': {'rank': 2, 'points': 0, 'name': "TWO"},
    'three': {'rank': 3, 'points': 0, 'name': "THREE"},
    'four': {'rank': 4, 'points': 0, 'name': "FOUR"},
    'five': {'rank': 5, 'points': 5, 'name': "FIVE"},
    'six': {'rank': 6, 'points': 0, 'name': "SIX"},
    'seven': {'rank': 7, 'points': 0, 'name': "SEVEN"},
    'eight': {'rank': 8, 'points': 0, 'name': "EIGHT"},
    'nine': {'rank': 9, 'points': 0, 'name': "NINE"},
    'ten': {'rank': 10, 'points': 10, 'name': "TEN"},
    'jack': {'rank': 11, 'points': 0, 'name': "JACK"},
    'queen': {'rank': 12, 'points': 0, 'name': "QUEEN"},
    'king': {'rank': 13, 'points': 10, 'name': "KING"},
    'ace': {'rank': 14, 'points': 0, 'name': "ACE"},
    'small joker': {'rank': 15, 'points': 0, 'name': "SMALL_JOKER"},
    'big joker': {'rank': 16, 'points': 0, 'name': "BIG_JOKER"}
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
    'not started': "NOT_STARTED",
    'drawing': "DRAWING",
    'discarding': "DISCARDING",
    'in play': "IN_PLAY",
    'between rounds': "BETWEEN_ROUNDS",
    'game over': "GAME_OVER"
}

LETTER_TO_POSITION = {
    'N': "NORTH",
    'E': "EAST",
    'S': "SOUTH",
    'W': "WEST"
}

LETTER_TO_POSITION_KEY = {
    'N': "north",
    'E': "east",
    'S': "south",
    'W': "west"
}

DRAW_ORDER = {
    'NORTH': "WEST",
    'WEST': "SOUTH",
    'SOUTH': "EAST",
    'EAST': "NORTH"
}

PLAYER_TO_TEAM = {
    'N': "NS",
    'W': "WE",
    'S': "NS",
    'E': "WE"
}

DECK = {
    1: {'suit': SUIT['heart'], 'value': VALUE['two']},
    2: {'suit': SUIT['heart'], 'value': VALUE['three']},
    3: {'suit': SUIT['heart'], 'value': VALUE['four']},
    4: {'suit': SUIT['heart'], 'value': VALUE['five']},
    5: {'suit': SUIT['heart'], 'value': VALUE['six']},
    6: {'suit': SUIT['heart'], 'value': VALUE['seven']},
    7: {'suit': SUIT['heart'], 'value': VALUE['eight']},
    8: {'suit': SUIT['heart'], 'value': VALUE['nine']},
    9: {'suit': SUIT['heart'], 'value': VALUE['ten']},
    10: {'suit': SUIT['heart'], 'value': VALUE['jack']},
    11: {'suit': SUIT['heart'], 'value': VALUE['queen']},
    12: {'suit': SUIT['heart'], 'value': VALUE['king']},
    13: {'suit': SUIT['heart'], 'value': VALUE['ace']},
    14: {'suit': SUIT['heart'], 'value': VALUE['two']},
    15: {'suit': SUIT['heart'], 'value': VALUE['three']},
    16: {'suit': SUIT['heart'], 'value': VALUE['four']},
    17: {'suit': SUIT['heart'], 'value': VALUE['five']},
    18: {'suit': SUIT['heart'], 'value': VALUE['six']},
    19: {'suit': SUIT['heart'], 'value': VALUE['seven']},
    20: {'suit': SUIT['heart'], 'value': VALUE['eight']},
    21: {'suit': SUIT['heart'], 'value': VALUE['nine']},
    22: {'suit': SUIT['heart'], 'value': VALUE['ten']},
    23: {'suit': SUIT['heart'], 'value': VALUE['jack']},
    24: {'suit': SUIT['heart'], 'value': VALUE['queen']},
    25: {'suit': SUIT['heart'], 'value': VALUE['king']},
    26: {'suit': SUIT['heart'], 'value': VALUE['ace']},
    27: {'suit': SUIT['spade'], 'value': VALUE['two']},
    28: {'suit': SUIT['spade'], 'value': VALUE['three']},
    29: {'suit': SUIT['spade'], 'value': VALUE['four']},
    30: {'suit': SUIT['spade'], 'value': VALUE['five']},
    31: {'suit': SUIT['spade'], 'value': VALUE['six']},
    32: {'suit': SUIT['spade'], 'value': VALUE['seven']},
    33: {'suit': SUIT['spade'], 'value': VALUE['eight']},
    34: {'suit': SUIT['spade'], 'value': VALUE['nine']},
    35: {'suit': SUIT['spade'], 'value': VALUE['ten']},
    36: {'suit': SUIT['spade'], 'value': VALUE['jack']},
    37: {'suit': SUIT['spade'], 'value': VALUE['queen']},
    38: {'suit': SUIT['spade'], 'value': VALUE['king']},
    39: {'suit': SUIT['spade'], 'value': VALUE['ace']},
    40: {'suit': SUIT['spade'], 'value': VALUE['two']},
    41: {'suit': SUIT['spade'], 'value': VALUE['three']},
    42: {'suit': SUIT['spade'], 'value': VALUE['four']},
    43: {'suit': SUIT['spade'], 'value': VALUE['five']},
    44: {'suit': SUIT['spade'], 'value': VALUE['six']},
    45: {'suit': SUIT['spade'], 'value': VALUE['seven']},
    46: {'suit': SUIT['spade'], 'value': VALUE['eight']},
    47: {'suit': SUIT['spade'], 'value': VALUE['nine']},
    48: {'suit': SUIT['spade'], 'value': VALUE['ten']},
    49: {'suit': SUIT['spade'], 'value': VALUE['jack']},
    50: {'suit': SUIT['spade'], 'value': VALUE['queen']},
    51: {'suit': SUIT['spade'], 'value': VALUE['king']},
    52: {'suit': SUIT['spade'], 'value': VALUE['ace']},
    53: {'suit': SUIT['club'], 'value': VALUE['two']},
    54: {'suit': SUIT['club'], 'value': VALUE['three']},
    55: {'suit': SUIT['club'], 'value': VALUE['four']},
    56: {'suit': SUIT['club'], 'value': VALUE['five']},
    57: {'suit': SUIT['club'], 'value': VALUE['six']},
    58: {'suit': SUIT['club'], 'value': VALUE['seven']},
    59: {'suit': SUIT['club'], 'value': VALUE['eight']},
    60: {'suit': SUIT['club'], 'value': VALUE['nine']},
    61: {'suit': SUIT['club'], 'value': VALUE['ten']},
    62: {'suit': SUIT['club'], 'value': VALUE['jack']},
    63: {'suit': SUIT['club'], 'value': VALUE['queen']},
    64: {'suit': SUIT['club'], 'value': VALUE['king']},
    65: {'suit': SUIT['club'], 'value': VALUE['ace']},
    66: {'suit': SUIT['club'], 'value': VALUE['two']},
    67: {'suit': SUIT['club'], 'value': VALUE['three']},
    68: {'suit': SUIT['club'], 'value': VALUE['four']},
    69: {'suit': SUIT['club'], 'value': VALUE['five']},
    70: {'suit': SUIT['club'], 'value': VALUE['six']},
    71: {'suit': SUIT['club'], 'value': VALUE['seven']},
    72: {'suit': SUIT['club'], 'value': VALUE['eight']},
    73: {'suit': SUIT['club'], 'value': VALUE['nine']},
    74: {'suit': SUIT['club'], 'value': VALUE['ten']},
    75: {'suit': SUIT['club'], 'value': VALUE['jack']},
    76: {'suit': SUIT['club'], 'value': VALUE['queen']},
    77: {'suit': SUIT['club'], 'value': VALUE['king']},
    78: {'suit': SUIT['club'], 'value': VALUE['ace']},
    79: {'suit': SUIT['diamond'], 'value': VALUE['two']},
    80: {'suit': SUIT['diamond'], 'value': VALUE['three']},
    81: {'suit': SUIT['diamond'], 'value': VALUE['four']},
    82: {'suit': SUIT['diamond'], 'value': VALUE['five']},
    83: {'suit': SUIT['diamond'], 'value': VALUE['six']},
    84: {'suit': SUIT['diamond'], 'value': VALUE['seven']},
    85: {'suit': SUIT['diamond'], 'value': VALUE['eight']},
    86: {'suit': SUIT['diamond'], 'value': VALUE['nine']},
    87: {'suit': SUIT['diamond'], 'value': VALUE['ten']},
    88: {'suit': SUIT['diamond'], 'value': VALUE['jack']},
    89: {'suit': SUIT['diamond'], 'value': VALUE['queen']},
    90: {'suit': SUIT['diamond'], 'value': VALUE['king']},
    91: {'suit': SUIT['diamond'], 'value': VALUE['ace']},
    92: {'suit': SUIT['diamond'], 'value': VALUE['two']},
    93: {'suit': SUIT['diamond'], 'value': VALUE['three']},
    94: {'suit': SUIT['diamond'], 'value': VALUE['four']},
    95: {'suit': SUIT['diamond'], 'value': VALUE['five']},
    96: {'suit': SUIT['diamond'], 'value': VALUE['six']},
    97: {'suit': SUIT['diamond'], 'value': VALUE['seven']},
    98: {'suit': SUIT['diamond'], 'value': VALUE['eight']},
    99: {'suit': SUIT['diamond'], 'value': VALUE['nine']},
    100: {'suit': SUIT['diamond'], 'value': VALUE['ten']},
    101: {'suit': SUIT['diamond'], 'value': VALUE['jack']},
    102: {'suit': SUIT['diamond'], 'value': VALUE['queen']},
    103: {'suit': SUIT['diamond'], 'value': VALUE['king']},
    104: {'suit': SUIT['diamond'], 'value': VALUE['ace']},
    105: {'suit': SUIT['none'], 'value': VALUE['small joker']},
    106: {'suit': SUIT['none'], 'value': VALUE['big joker']},
    107: {'suit': SUIT['none'], 'value': VALUE['small joker']},
    108: {'suit': SUIT['none'], 'value': VALUE['big joker']}
}

VAL_TO_STRING = {
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "10",
    11: "J",
    12: "Q",
    13: "K",
    14: "A",
    15: "S",
    16: "B"
}

SUIT_TO_STRING = {
    'HEART': "H",
    'SPADE': "S",
    'DIAMOND': "D",
    'CLUB': "C",
    'NONE': "J"
}

INITIAL_GAME_STATE = {
    'drawing': {
        'status': GAME_STATE['drawing'],
        'draw next': LETTER_TO_POSITION['N'],
        'last eight': None,
        'defender': None,
        'deck': DECK.copy(),
        'trump': None,
        'team level': {
            'NS': 2,
            'WE': 2
        },
        'players': {
            'north': {
                'position': LETTER_TO_POSITION['N'],
                'cards': []
            },
            'east': {
                'position': LETTER_TO_POSITION['E'],
                'cards': []
            },
            'south': {
                'position': LETTER_TO_POSITION['S'],
                'cards': []
            },
            'west': {
                'position': LETTER_TO_POSITION['W'],
                'cards': []
            }
        }
    }
}

# DATABASE CONSTANTS

_config_path = os.path.join(os.getcwd(), 'config.yml')
with open(_config_path) as file:
    _config = yaml.load(file, Loader=yaml.SafeLoader)

cnx = connector.connect(user=_config['database']['user'],
                        password=_config['database']['password'],
                        host=_config['database']['host'],
                        database=_config['database']['database'])
cnx.autocommit = True
cursor = cnx.cursor()
