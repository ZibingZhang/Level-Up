import { addToHand } from './card.mjs';
import { 
    URL,
    CHAT,
    COMMAND,
    DEFAULT,
    POSITION_TO_DIRECTION
} from './constants.mjs';

export {
    listenToEnter,
    addChatroomCommand,
    addChatroomMessage,
    getNextMessages,
};

function listenToEnter() {
    const chatroom = document.getElementsByClassName('chatroom-user-input')[0];
    chatroom.addEventListener('keyup', async function(event) {    
        if (event.key === 'Enter') {
            const message = chatroom.value;
            if (message === '/drawall\n') {
                let i;
                for (i = 0; i < 25; i++) {
                    await axios.post(`${URL}/chat`, {playerName: document.state.name, message: '/draw N\n'}).then(r => addToHand(POSITION_TO_DIRECTION[r.data.position], r.data.card));
                    await axios.post(`${URL}/chat`, {playerName: document.state.name, message: '/draw W\n'}).then(r => addToHand(POSITION_TO_DIRECTION[r.data.position], r.data.card));
                    await axios.post(`${URL}/chat`, {playerName: document.state.name, message: '/draw S\n'}).then(r => addToHand(POSITION_TO_DIRECTION[r.data.position], r.data.card));
                    await axios.post(`${URL}/chat`, {playerName: document.state.name, message: '/draw E\n'}).then(r => {
                        addToHand(POSITION_TO_DIRECTION[r.data.position], r.data.card);
                        if (r.data.message) {
                            addChatroomCommand(r.data.message);
                            r.data.cards.forEach(card => {
                                addToHand('bottom', card);
                            });
                        }
                    });
                }
                chatroom.value = '';
                return;
            } else if (message === '/clear\n') {
                chatroom.value = '';
                var chatroomBlocks = document.getElementsByClassName('chatroom-block');
                while(chatroomBlocks.length > 0) {
                    chatroomBlocks[0].parentNode.removeChild(chatroomBlocks[0]);
                }
                return;
            }

            axios.post(`${URL}/chat`, {
                playerName: document.state.name,
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

    if (data.error === false) {
        if (command === COMMAND.JOIN) {
            document.state.name = data.playerName;
            document.state.messageId = data.messageId;
            document.state.position = data.position;
        } else if (command === COMMAND.RESET) {
            document.state.name = DEFAULT.NAME;
            document.state.messageId = -1;
        } else if (command === COMMAND.HOST) {
            document.state.name = data.playerName;
            document.state.messageId = data.messageId;
            document.state.position = data.position;
        } else if (command === COMMAND.REJOIN) {
            document.state.name = data.playerName;
            document.state.messageId = data.messageId;
            document.state.position = data.position;
        } else {
            // ACTIONS
            if (command === COMMAND.ACTION.DRAW) {
                console.log(data)
            } else if (command === COMMAND.ACTION.DISCARD) {

            } else if (command === COMMAND.ACTION.PLAY) {

            } else if (command === COMMAND.ACTION.DECLARE) {
                
            }
        }
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

function getNextMessages() {
    axios.get(`${URL}/messages/${document.state.messageId}`).then(r => {
        const data = r.data;
        document.state.messageId = data.messageId;
        data.messages.forEach(messageData => {
            const playerName = messageData[0];
            const message = messageData[1];
            
            if (playerName !== document.state.name) {
                addChatroomMessage(false, playerName, message);
            }
        });
    });

    setTimeout(getNextMessages, 1000);
}