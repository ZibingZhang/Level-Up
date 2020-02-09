import json
from constants import cursor, GAME_STATE


def get_gamestate():
    cursor.execute(
        "SELECT * FROM levelup.gamestate"
    )
    return json.loads(cursor.fetchall()[0][0])


def set_gamestate(gamestate):
    _clear()
    cursor.execute(
        "INSERT INTO levelup.gamestate (GAMESTATE) VALUES (%s)",
        (json.dumps(gamestate), )
    )


def reset():
    set_gamestate({
        'status': GAME_STATE['not started']
    })


def _clear():
    cursor.execute(
        "DELETE FROM levelup.gamestate"
    )
