from service.action import discard as discard_action
from service.action import draw as draw_action
from service.action import play as play_action
from service.action import declare as declare_action


def discard(position, cards):
    return discard_action.discard(position, cards)


def draw(position):
    return draw_action.draw(position)


def declare(position, cards):
    return declare_action.declare(position, cards)


def play(position, cards):
    return play_action.play(position, cards)












