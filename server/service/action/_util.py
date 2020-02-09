from constants import \
    SUIT_TO_STRING, \
    VAL_TO_STRING


def _in_cards(find, hand):
    for idx, card in enumerate(hand):
        if find['suit'] == card['suit'] and find['card']['val'] == card['card']['val']:
            return idx
    return -1


def _round_over(gamestate):
    for player in gamestate['players'].keys():
        if len(gamestate['players'][player]['cards']) != 0:
            return False
    return True


def _card_to_string(card):
    return SUIT_TO_STRING[card['suit']] + VAL_TO_STRING[card['value']['rank']]


def _check_suits(gamestate, posn, cards):
    suit = cards[0]['suit']
    if gamestate['players'][posn]['leading']:
        gamestate['trick']['suit'] = suit
    for card in cards:
        if card['suit'] != suit:
            return {'error': True,
                    'message': "Different suits within play"}
        if card['suit'] != gamestate['trick']['suit']:
            return {'error': True,
                    'message': "Different suit from leading suit"}
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
        if cards[0]['val'] == cards[1]['val']:
            return {'error': False,
                    'message': "Pair played"}
        else:
            return {'error': True,
                    'message': "Invalid play with two cards"}
    else:
        return {'error': False,
                'message': "Single played"}
