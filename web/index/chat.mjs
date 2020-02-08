import { 
    URL,
    CHAT,
    COMMAND,
    DEFAULT
} from './constants.mjs';

export {
    listenToEnter,
    addChatroomCommand,
    addChatroomMessage,
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
            if (r.data.type === CHAT.TYPE.MESSAGE) {
                addChatroomMessage(true, document.state.name, message);
            } else if (r.data.type === CHAT.TYPE.COMMAND) {
                commandResponse(r.data);
            }
        });
        chatroom.value = '';
    };
    });
};

function commandResponse(data) {
    if (data.message) {
        addChatroomCommand(data.message);
    }
    const command = data.command;

    if (command === COMMAND.JOIN) {
        document.state.name = data.playerName;
    } else if (command === COMMAND.RESET) {
        document.state.name = DEFAULT.NAME;
    } else if (command === COMMAND.HOST) {
        document.state.name = data.playerName;
    }
}

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