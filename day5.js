fs = require('fs');

function day5(input) {
    let move = 0 //current move
    let p = 0 // current position
    while(p < input.length) {
        p = doMove(input,p)
        move++
    }
    return move
}

function doMove(input,position) {
    let newPosition = position + input[position]
    if(input[position] > 2) {
        input[position]--
    } else {
        input[position]++
    }
    return newPosition
}



fs.readFile('input/day5','utf-8', (err, input) => { 
    const lines = input.split("\n")
    let data = []
    for(v of lines) {
        data.push(Number(v))
    }
    
    console.log(day5(data))
})

