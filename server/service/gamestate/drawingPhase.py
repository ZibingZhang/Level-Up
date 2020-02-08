drawing_phase = {"deck": {}, "discard": {}, "players": [], "trump": ()}

def create_deck():
    for i in range(0, 107):
        drawing_phase["deck"]

def create_discard():
    if len(drawing_phase["deck"]) == 8:
        drawing_phase["discard"] = drawing_phase["deck"]
        drawing_phase["deck"].clear()
        return True
    else:
        return False

def create(players):
    drawing_phase["players"] = players

