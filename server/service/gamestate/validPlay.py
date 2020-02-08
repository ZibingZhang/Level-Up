def is_valid_play(gamestate, cards):
    return _follows_style(gamestate, cards) \
        and _follows_suit(gamestate, cards)


def _follows_suit(gamestate, cards):
    pass


def _follows_style(gamestate, cards):
    pass


def _passes():
    return True
