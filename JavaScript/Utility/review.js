var getReview = function (movie) {
    switch(movie.toLowerCase()) {
        case "toy story 2":
            return "Great story. Mean prospector."
        case "finding nemo":
            return "Cool animation, and funny turtles."
        case "the lion king":
            return "Great songs."
        default:
            return "I don't know!"
    }

};

var mov = prompt("What movie?");
var rev = getReview(mov);
alert(rev);
console.log(rev);
