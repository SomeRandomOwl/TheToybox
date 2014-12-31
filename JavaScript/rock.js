var userChoice = prompt("Do you choose rock, paper or scissors?")
var computerChoice = Math.random()

if (computerChoice >= 0 && computerChoice <= 0.33) {
    computerChoice = "Rock";
} else if (computerChoice >= 0.34 && computerChoice <= 0.66) {
    computerChoice = "Paper";
} else {
    computerChoice = "Scissors";
}
console.log('The Computer Chooses:' + " " + computerChoice);

var compare = function(choice1, choice2) {
    if (choice1 === choice2) {
        return "The result is a tie!";
    } else if (choice1 === "rock" || choice1 === "Rock") {
        if (choice2 === "Scissors") {
            return "You win!";
        } else {
            return "The Computer wins!";
        }
    } else if (choice1 === "paper" || choice1 === "Paper") {
        if (choice2 === "Rock") {
            return "You win!";
        } else {
            return "The Computer wins!";
        }
    } else if (choice1 === "scissors" || choice1 === "Scissors") {
        if (choice2 === "Paper") {
            return "You win!";
        } else {
            return "The Computer wins!";
        }
    }
}
var dothething = function() {
    if (userChoice === null || userChoice !== "rock" || userChoice !== "Rock" || userChoice !== "paper" || userChoice !== "Paper" || userChoice !== "scissors" || userChoice !== "Scissors") {
        return "You have to make a choice!";
        var userChoice = prompt("Do you choose rock, paper or scissors?");
        dothething();
    }
    var inform = confirm('The Computer Chooses:' + " " + computerChoice)
    if (inform === true) {
        var results = compare(userChoice, computerChoice);
        alert(results)
    } else {
        console.log('error');
    }
}
//This does something
dothething()