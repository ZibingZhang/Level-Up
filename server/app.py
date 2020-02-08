from flask import Flask, request
from flask_cors import CORS

from service import chatService
from constants import cursor

app = Flask(__name__)
CORS(app)

# messages table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS MESSAGES ("
        "ID INT AUTO_INCREMENT PRIMARY KEY, "
        "RECIPIENT VARCHAR(3) NOT NULL, "
        "SENDER VARCHAR(20) NOT NULL, "
        "MESSAGE VARCHAR(200) NOT NULL"
    ")"
)

# players table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS PLAYERS ("
        "POSITION VARCHAR(1) NOT NULL, "
        "PLAYER_NAME VARCHAR(20) NOT NULL"
    ")"
)


@app.route("/chat", methods=["POST"])
def chat():
    player_name = request.json['playerName']
    message = request.json['message']

    if message[0] == "/":
        args = message[1:][:-1].split(" ")
        command = args[0]
        params = args[1:]
        return chatService.command(command, params)
    else:
        chatService.add_message(player_name, message)
        return {'type': 'message'}


if __name__ == "__main__":
    app.run()
