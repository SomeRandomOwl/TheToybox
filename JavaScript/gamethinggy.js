// Check if the user is ready to play!
alert("This script requires you to be looking at your browsers console through inspect element")
confirm("Are you ready");
var age = prompt("How old are ye?");
if (age <= 13) {
    console.log("You ant really old enough for this...but thats not stopping you now is it?")
} else if (age > 1000) {
    console.log("Hello Doctor")
} else if (age < 1000 && age >= 14) {
    console.log("Your old enough to make your own decisions!")
}
console.log("You are at a Justin Bieber concert, and you hear this lyric 'Lace my shoes off, start racing.'")
console.log("Suddenly, Bieber stops and says, 'Who wants to race me?'")
var userAnswer = prompt("Do you want to shoot him in his head?")
if (userAnswer === "yes" || userAnswer === "Yes") {
    console.log("You take the shot finally killing justin beiber makeing the world celebrate!");
} else {
    console.log("You decide to not take the shot and from the background you hear another sniper shot and see beiber drop dead on the floor");
}

var feedback = prompt("Rate this murdering game")
if (feedback >= 8) {
    console.log("Thank you you for you assistance in murder");
} else {
    console.log("I killed him myself no thanks to you...");
}
