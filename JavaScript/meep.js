var user = prompt("Do you like to meep?").toLowerCase();
switch (user) {
    case 'yes':
        console.log("Good...good...");
    break;
    case 'no':
        console.log("NON MEEPER!");
    break;
    case 'meep':
        console.log("Excellent, you can continue!");
        var who = prompt("Who are you?","Someone?").toLowerCase();
            if (user === "meep" && who === "seth177") {
                console.log("Welcome Master of meeping");
            } else if (who === "meep" || who === "meep meep") {
                console.log("Welcome " + who + " This is a script made by the Master meeper");
            }
            
    break;
    default:
        console.log("Well do you like to meep or not");
    break;
}
