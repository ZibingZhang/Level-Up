from constants import cursor


def add_message(player_name, message):
    cursor.execute(
        "INSERT INTO levelup.messages ("
            "SENDER, MESSAGE"
        ") VALUES ("
            "%s, %s"
        ")", (player_name, message)
    )


def reset():
    cursor.execute(
        "DELETE FROM levelup.messages"
    )
    cursor.execute(
        "ALTER TABLE levelup.messages AUTO_INCREMENT=1"
    )


def get_largest_id():
    cursor.execute(
        "SELECT MAX(ID) FROM levelup.messages"
    )
    id = cursor.fetchall()[0][0]
    return int(id) if id is not None else 0


def get_next_messages(message_id):
    cursor.execute(
        "SELECT SENDER, MESSAGE FROM levelup.messages WHERE id>%s ORDER BY ID ASC",
        (message_id, )
    )
    return cursor.fetchall()
