fs = require('fs');

function day13(input) {
    let severity = 0;
    delay: for(let delay = 0; delay<10000000; delay++) {
        // We could replace the brute force method by a crucible ?
        for(line of input.split("\n")) {
            const matches = line.split(": ");
            const depth = Number(matches[0]);
            const range = Number(matches[1]);
            
            const frequency = 2*range - 2;
            if((delay+depth)%frequency == 0) {
                continue delay
            }
        }

        return delay
    }

    return severity
}


fs.readFile('input/day13','utf-8', (err, data) => { console.log(day13(data)) });