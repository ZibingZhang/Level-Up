export {
    URL,
    CHAT,
    COMMAND,
    DEFAULT,
    POSITION_TO_DIRECTION,
};

const URL = 'http://127.0.0.1:5000';

const CHAT = {
    TYPE: {
        MESSAGE: 'MESSAGE',
        COMMAND: 'COMMAND'
    }
}

const COMMAND = {
    JOIN: "JOIN",
    RESET: "RESET",
    HOST: "HOST",
    REJOIN: "REJOIN",
    ACTION: {
        DRAW: "DRAW",
        DISCARD: "DISCARD",
        PLAY: "PLAY",
        DECLARE: "DECLARE"
    },
    OTHER: {
        GAME_STATE: "GAME_STATE"
    }
}

const DEFAULT = {
    NAME: "[NAME]"
}

const POSITION_TO_DIRECTION = {
    'N': 'bottom',
    'E': 'left',
    'S': 'top',
    'W': 'right'
}