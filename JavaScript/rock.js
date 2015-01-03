var dothething = function() {
        var userChoice = prompt("Do you choose rock, paper or scissors?")
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
            if (choice1.toLowerCase() === choice2.toLowerCase()) {
                return "The result is a tie!";
                console.log('It is a Tie!');
            } else if (choice1.toLowerCase() === "rock") {
                if (choice2 === "Scissors") {
                    return "You win!";
                    console.log('You Win!');
                } else {
                    return "The Computer wins!";
                    console.log("The Computer Wins!");
                }
            } else if (choice1.toLowerCase() === "paper") {
                if (choice2 === "Rock") {
                    return "You win!";
                    console.log('You Win!');
                } else {
                    return "The Computer wins!";
                    console.log("The Computer Wins!");

                }
            } else if (choice1.toLowerCase() === "scissors") {
                if (choice2 === "Paper") {
                    return "You win!";
                    console.log('You Win!');
                } else {
                    return "The Computer wins!";
                    console.log("The Computer Wins!");

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
            console.log('error');
        }
    }
    //This does something
dothething()