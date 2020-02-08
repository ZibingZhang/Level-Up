from constants import cursor, cnx


def add_message(player_name, message):
    cursor.execute(
        "INSERT INTO levelup.messages ("
            "RECIPIENT, SENDER, MESSAGE"
        ") VALUES ("
            "'ALL', %s, %s"
        ")", (player_name, message)
    )
    cnx.commit()
