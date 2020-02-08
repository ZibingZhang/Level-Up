import os
import yaml
from mysql import connector

CARDS = {
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
    'small joker': {'val': 15, 'points': 0, 'name': "SMALL JOKER"},
    'big joker': {'val': 16, 'points': 0, 'name': "BIG JOKER"}
}

SUITS = {
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
    'host': "HOST"
}

DECK = {

}

_config_path = os.path.join(os.getcwd(), 'config.yml')
with open(_config_path) as file:
    _config = yaml.load(file, Loader=yaml.SafeLoader)

cnx = connector.connect(user=_config['database']['user'],
                        password=_config['database']['password'],
                        host=_config['database']['host'],
                        database=_config['database']['database'])
cursor = cnx.cursor()
