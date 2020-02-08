from flask import Flask, request
from flask_cors import CORS
from mysql import connector
import yaml
import os

from service import chatService

app = Flask(__name__)
CORS(app)

config_path = os.path.join(os.getcwd(), 'config.yml')
with open(config_path) as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

cnx = connector.connect(user=config['database']['user'],
                        password=config['database']['password'],
                        host=config['database']['host'],
                        database=config['database']['database'])
cursor = cnx.cursor()

# if tables don't exist then create them
# MESSAGES table
cursor.execute(
    "CREATE TABLE IF NOT EXISTS MESSAGES ("
        "ID INT AUTO_INCREMENT PRIMARY KEY, "
        "RECIPIENT VARCHAR(3) NOT NULL, "
        "SENDER VARCHAR(20) NOT NULL, "
        "MESSAGE VARCHAR(200) NOT NULL"
    ")"
)


@app.route("/chat", methods=["POST"])
def chat():
    player_name = request.form['playerName']
    message = request.form['message']

    if message[0] == "/":
        # TODO: deal with commands
        return "Command"
    else:
        chatService.add_message(cnx, player_name, message)
        return "Message"


if __name__ == "__main__":
    app.run()
