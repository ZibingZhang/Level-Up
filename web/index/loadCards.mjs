export {
    loadCards,
};

const URLS = {
    'C2': '../assets/cards/clubs/2.png',
    'C3': '../assets/cards/clubs/3.png',
    'C4': '../assets/cards/clubs/4.png',
    'C5': '../assets/cards/clubs/5.png',
    'C6': '../assets/cards/clubs/6.png',
    'C7': '../assets/cards/clubs/7.png',
    'C8': '../assets/cards/clubs/8.png',
    'C9': '../assets/cards/clubs/9.png',
    'C10': '../assets/cards/clubs/10.png',
    'CJ': '../assets/cards/clubs/J.png',
    'CQ': '../assets/cards/clubs/Q.png',
    'CK': '../assets/cards/clubs/K.png',
    'CA': '../assets/cards/clubs/A.png',
    'D2': '../assets/cards/diamonds/2.png',
    'D3': '../assets/cards/diamonds/3.png',
    'D4': '../assets/cards/diamonds/4.png',
    'D5': '../assets/cards/diamonds/5.png',
    'D6': '../assets/cards/diamonds/6.png',
    'D7': '../assets/cards/diamonds/7.png',
    'D8': '../assets/cards/diamonds/8.png',
    'D9': '../assets/cards/diamonds/9.png',
    'D10': '../assets/cards/diamonds/10.png',
    'DJ': '../assets/cards/diamonds/J.png',
    'DQ': '../assets/cards/diamonds/Q.png',
    'DK': '../assets/cards/diamonds/K.png',
    'DA': '../assets/cards/diamonds/A.png',
    'H2': '../assets/cards/hearts/2.png',
    'H3': '../assets/cards/hearts/3.png',
    'H4': '../assets/cards/hearts/4.png',
    'H5': '../assets/cards/hearts/5.png',
    'H6': '../assets/cards/hearts/6.png',
    'H7': '../assets/cards/hearts/7.png',
    'H8': '../assets/cards/hearts/8.png',
    'H9': '../assets/cards/hearts/9.png',
    'H10': '../assets/cards/hearts/10.png',
    'HJ': '../assets/cards/hearts/J.png',
    'HQ': '../assets/cards/hearts/Q.png',
    'HK': '../assets/cards/hearts/K.png',
    'HA': '../assets/cards/hearts/A.png',
    'S2': '../assets/cards/spades/2.png',
    'S3': '../assets/cards/spades/3.png',
    'S4': '../assets/cards/spades/4.png',
    'S5': '../assets/cards/spades/5.png',
    'S6': '../assets/cards/spades/6.png',
    'S7': '../assets/cards/spades/7.png',
    'S8': '../assets/cards/spades/8.png',
    'S9': '../assets/cards/spades/9.png',
    'S10': '../assets/cards/spades/10.png',
    'SJ': '../assets/cards/spades/J.png',
    'SQ': '../assets/cards/spades/Q.png',
    'SK': '../assets/cards/spades/K.png',
    'SA': '../assets/cards/spades/A.png',
    'JS': '../assets/cards/jokers/little.png',
    'JB': '../assets/cards/jokers/big.png',
}

function loadCards() {
    document.state.cards = {};
    for (let key in URLS) {
        if (URLS.hasOwnProperty(key)) {
            const img = new Image();
            img.src = URLS[key];
            img.id = key;
            img.className = 'playing-card '
            document.state.cards[key] = img;
        }
    }

    // const hand = document.getElementsByClassName('player-bottom-hand')[0];
    // const card = document.state.cards['C2'].cloneNode(true);
    // hand.appendChild(card);
}