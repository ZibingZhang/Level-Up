from dao import gamestateDao
from ._util import _card_to_string
from constants import \
    LETTER_TO_POSITION, \
    LETTER_TO_POSITION_KEY, \
    GAME_STATE, \
    DRAW_ORDER, \
    SUIT, \
    PLAYER_TO_TEAM


def draw(position):
    gamestate = gamestateDao.get_gamestate()

    if LETTER_TO_POSITION[position.upper()] != gamestate['draw next']:
        return {'error': True,
                'message': "Not your turn to draw"}
    else:
        card = gamestate['deck'].pop(str(len(gamestate['deck'])))  # replace with random card choosing
        gamestate['players'][LETTER_TO_POSITION_KEY[position.upper()]]['cards'].append(card)
        if len(gamestate['deck']) == 8:
            if gamestate['trump'] is None:
                if gamestate['last eight'] is None:
                    gamestate['last eight'] = "N"  # hard coded
                    gamestate['players']['north']['cards'].extend(gamestate['deck'])  # hard coded
                gamestate['trump'] = {
                    'suit': SUIT['heart'],  # hard coded
                    'value': gamestate['team level'][PLAYER_TO_TEAM[gamestate['last eight']]]
                }

            gamestate['status'] = GAME_STATE['discarding']
            gamestateDao.set_gamestate(gamestate)
            return {'error': False,
                    'message': "Now waiting for discarding",
                    'position': position,
                    'card': _card_to_string(card),
                    'cards': [_card_to_string(card) for card in gamestate['deck'].values()]}
        else:
            gamestate['draw next'] = DRAW_ORDER[gamestate['draw next']]
            gamestateDao.set_gamestate(gamestate)
            return {'error': False,
                    'position': position,
                    'card': _card_to_string(card)}