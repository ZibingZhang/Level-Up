import { 
    listenToEnter as chatListenToEnter,
    getNextMessages as chatGetNextMessages
} from './chat.mjs';
import { initState } from './state.mjs';
import { loadCards } from './loadCards.mjs';

initState();
loadCards();
chatListenToEnter();
chatGetNextMessages();