var divisions = []
for(var i = 1;i < 21; i++) {
    if (i % 3 === 0) {
        if (i % 5 === 0) {
            divisions.push(i + "Is dividable by 3 & 5")
        } else {
            divisions.push(i + "Is dividable by 3")
        }
    } else if (i % 5 === 0) {
        divisions.push(i + "Is dividable by 5")
    } else {
        divisions.push(i + "Isn't Divideable by 3 or 5")
    }
}
