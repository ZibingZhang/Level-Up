from constants import cursor, cnx


def get_names():
    cursor.execute(
        "SELECT PLAYER_NAME FROM levelup.players"
    )
    return [player[0] for player in cursor.fetchall()]


def get_positions():
    cursor.execute(
        "SELECT POSITION FROM levelup.players"
    )
    return [player[0] for player in cursor.fetchall()]


def add_player(position, player_name):
    cursor.execute(
        "INSERT INTO levelup.players (POSITION, PLAYER_NAME) VALUES (%s, %s)",
        (position, player_name)
    )
    cnx.commit()


def reset():
    cursor.execute(
        "DELETE FROM levelup.players"
    )
    cnx.commit()


def has_host():
    cursor.execute(
        "SELECT COUNT(*) FROM levelup.players WHERE POSITION='N'"
    )
    return cursor.fetchall()[0][0] == 1
