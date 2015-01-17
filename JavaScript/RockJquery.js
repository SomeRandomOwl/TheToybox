//Making The Variables in the function global
var dothething = ""
var userChoice = ""
var computerChoice = ""
var done = false
    //----------------
var doTheThing = function() {
        do {
            var userChoice = ""

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
                    console.log('It is a Tie!'); 
                    var done = true
                    return "The result is a tie!";
                } else if (choice1.toLowerCase() === "rock") {
                    if (choice2 === "Scissors") {
                        console.log('You Win!');
                        var done = true
                        return "You win!";
                    } else {
                        console.log("The Computer Wins!");
                        var done = true
                        return "The Computer wins!";
                    }
                } else if (choice1.toLowerCase() === "paper") {
                    if (choice2 === "Rock") {
                        console.log('You Win!');
                        var done = true
                        return "You win!";
                    } else {
                        console.log("The Computer Wins!");
                        var done = true
                        return "The Computer wins!";
                    }
                } else if (choice1.toLowerCase() === "scissors") {
                    if (choice2 === "Paper") {
                        console.log('You Win!');
                        var done = true
                        return "You win!";
                    } else {
                        console.log("The Computer Wins!");
                        var done = true
                        return "The Computer wins!";
                    }
                } else {
                    return "Error! Unrecgonized Choice!";
                    console.log('Error, undefined Choice');
                    var done = false
                }
            }
            var inform = confirm('The Computer Chooses:' + " " + computerChoice)
            if (inform === true) {
                var results = compare(userChoice, computerChoice);
                alert(results)
            } else {
                console.log('error');
            }
            if (!confirm("Play Again?")) {
                return;
            }

        } while (true)
    }
    //This does something 
var meep = function() {
        var rock = ""
        if (rock.toLowerCase() === "yes") {
            dothething = doTheThing()
        } else if (rock = null) {
            console.log('Null Error, The cancel button was clicked');
        } else {
            console.log("meh… ")
        }
    }
    //This does nothing
var nothing = function() {
        console.log('A thing that doesnt do anything did a thing thats nothing.');
    }
    //Starts the game
   //meep() 
 