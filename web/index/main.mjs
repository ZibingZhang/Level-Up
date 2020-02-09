import { 
    listenToEnter as chatListenToEnter,
    getNextMessages as chatGetNextMessages
} from './chat.mjs';
import { initState } from './state.mjs';
import { loadCards } from './loadCards.mjs';

initState();
loadCards();
chatListenToEnter();
// chatGetNextMessages();

document.onkeydown = function(e){
    if(e.target.nodeName === 'TEXTAREA') return;
    $('.selected').removeClass('selected');
};