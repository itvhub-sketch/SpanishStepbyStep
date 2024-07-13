var cardSide = "QuestionSide";

function showCard() {
    $(".practice_card").show();
}

function flipCard(cardId) {
    const cardElement = document.getElementById(`card-${cardId}`);
    const cardFront = cardElement.querySelector('.card-front');
    const cardBack = cardElement.querySelector('.card-back');

    if (cardFront && cardBack) {
        const isFrontVisible = cardFront.style.display !== 'none';
        cardFront.style.display = isFrontVisible ? 'none' : 'block';
        cardBack.style.display = isFrontVisible ? 'block' : 'none';
    } else {
        console.error('Card elements not found.');
    }
}

function toggleTextToSpeech(button) {
    const cardId = button.dataset.cardId;
    const deckId = window.location.pathname.split('/')[3]; // Assuming the deck_id is the 4th part of the URL path
    const questionAudioUrl = button.dataset.questionAudio;
    const answerAudioUrl = button.dataset.answerAudio;

    const url = `/deck/practice/${deckId}/text_to_speech/${cardId}/`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
        },
        body: JSON.stringify({}),
    })
    .then(response => response.json())
    .then(data => {
        const questionAudio = new Audio(questionAudioUrl);
        const answerAudio = new Audio(answerAudioUrl);

        questionAudio.play();
        questionAudio.addEventListener('ended', () => {
            answerAudio.play();
        });
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

$(document).ready(function() {
    showCard();
    $(".practicese_card").on('click', function() {
        const cardId = $(this).attr('id').split('-')[1]; // Extract card ID from element ID
        flipCard(cardId);
    });

    const ttsButtons = document.querySelectorAll('.tts-button');
    ttsButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.stopPropagation(); // Prevent flipCard from being called
            toggleTextToSpeech(button);
        });
    });
});
