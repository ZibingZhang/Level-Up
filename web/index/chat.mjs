import { URL } from './constants.mjs';

export {
    listenToEnter,
};

function listenToEnter() {
    const chatroom = document.getElementsByClassName("chatroom-user-input")[0];
    chatroom.addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        const message = chatroom.value;
        axios.post(`${URL}/chat`, {
            playerName: 'Anisa',
            message
        });
        chatroom.value = '';
    };
});
};