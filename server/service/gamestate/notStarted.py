not_started = {"players": {}}


def add_player(name, posn):
    not_started["players"].append({"player": name, "position": posn})


def check_start():
    if len(not_started["players"]) == 4:
        return True
    else:
        return False
