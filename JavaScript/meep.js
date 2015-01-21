var meep = confirm("Meep?");

switch(meep) {
    case(true):
        console.log("meep meep");
        break;
    case(false):
        console.log("No meep....");
        break;
    case("Meep"):
        console.log("meep?....");
        break;
    default:
        console.log("This isnt even possible...what did you do?");
        break;
}