from constants import \
    SUIT_TO_STRING, \
    VAL_TO_STRING, \
    LETTER_TO_POSITION_KEY, \
    PLAYER_TO_TEAM


def _in_cards(find, hand):
    for idx, card in enumerate(hand):
        if find['suit'] == card['suit'] and find['card']['val'] == card['card']['val']:
            return idx
    return -1


def _round_over(gamestate):
    for player in gamestate['players'].keys():
        if len(gamestate['players'][player]['cards']) != 0:
            return False
    else:
        return True


def _trick_over(gamestate):
    if len(gamestate['trick']['current_play']) == 4:
        return True
    else:
        return False


def _rank_hand(gamestate, position):
    player = gamestate['trick']['current_play'][LETTER_TO_POSITION_KEY[position.upper()]]
    if len(player['cards']) == 2:
        if player['cards'][0]['value']['rank'] == player['cards'][1]['value']['rank'] \
                and player['cards'][0]['suit'] == player['cards'][1]['suit']:
            player['rank'] = 2
        else:
            player['rank'] = 1
    else:
        player['rank'] = 1


def _trick_winner(gamestate):
    pass
    return "N"


def _points_in_current_play(gamestate):
    total = 0
    for player in gamestate['players'].keys():
        for card in gamestate['trick']['current_play'][player]['cards']:
            total += card['value']['points']
    return total


def _assign_points(gamestate):
    [_rank_hand(gamestate, position) for position in gamestate['players'].keys()]
    winner = _trick_winner(gamestate)
    gamestate['trick']['starter'] = winner
    if gamestate['defender'] == PLAYER_TO_TEAM[winner]:
        gamestate['points'] += _points_in_current_play(gamestate)
    gamestate['trick']['current_play'] = []


def _card_to_string(card):
    return SUIT_TO_STRING[card['suit']] + VAL_TO_STRING[card['value']['rank']]


def _follow_suit(gamestate, position):
    num_suit = 0
    for card in gamestate['players'][LETTER_TO_POSITION_KEY[position.upper()]]['cards']:
        if card['suit'] == gamestate['trick']['suit']:
            num_suit += 1
    return num_suit


def _check_suits(gamestate, position, cards):
    suit = cards[0]['suit']
    if gamestate['players'][position]['leading']:
        gamestate['trick']['suit'] = suit
    num_follow = _follow_suit(gamestate, position)
    num_dont_follow = len(cards) - num_follow
    for card in cards:
        if card['suit'] != suit:
            if num_dont_follow == 0:
                return {'error': True,
                        'message': "Different suits within play/Too many different suited cards"}
            else:
                num_dont_follow -= 1
        if card['suit'] != gamestate['trick']['suit']:
            if num_follow > 0:
                return {'error': True,
                        'message': "Different suit from leading suit/Too many different non-leading suited cards"}
            else:
                num_follow -= 1
    return {'error': False,
            'message': "All suits match"}


def _check_style(gamestate, cards):
    # if len(cards) == 6:
    #     if cards[0]['val'] == cards[1]['val'] and cards[2]['val'] == cards[3]['val'] \
    #             and cards[4]['val'] == cards[5]['val'] and cards[1]['val'] + 1 == cards[2]['val'] \
    #             and cards[3]['val'] + 1 == cards[4]['val']:
    #         return {'error': False,
    #                 'message': "Three consecutive pairs played"}
    #     else:
    #         return {'error': True,
    #                 'message': "Invalid play with six cards"}
    # elif len(cards) == 4:
    #     if cards[0]['val'] == cards[1]['val'] and cards[2]['val'] == cards[3]['val'] \
    #             and cards[1]['val'] + 1 == cards[2]['val']:
    #         return {'error': False,
    #                 'message': "Two consecutive pairs played"}
    #     else:
    #         return {'error': True,
    #                 'message': "Invalid play with four cards"}
    if len(cards) == 2:
        if cards[0]['value']['rank'] == cards[1]['value']['rank'] and cards[0]['suit'] == cards[1]['suit']:
            return {'error': False,
                    'message': "Pair played"}
        else:
            return {'error': True,
                    'message': "Invalid play with two cards"}
    else:
        return {'error': False,
                'message': "Single played"}


def _check_valid(gamestate, position, cards):
    sorted_cards = sorted(cards, key=lambda k: k['value']['rank'])
    valid_suits = _check_suits(gamestate, position, sorted_cards)
    if valid_suits['error']:
        return valid_suits
    valid_style = _check_style(gamestate, sorted_cards)
    return valid_style
