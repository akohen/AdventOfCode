fs = require('fs');

function day1(input) {
    let result = 0
    let result_part2 = 0
    const len = input.length

    for ( let i=0; i<input.length; i++) {
        const current = input[i]
        const next = input[(i+1)%len]
        const halfway = input[(i+len/2)%len]

        if ( current == next ) {
            result += Number(current)
        }
        if ( current == halfway ) {
            result_part2 += Number(current)
        }
    }
    return [result, result_part2]
}


fs.readFile('input/day1','utf-8', (err, data) => { console.log(day1(data)) });