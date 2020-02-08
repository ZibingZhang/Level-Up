from flask import Flask, request
from flask_cors import CORS

from service import chatService
from constants import cursor, cnx

app = Flask(__name__)
CORS(app)

# messages table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS MESSAGES ("
        "ID INT AUTO_INCREMENT PRIMARY KEY, "
        "SENDER VARCHAR(20) NOT NULL, "
        "MESSAGE VARCHAR(200) NOT NULL"
    ")"
)
cnx.commit()

# players table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS PLAYERS ("
        "POSITION VARCHAR(1) NOT NULL, "
        "PLAYER_NAME VARCHAR(20) NOT NULL"
    ")"
)
cnx.commit()

# gamestate table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS GAMESTATE ("
        "GAMESTATE VARCHAR(10000) NOT NULL"
    ")"
)
cnx.commit()


@app.route("/action", methods=["POST"])
def action():
    pass


@app.route("/chat", methods=["POST"])
def chat():
    player_name = request.json['playerName']
    message = request.json['message']

    if message[0] == "/":
        args = message[1:][:-1].split(" ")
        command = args[0].upper()
        params = args[1:]
        return chatService.command(command, params,
                                   player_name=player_name)
    else:
        chatService.add_message(player_name, message)
        return {'type': 'MESSAGE'}


@app.route("/messages/<message_id>", methods=["GET"])
def messages(message_id):
    return chatService.get_next_messages(int(message_id))


if __name__ == "__main__":
    app.run()
