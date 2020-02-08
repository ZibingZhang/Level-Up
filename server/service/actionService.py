def discard(posn, cards):
    gamestate = None  #Need gamestate
    for card_key in cards.keys():
        if card_key not in gamestate.player(posn).hand.keys():
            return False
        if gamestate.player(posn).hand.get(card_key).get("quantity") == 2:
            gamestate.player(posn).hand.get(card_key).get("quantity") == 1
        else:
            del gamestate.player(posn).hand[card_key]
    gamestate.discard_pile = cards
    return True


def draw(posn, card):
    gamestate = None
    if card.key in gamestate.player(posn).hand.keys():
        gamestate.player(posn).hand.get(card.key).get("quantity") == 2
    else:
        gamestate.player(posn).hand[card.key] = {"card": card, "quantity": 1}
    if gamestate.deck.get(card.key).get("quantity") == 2:
        gamestate.deck.get(card.key).get("quantity") == 1
    else:
        del gamestate.deck[card.key]


def play(posn, cards):
    gamestate = None

