var remainingAttemps = document.getElementById("remainingAttempts");
var answer = document.getElementById("answer");
var feedback = document.getElementById("feedback");
var startBtn = document.getElementById("startBtn");
var resetBtn = document.getElementById("resetBtn");
var submitBtn = document.getElementById("submitBtn");
var random;
var attempt;
var mercyUsed;
function gameLogic() {
    submitBtn.style.display = "inline-block";
    resetBtn.style.display = "inline-block";
    answer.style.display = "inline-block";
    startBtn.style.display = "none";
    random = Math.floor(Math.random() * 10) + 1;
    console.log(random);
    attempt = 10;
    remainingAttemps.textContent = "Attempts Remaining : ".concat(attempt);
    mercyUsed = false;
    feedback.textContent = "Game Started !!!";
}
startBtn.addEventListener("click", function () {
    gameLogic();
});
submitBtn.addEventListener("click", function () {
    var value = Number(answer.value);
    switch (true) {
        case value > random:
            feedback.textContent = "Too High.";
            break;
        case value < random:
            feedback.textContent = "Too Low.";
            break;
        case value === random:
            feedback.textContent = "Correct ! You Win.";
            gameoverWin();
            break;
        default:
            feedback.textContent = "Invalid Input";
    }
    if (value !== random) {
        attempt--;
    }
    checkMercy();
    remainingAttemps.textContent = "Attempts Remaining : ".concat(attempt);
    answer.value = "";
});
function checkMercy() {
    if (!mercyUsed && attempt === 0) {
        var mercyChance = Math.random() < 0.5;
        if (mercyChance) {
            mercyUsed = true;
            attempt++;
            feedback.textContent = "You got an extra chance";
            return;
        }
    }
    if (attempt === 0 && (mercyUsed || !mercyUsed)) {
        gameover();
    }
}
function gameover() {
    answer.style.display = "none";
    submitBtn.style.display = "none";
    feedback.textContent = "Game Over, The number was ".concat(random, ", Press the Reset Button");
}
function gameoverWin() {
    answer.style.display = "none";
    submitBtn.style.display = "none";
}
resetBtn.addEventListener("click", function () {
    gameLogic();
});
