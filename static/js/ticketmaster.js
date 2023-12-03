document.addEventListener('DOMContentLoaded', function() {
    console.log("JavaScript is working!");

    var textContainer = document.getElementById('animated-text');
    if (textContainer) {
        var words = ['Events', 'Music', 'Sports', 'Concerts'], wordIndex = 0;
        var letterIndex = 0, currentWord = '', addingLetter = true;

        function updateText() {
            if (addingLetter) {
                if (letterIndex < words[wordIndex].length) {
                    currentWord += words[wordIndex].charAt(letterIndex++);
                } else {
                    addingLetter = false;
                    setTimeout(updateText, 2000);
                    return;
                }
            } else {
                if (letterIndex > 0) {
                    currentWord = currentWord.slice(0, -1);
                    letterIndex--;
                } else {
                    addingLetter = true;
                    wordIndex = (wordIndex + 1) % words.length;
                }
            }
            textContainer.textContent = currentWord;
            setTimeout(updateText, addingLetter ? 200 : 100);
        }

        updateText();
    }
});
