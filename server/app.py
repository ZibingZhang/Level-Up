from flask import Flask
from flask_cors import CORS
from mysql import connector
import yaml
import os

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
    "SELECT COUNT(*) FROM (SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'messages') count"
)
if cursor.fetchone()[0] == 0:
    cursor.execute(
        "CREATE TABLE MESSAGES ("
        "ID INT PRIMARY KEY, "
        "SENDER VARCHAR(20) NOT NULL, "
        "MESSAGE VARCHAR(200) NOT NULL)"
    )


@app.route("/test", methods=["GET"])
def hello():
    return "Hello World!"


@app.route("/insert", methods=["POST"])
def insert():
    cursor.execute("INSERT INTO MESSAGES (ID, SENDER, MESSAGE) VALUES (1, 'Anisa', 'hello world')")
    cnx.commit()
    return "inserted"


if __name__ == "__main__":
    app.run()
