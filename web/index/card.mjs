export {
    addToHand,
}

function addToHand(direction, cardKey) {
    const card = document.state.cards[cardKey].cloneNode(true);
    const element = $(`#${direction} .hand`);
    let rest = element.children().length !== 0;
    card.className += `${rest ? 'rest' : ''}`;
    element.append(card);

    if (direction === 'bottom') {
        card.addEventListener('click', () => {
            if (~card.className.indexOf('selected')) {
                card.className = card.className.replace('selected', '')
            } else {
                card.className += ' selected';
            }
        });
    }
}