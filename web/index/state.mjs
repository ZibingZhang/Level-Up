import {
    DEFAULT
} from './constants.mjs';

export {
    initState,
}

function initState() {
    document.state = {
        name: DEFAULT.NAME,
        messageId: -1
    }
}