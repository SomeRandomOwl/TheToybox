//Making The Variables in the function global
var dothething = ""
var userChoice = ""
var computerChoice = ""
var inform = ""
var results = ""
var meep = ""
    //----------------
var doTheThing = function() {
        do {
            var userChoice = prompt("Do you choose rock, paper or scissors?", "Rock, Paper, or Scissors?").toLowerCase();
            if (userChoice === null) {
                return null
            } else if (userChoice === "Rock, Paper, or Scissors?") {
                return null
            }
            console.log("The Player Chooses" + " " + userChoice)
            var computerChoice = Math.random()
            console.log("The Random Number Is:" + " " + computerChoice);
            if (computerChoice >= 0 && computerChoice <= 0.33) {
                computerChoice = "Rock";
            } else if (computerChoice >= 0.34 && computerChoice <= 0.66) {
                computerChoice = "Paper";
            } else {
                computerChoice = "Scissors";
            }
            console.log("The Computer Chooses:" + " " + computerChoice);
            var compare = function(choice1, choice2) {
                if (choice1 === choice2) {
                    console.log('It is a Tie!');
                    return "The result is a tie!";
                } else if (choice1 === "rock") {
                    if (choice2 === "Scissors") {
                        console.log('You Win!');
                        return "You win!";
                    } else {
                        console.log("The Computer Wins!");
                        return "The Computer wins!";
                    }
                } else if (choice1 === "paper") {
                    if (choice2 === "Rock") {
                        console.log('You Win!');
                        return "You win!";
                    } else {
                        console.log("The Computer Wins!");
                        return "The Computer wins!";
                    }
                } else if (choice1 === "scissors") {
                    if (choice2 === "Paper") {
                        console.log('You Win!');
                        return "You win!";
                    } else {
                        console.log("The Computer Wins!");
                        return "The Computer wins!";
                    }
                } else {
                    return "Error! Unrecgonized Choice!";
                    console.log('Error, undefined Choice');

                }
            }
            var inform = confirm('The Computer Chooses:' + " " + computerChoice)
            if (inform === true) {
                var results = compare(userChoice, computerChoice);
                alert(results)
                } else {
                    return null
                }
                if (!confirm("Play Again?")) {
                    return;
                }

            }
            while (true)
        }

        //This does something 
        var meep = function() {
                var rock = prompt("Want to play a game", "Yes or No?").toLowerCase();
                if (rock === "yes") {
                    dothething = doTheThing()
                } else {
                    console.log("meh… ")
                }
            }
            //This does nothing
        var nothing = function() {
            console.log('A thing that doesnt do anything did a thing thats nothing.');
        }
        nothing()
            //Starts the game
        meep()