//String
"I am a string";
//Numbers 
1234.1234;
//booleans 
1 < 2;
true;
false;
//compairesons
1 < 2;
2 > 1;
1 === 1;
1 !== 2;
1 <= 2;
2 >= 1;
	//modulo
42 % 2;
//string length
	"string".length
//substrings
	"substrings".substring(0, 4);
//Console.log
console.log("I log things");
//variables
var meep == "meep";
//Functions
var func = function(thing) {
		return "I Do Things";
	}
//For Loops
for (var i = 10; i >= 0; i--) {
	console.log(i);
}

for (var i = 0; i <= 10; i++) {
	console.log(i);
}
//Arrays
var junkData = ["Eddie Murphy", 49, "peanuts", 31];
//Array .push
junkData.push("More Junk");
//While loops 
var loop = true
var soloLoop = function() {
	while (loop) {
		console.log("Looped once!");
		loop = false;
	}
};

soloLoop();

var number = 4

var loop = function() {
	while (number !== 1) {
		//Your code goes here!
		console.log("I'm looping!");
		number--;
	}
};

loop();
//do
do{
	console.log('stuff');
}while(loop);
//isNaN()
var isEven = function(number) {
  if(number % 2 == 0){
      return true;
  }
  else if (isNaN(number)) {
      return "That isnt a number";
  }
  else{
      return false;
  }
  
};
isEven("meep");