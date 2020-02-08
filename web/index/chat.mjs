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
        }).then(r => {
            if (r.data.type === 'message') {
                addChatroomMessage(true, document.state.name, message);
            } else if (r.data.type === 'command') {
                if (r.data.error === true) {
                    addChatroomCommand(r.data.message);
                } else if (r.data.error === false) {
                    console.log("Asdf");
                }
            }
        });
        chatroom.value = '';
    };
    });
};

function addChatroomCommand(message) {
    const chatroomBlock = document.createElement('div');
    chatroomBlock.className = 'chatroom-block';

    const chatroomCommand = document.createElement('span');
    chatroomCommand.className = 'chatroom-command';
    chatroomCommand.innerHTML = message;
    chatroomBlock.appendChild(chatroomCommand);

    const chatroom = document.getElementsByClassName('chatroom-display')[0];
    chatroom.appendChild(chatroomBlock);

    scrollToBottom();
}

function addChatroomMessage(currentPlayer, playerName, message) {
    const chatroomBlock = document.createElement('div');
    chatroomBlock.className = 'chatroom-block';

    const chatroomUser = document.createElement('span');
    chatroomUser.className = `chatroom-user ${currentPlayer ? 'current-user' : ''}`;
    chatroomUser.innerHTML = `${playerName}:`;
    chatroomBlock.appendChild(chatroomUser);

    const chatroomMessage = document.createElement('span');
    chatroomMessage.className = 'chatroom-message';
    chatroomMessage.innerHTML = message;
    chatroomBlock.appendChild(chatroomMessage);

    const chatroom = document.getElementsByClassName('chatroom-display')[0];
    chatroom.appendChild(chatroomBlock);

    scrollToBottom();
}

function scrollToBottom() {
    const chatroom = document.getElementsByClassName('chatroom-display')[0];
    chatroom.scrollTop = chatroom.scrollHeight;
}