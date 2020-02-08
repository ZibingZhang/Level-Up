def add_message(cnx, player_name, message):
    cursor = cnx.cursor()
    cursor.execute(
        "INSERT INTO levelup.messages ("
            "RECIPIENT, SENDER, MESSAGE"
        ") VALUES ("
            f"'ALL', '{player_name}', '{message}'"
        ")"
    )
    cnx.commit()
