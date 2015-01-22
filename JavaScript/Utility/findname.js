/*jshint multistr:true */
var text = "I am Ethan and i go meep moop \
Ethan i be"
var myName = "Ethan";
var hits = []

for (var i = 0; i < text.length; i++) {
	if (text[i] === "E") {
		for (var j = i; j < i + myName.length; j++) {
			hits.push(text[j])
		}
	}
}
if (hits.length === 0) {
	console.log("Your name wasnt found!")
} else {
	console.log(hits)
}
