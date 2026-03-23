var countLable = document.getElementById("countLable");
var decreaseBtn = document.getElementById("decreaseBtn");
var resetBtn = document.getElementById("resetBtn");
var increaseBtn = document.getElementById("increaseBtn");
var count = 0;
decreaseBtn.onclick = function () {
    count--;
    countLable.textContent = count.toString();
};
resetBtn.onclick = function () {
    count = 0;
    countLable.textContent = count.toString();
};
increaseBtn.onclick = function () {
    count++;
    countLable.textContent = count.toString();
};
