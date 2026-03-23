const remainingAttemps = document.getElementById("remainingAttempts") as HTMLParagraphElement;
const answer = document.getElementById("answer") as HTMLInputElement;
const feedback = document.getElementById("feedback") as HTMLParagraphElement;
const startBtn = document.getElementById("startBtn") as HTMLButtonElement;
const resetBtn = document.getElementById("resetBtn") as HTMLButtonElement;
const submitBtn = document.getElementById("submitBtn") as HTMLButtonElement;

let random: number;
let attempt: number;
let mercyUsed: boolean;

function gameLogic() {
    submitBtn.style.display = "inline-block";
    resetBtn.style.display = "inline-block";
    answer.style.display = "inline-block";
    startBtn.style.display = "none";

    random = Math.floor(Math.random() * 10) + 1;
    console.log(random);

    attempt = 10;
    remainingAttemps.textContent = `Attempts Remaining : ${attempt}`;
    mercyUsed = false;

    feedback.textContent = "Game Started !!!";
}

startBtn.addEventListener("click", () => {
    gameLogic();
});

submitBtn.addEventListener("click", () => {
    let value = Number(answer.value);

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

    remainingAttemps.textContent = `Attempts Remaining : ${attempt}`;
    answer.value = "";
});

function checkMercy() {
    if (!mercyUsed && attempt === 0) {
        const mercyChance = Math.random() < 0.5;

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
    feedback.textContent = `Game Over, The number was ${random}, Press the Reset Button`;
}

function gameoverWin() {
    answer.style.display = "none";
    submitBtn.style.display = "none";
}

resetBtn.addEventListener("click", () => {
    gameLogic();
});