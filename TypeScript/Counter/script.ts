const countLable = document.getElementById("countLable") as HTMLSpanElement;
const decreaseBtn = document.getElementById("decreaseBtn") as HTMLSpanElement;
const resetBtn = document.getElementById("resetBtn") as HTMLSpanElement;
const increaseBtn = document.getElementById("increaseBtn") as HTMLSpanElement;

let count: number = 0;

decreaseBtn.onclick = function(): void {
    count--;
    countLable.textContent = count.toString();
}

resetBtn.onclick = function(): void {
    count = 0;
    countLable.textContent = count.toString();
}

increaseBtn.onclick = function(): void {
    count++;
    countLable.textContent = count.toString();
}