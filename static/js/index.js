const popup = document.querySelector('.chat-popup');
const chatBtn = document.querySelector('.chat-btn');
const emojiBtn = document.querySelector('#emoji-btn');
const picker = new EmojiButton();

// Emoji selection
window.addEventListener('DOMContentLoaded', () => {

    picker.on('emoji', emoji => {
        document.querySelector('input').value += emoji;
        console.log(document.querySelector('input').value)
    });

    emojiBtn.addEventListener('click', () => {
        picker.togglePicker(emojiBtn);
    });
});

// chat button

chatBtn.addEventListener('click', () => {
    popup.classList.toggle('show');
});






