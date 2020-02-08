from dao import messageDao


def add_message(cnx, player_name, message):
    messageDao.add_message(cnx, player_name, message)
