
KEYS = {
    BACKSPACE: 8,
    SHIFT: 16,
    SPACE: 32,
    KEY_0: 48,
    KEY_Z: 90,
    COMMA: 188,
    DASH: 189,
    PERIOD: 190,
    FORWARD_SLASH: 191,
    GRAVE_ACCENT: 192,
};
const right_shift_letters = "qazwsxedcrfvtgb"

var start_time;
var word_count;
var mistakes = 0;

var left_upper = false;
var right_upper = false;

var completed;
var cursor;
var uncompleted;

const reset = async () => {
    const response = await fetch('https://www.randomtext.me/api/gibberish/h1/50');
    const json = await response.json();
    text=json.text_out
        .replace("<h1>","") // randomtext.me only outputs "HTML" text
        .replace("<h1/>","")
        .replace(/\b\w/g, l => l.toUpperCase()) // Words will begin with capitals
        .replace(/\s+/g, ' ') // collapse whitespace just in case.
        .trim()
    // Hardcoded text for unittests.
    // text = "hello world YHNUJM QAZWSXEDCRFVTGB";
    start_time = undefined;
    results_set = false;
    mistakes = 0;
    resetText(text);
    

}

function resetText(text) {
    completed.innerHTML = ""
    cursor.innerHTML = text.charAt(0)
    uncompleted.innerHTML = text.substring(1)
    word_count = text.split(" ").length;
}

document.addEventListener("DOMContentLoaded", function (event) {
    completed = document.getElementById("tutor-completed");
    cursor = document.getElementById("tutor-cursor");
    uncompleted = document.getElementById("tutor-uncompleted");
    reset();
});

document.addEventListener('keyup', function (event) {
    if (event.location === KeyboardEvent.DOM_KEY_LOCATION_LEFT) {
        left_upper = false
    } else if (event.location === KeyboardEvent.DOM_KEY_LOCATION_RIGHT) {
        right_upper = false
    }
});
document.addEventListener('keydown', function (event) {
    if (!start_time) {
        start_time = new Date().getTime();
    }

    var key = '';

    switch (event.keyCode) {
        case KEYS.SPACE:
            event.preventDefault();
            key = ' ';
            break;
        case KEYS.FORWARD_SLASH:
            event.preventDefault();
            key = '/';
            break;
        case KEYS.COMMA:
            key = ',';
            break;
        case KEYS.PERIOD:
            key = '.';
            break;
        case 173:
            key = '-';
            break;
        case KEYS.SHIFT:
            if (event.location === KeyboardEvent.DOM_KEY_LOCATION_LEFT) {
                left_upper = true
                return
            } else if (event.location === KeyboardEvent.DOM_KEY_LOCATION_RIGHT) {
                right_upper = true
                return
            }
        case KEYS.BACKSPACE:
            uncompleted.innerHTML = cursor.innerHTML + uncompleted.innerHTML;
            cursor.innerHTML = completed.innerHTML.slice(-1);
            completed.innerHTML = completed.innerHTML.slice(0, -1);
            break;
        default:
            if (KEYS.KEY_0 <= event.keyCode && event.keyCode <= KEYS.KEY_Z) {
                key = String.fromCharCode(event.keyCode);
                key = key.toLowerCase();
                if (right_upper && left_upper){
                    key=''; // Disallow holding both shifts down.
                }
                else if (right_upper && right_shift_letters.includes(key)) {
                    key = key.toUpperCase();
                }
                else if (left_upper && !right_shift_letters.includes(key)) {
                    key = key.toUpperCase();
                }
                break;
            }
    }
    if (key == cursor.innerHTML) {
        completed.innerHTML += key;
        cursor.innerHTML = (uncompleted.innerHTML.charAt(0));
        uncompleted.innerHTML = uncompleted.innerHTML.substr(1);
    }
    else {
        mistakes++;
    }
    if (uncompleted.innerHTML.length == 0 && cursor.innerHTML.length == 0) {
        var stop_time = new Date().getTime();
        var result = document.getElementById("result");
        var wpm = word_count / (((stop_time - start_time) / 1000) / 60);
        var mpw = mistakes/word_count;
        result.innerHTML = `WPM:${wpm.toFixed(2)}; MPW:${mpw.toFixed(2)}; Words:${word_count}; Mistakes:${mistakes};`;
        reset();
    }
});
