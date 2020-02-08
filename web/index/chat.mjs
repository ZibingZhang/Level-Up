import { URL } from './constants.mjs';

export {
    listenToEnter,
};

function listenToEnter() {
    const chatroom = document.getElementsByClassName('chatroom-user-input')[0];
    chatroom.addEventListener('keyup', function(event) {    
    if (event.key === 'Enter') {
        const message = chatroom.value;
        axios.post(`${URL}/chat`, {
            playerName: 'Anisa',
            message
        }).then(r => addChatroomCommand(r.data));
        chatroom.value = '';
    };
    });
};

function addChatroomCommand(message) {
    let chatroomBlock = document.createElement('div');
    chatroomBlock.className = 'chatroom-block';

    let chatroomCommand = document.createElement('span');
    chatroomCommand.className = 'chatroom-command';
    chatroomCommand.innerHTML = message;

    chatroomBlock.appendChild(chatroomCommand);

    let chatroom = document.getElementsByClassName('chatroom-display')[0];
    chatroom.appendChild(chatroomBlock);
}