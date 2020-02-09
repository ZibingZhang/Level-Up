export {
    URL,
    CHAT,
    COMMAND,
    DEFAULT,
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
    ACTIONS: {
        DRAW: "DRAW",
        DISCARD: "DISCARD",
        PLAY: "PLAY",
        DECLARE: "DECLARE"
    }
}

const DEFAULT = {
    NAME: "[NAME]"
}